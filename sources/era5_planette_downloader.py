#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Planette ERA5 Downloader
从 AWS S3 (planette-era5) 下载 ERA5 数据并导出为 NetCDF / Zarr

数据源: s3://planette-era5/era5/{variable}/{frequency}/{grid}/
格式: Icechunk Zarr

依赖:
    pip install xarray icechunk s3fs numpy netcdf4 requests dask

Usage:
    # 下载月平均 2m 气温
    python era5_planette_downloader.py -v t2m -f month \\
        -t 2020-01-01 2024-12-31 -o ./t2m_monthly.nc

    # 下载并裁剪区域
    python era5_planette_downloader.py -v t2m tp -f month \\
        -t 2020-01-01 2024-12-31 -r 70 140 15 55 \\
        -o ./output/ --auto-name --concurrent

    # 查看可用变量
    python era5_planette_downloader.py --list-variables
"""

import os
import sys
import json
import time
import signal
import hashlib
import logging
import argparse
import requests
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, List, Tuple, Any
from concurrent.futures import ThreadPoolExecutor, as_completed

import xarray as xr
import numpy as np
import icechunk as ic
import icechunk.config as ic_config

__version__ = "1.0.0"

# ==================== S3 配置 ====================
S3_CONFIG = {
    "bucket": "planette-era5",
    "region": "us-east-2",
    "prefix": "era5",
    "anonymous": True,
    "max_retries": 3,
    "retry_delay": 2,
}

# Icechunk 并发优化配置
ICECHUNK_CONFIG = ic_config.RepositoryConfig(
    max_concurrent_requests=512,
    get_partial_values_concurrency=50,
)

FREQUENCY_OPTIONS = ["day", "7day", "month", "3month"]
GRID_OPTIONS = ["0p25latx0p25lon"]

# ==================== 单位转换 ====================
UNIT_CONVERSIONS = {
    "t2m":  {"factor": 1,           "offset": -273.15,     "from": "K",       "to": "degC",  "name": "2m Temperature"},
    "d2m":  {"factor": 1,           "offset": -273.15,     "from": "K",       "to": "degC",  "name": "2m Dewpoint Temperature"},
    "tp":   {"factor": 1000,        "offset": 0,            "from": "m",       "to": "mm",    "name": "Total Precipitation"},
    "sp":   {"factor": 0.01,        "offset": 0,            "from": "Pa",      "to": "hPa",   "name": "Surface Pressure"},
    "msl":  {"factor": 0.01,        "offset": 0,            "from": "Pa",      "to": "hPa",   "name": "Mean Sea Level Pressure"},
    "u10m": {"factor": 1,           "offset": 0,            "from": "m s-1",   "to": "m s-1", "name": "10m U-component Wind"},
    "v10m": {"factor": 1,           "offset": 0,            "from": "m s-1",   "to": "m s-1", "name": "10m V-component Wind"},
    "u850": {"factor": 1,           "offset": 0,            "from": "m s-1",   "to": "m s-1", "name": "850hPa U-component Wind"},
    "v850": {"factor": 1,           "offset": 0,            "from": "m s-1",   "to": "m s-1", "name": "850hPa V-component Wind"},
    "t850": {"factor": 1,           "offset": -273.15,     "from": "K",       "to": "degC",  "name": "850hPa Temperature"},
    "z500": {"factor": 1/98.0665,   "offset": 0,            "from": "m2 s-2",  "to": "dagpm", "name": "500hPa Geopotential Height"},
    "r500": {"factor": 1,           "offset": 0,            "from": "%",       "to": "%",     "name": "500hPa Relative Humidity"},
    "slp":  {"factor": 0.01,        "offset": 0,            "from": "Pa",      "to": "hPa",   "name": "Sea Level Pressure"},
    "sst":  {"factor": 1,           "offset": -273.15,     "from": "K",       "to": "degC",  "name": "Sea Surface Temperature"},
}

# 临时文件列表 (用于中断清理)
_temp_files: List[Path] = []


# ==================== 日志 ====================
def setup_logging(debug: bool = False):
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%H:%M:%S",
        handlers=[logging.StreamHandler(sys.stdout)],
    )


logger = logging.getLogger(__name__)


# ==================== 信号处理 ====================
def _cleanup_handler(signum, frame):
    for p in _temp_files:
        if p.exists():
            try:
                p.unlink()
            except Exception:
                pass
    logger.warning("User interrupted, cleaned up temp files")
    sys.exit(130)


# ==================== S3 发现 ====================
def _s3_list(prefix: str = "", delimiter: str = "/") -> Optional[ET.Element]:
    url = f"https://{S3_CONFIG['bucket']}.s3.amazonaws.com/"
    params = {"prefix": prefix, "delimiter": delimiter, "max-keys": "1000"}
    try:
        resp = requests.get(url, params=params, timeout=15)
        resp.raise_for_status()
        return ET.fromstring(resp.content)
    except Exception as e:
        logger.warning(f"S3 request failed ({prefix}): {e}")
        return None


def discover_variables() -> List[str]:
    root = _s3_list(f"{S3_CONFIG['prefix']}/", "/")
    if root is None:
        return []
    ns = {"s3": "http://s3.amazonaws.com/doc/2006-03-01/"}
    return sorted(
        {
            p.text.strip("/").split("/")[1]
            for p in root.findall(".//s3:CommonPrefixes/s3:Prefix", ns)
            if len(p.text.strip("/").split("/")) >= 2
        }
    )


def discover_frequencies(variable: str) -> List[str]:
    root = _s3_list(f"{S3_CONFIG['prefix']}/{variable}/", "/")
    if root is None:
        return []
    ns = {"s3": "http://s3.amazonaws.com/doc/2006-03-01/"}
    return sorted(
        {
            p.text.strip("/").split("/")[2]
            for p in root.findall(".//s3:CommonPrefixes/s3:Prefix", ns)
            if len(p.text.strip("/").split("/")) >= 3
        }
    )


def discover_grids(variable: str, frequency: str) -> List[str]:
    root = _s3_list(f"{S3_CONFIG['prefix']}/{variable}/{frequency}/", "/")
    if root is None:
        return []
    ns = {"s3": "http://s3.amazonaws.com/doc/2006-03-01/"}
    return sorted(
        {
            p.text.strip("/").split("/")[3]
            for p in root.findall(".//s3:CommonPrefixes/s3:Prefix", ns)
            if len(p.text.strip("/").split("/")) >= 4
        }
    )


def list_s3_tree(variable: str):
    freqs = discover_frequencies(variable)
    print(f"\n  {variable}/")
    for fi, freq in enumerate(freqs):
        prefix = "  └──" if fi == len(freqs) - 1 else "  ├──"
        grids = discover_grids(variable, freq)
        grid_str = ", ".join(grids) if grids else "?"
        print(f"  {prefix} {freq}/  ({grid_str})")


# ==================== 断点续传 ====================
class CheckpointManager:
    def __init__(self, path: str):
        self.path = Path(path)
        self.completed: set = set()
        self._load()

    def _load(self):
        if self.path.exists():
            try:
                with open(self.path) as f:
                    self.completed = set(json.load(f).get("completed", []))
                logger.info(f"Loaded checkpoint: {len(self.completed)} completed")
            except Exception:
                pass

    def save(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.path, "w") as f:
            json.dump({"completed": list(self.completed), "ts": datetime.now().isoformat()}, f, indent=2)

    def is_done(self, key: str) -> bool:
        return key in self.completed

    def mark_done(self, key: str):
        self.completed.add(key)
        self.save()


# ==================== 数据校验 ====================
def validate_data(ds: xr.Dataset, variable: str) -> Dict[str, Any]:
    if variable not in ds.data_vars:
        return {}
    data = ds[variable]
    total = data.size
    nan_count = int(data.isnull().sum())
    nan_ratio = nan_count / total if total > 0 else 0
    val_min = float(np.nanmin(data.values))
    val_max = float(np.nanmax(data.values))
    val_mean = float(np.nanmean(data.values))

    logger.info(f"  Validation: {total:,} points | NaN={nan_ratio:.2%} | "
                f"range=[{val_min:.2f}, {val_max:.2f}] | mean={val_mean:.2f}")
    if nan_ratio > 0.5:
        logger.warning(f"  High NaN ratio ({nan_ratio:.1%}), check data integrity")
    return {"total": total, "nan_ratio": nan_ratio, "min": val_min, "max": val_max, "mean": val_mean}


# ==================== 核心下载器 ====================
class ERA5Downloader:
    def __init__(
        self,
        variable: str,
        frequency: str,
        grid: str = "0p25latx0p25lon",
        convert_units: bool = True,
        resume: bool = True,
        workers: int = 4,
    ):
        self.variable = variable
        self.frequency = frequency
        self.grid = grid
        self.convert_units = convert_units
        self.resume = resume
        self.workers = workers

        self.zarr_path = (
            f"{S3_CONFIG['prefix']}/{variable}/{frequency}/{grid}/"
            f"era5_{variable}_{frequency}_{grid}.zarr"
        )
        self.s3_url = f"s3://{S3_CONFIG['bucket']}/{self.zarr_path}"

    def _open_dataset(self) -> xr.Dataset:
        for attempt in range(S3_CONFIG["max_retries"]):
            try:
                storage = ic.s3_storage(
                    bucket=S3_CONFIG["bucket"],
                    prefix=self.zarr_path,
                    region=S3_CONFIG["region"],
                    anonymous=S3_CONFIG["anonymous"],
                )
                repo = ic.Repository.open(storage=storage, config=ICECHUNK_CONFIG)
                session = repo.readonly_session(branch="main")
                ds = xr.open_dataset(
                    session.store,
                    engine="zarr",
                    consolidated=False,
                    decode_timedelta=True,
                    chunks={},
                )
                return ds
            except Exception as e:
                logger.warning(f"  Attempt {attempt + 1}/{S3_CONFIG['max_retries']}: {e}")
                if attempt < S3_CONFIG["max_retries"] - 1:
                    time.sleep(S3_CONFIG["retry_delay"] * (attempt + 1))
                else:
                    raise

    def _apply_filters(
        self,
        ds: xr.Dataset,
        time_range: Optional[Tuple[str, str]] = None,
        region: Optional[Tuple[float, float, float, float]] = None,
    ) -> xr.Dataset:
        if time_range:
            logger.info(f"  Time: {time_range[0]} ~ {time_range[1]}")
            ds = ds.sel(time=slice(time_range[0], time_range[1]))
        if region:
            lon_min, lon_max, lat_min, lat_max = region
            logger.info(f"  Region: lon[{lon_min}:{lon_max}] lat[{lat_min}:{lat_max}]")
            ds = ds.sel(lon=slice(lon_min, lon_max), lat=slice(lat_max, lat_min))
        return ds

    def _apply_unit_conversion(self, ds: xr.Dataset) -> xr.Dataset:
        if not self.convert_units or self.variable not in UNIT_CONVERSIONS:
            return ds
        cfg = UNIT_CONVERSIONS[self.variable]
        if self.variable in ds.data_vars:
            ds[self.variable] = ds[self.variable] * cfg["factor"] + cfg["offset"]
            ds[self.variable].attrs["units"] = cfg["to"]
            ds[self.variable].attrs["long_name"] = cfg["name"]
            logger.info(f"  Unit conversion: {cfg['from']} -> {cfg['to']}")
        return ds

    def _format_eta(self, seconds: float) -> str:
        if seconds < 60:
            return f"{seconds:.0f}s"
        m, s = divmod(int(seconds), 60)
        if m < 60:
            return f"{m}m{s:02d}s"
        h, m = divmod(m, 60)
        return f"{h}h{m:02d}m"

    def _load_with_progress(self, ds: xr.Dataset) -> xr.Dataset:
        """多线程并发从 S3 加载数据到内存，实时显示进度和速度"""
        n_time = len(ds.time)
        total_bytes = sum(ds[v].nbytes for v in ds.data_vars)
        total_mb = total_bytes / 1024 / 1024

        logger.info(f"  Downloading {total_mb:.1f} MB ({n_time} steps, {self.workers} workers)...")

        # 按 batch 分配任务，每个 worker 处理若干时间步
        def _load_range(start_end):
            s, e = start_end
            return ds.isel(time=slice(s, e)).compute()

        # 划分 batch
        batch_size = max(1, (n_time + self.workers - 1) // self.workers)
        batches = []
        for i in range(0, n_time, batch_size):
            batches.append((i, min(i + batch_size, n_time)))

        t0 = time.time()
        results = [None] * len(batches)
        completed = 0

        with ThreadPoolExecutor(max_workers=self.workers) as pool:
            future_to_idx = {pool.submit(_load_range, b): idx for idx, b in enumerate(batches)}

            for future in as_completed(future_to_idx):
                idx = future_to_idx[future]
                results[idx] = future.result()
                completed += 1

                elapsed = time.time() - t0
                done_steps = sum(b[1] - b[0] for b in batches[:completed])
                done_mb = total_mb * done_steps / n_time
                speed = done_mb / elapsed if elapsed > 0 else 0
                eta = elapsed / completed * (len(batches) - completed)

                bar_len = 30
                filled = int(bar_len * completed / len(batches))
                bar = "█" * filled + "░" * (bar_len - filled)
                pct = completed / len(batches) * 100

                print(
                    f"\r  [{bar}] {pct:5.1f}% | "
                    f"{done_mb:.1f}/{total_mb:.1f} MB | "
                    f"{speed:.3f} MB/s | "
                    f"ETA {self._format_eta(eta)} | "
                    f"{done_steps}/{n_time} steps    ",
                    end="", flush=True,
                )

        print()

        elapsed_total = time.time() - t0
        avg_speed = total_mb / elapsed_total if elapsed_total > 0 else 0
        logger.info(f"  Downloaded {total_mb:.1f} MB in {self._format_eta(elapsed_total)} ({avg_speed:.3f} MB/s avg)")

        return xr.concat(results, dim="time")

    def _export_netcdf(self, ds: xr.Dataset, output_path: str, raw_bytes: int, compress: bool = True) -> dict:
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        _temp_files.append(output_file)

        encoding = {}
        if compress:
            for var in ds.data_vars:
                encoding[var] = {
                    "zlib": True,
                    "complevel": 4,
                    "shuffle": True,
                    "_FillValue": -9999,
                    "dtype": "float32",
                }

        t0 = time.time()
        ds.to_netcdf(
            output_file,
            format="NETCDF4",
            engine="netcdf4",
            encoding=encoding if encoding else None,
            unlimited_dims=["time"],
        )
        elapsed = time.time() - t0

        size_mb = output_file.stat().st_size / 1024 / 1024
        raw_mb = raw_bytes / 1024 / 1024
        ratio = raw_mb / size_mb if size_mb > 0 else 1.0

        logger.info(f"  Written: {size_mb:.2f} MB (ratio: {ratio:.1f}x) in {elapsed:.1f}s")

        if output_file in _temp_files:
            _temp_files.remove(output_file)
        return {"elapsed": elapsed, "size_mb": size_mb, "ratio": ratio}

    def _export_zarr(self, ds: xr.Dataset, output_path: str) -> dict:
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        _temp_files.append(output_file)

        t0 = time.time()
        ds.to_zarr(output_file, mode="w")
        elapsed = time.time() - t0

        logger.info(f"  Written Zarr in {elapsed:.1f}s")
        if output_file in _temp_files:
            _temp_files.remove(output_file)
        return {"elapsed": elapsed}

    def download(
        self,
        time_range: Optional[Tuple[str, str]] = None,
        region: Optional[Tuple[float, float, float, float]] = None,
        output_path: str = None,
        output_format: str = "netcdf4",
        validate: bool = True,
        compress: bool = True,
    ) -> str:
        logger.info(f"Connecting: {self.s3_url}")

        # 断点续传检查
        if self.resume and output_path:
            ckpt_hash = hashlib.md5(f"{self.s3_url}{time_range}{region}".encode()).hexdigest()[:8]
            ckpt = CheckpointManager(str(Path(output_path).with_suffix(f".{ckpt_hash}.ckpt")))
            if ckpt.is_done(f"{self.variable}_{self.frequency}"):
                logger.info(f"Skipping completed: {self.variable}_{self.frequency}")
                return output_path
        else:
            ckpt = None

        # 打开 + 筛选
        ds = self._open_dataset()
        ds = self._apply_filters(ds, time_range, region)

        # 数据信息
        n_time = len(ds.time)
        logger.info(f"  {n_time} time steps | dims: {dict(ds.sizes)}")

        raw_bytes = sum(ds[v].size * 4 for v in ds.data_vars)
        raw_mb = raw_bytes / 1024 / 1024
        logger.info(f"  Estimated: {raw_mb:.1f} MB (uncompressed)")

        # 单位转换 (延迟计算)
        ds = self._apply_unit_conversion(ds)

        # 全局属性
        ds.attrs.update({
            "source": "Planette ERA5 Archive (s3://planette-era5)",
            "original_source": "ECMWF ERA5 Reanalysis",
            "downloaded_by": f"era5_planette_downloader v{__version__}",
            "download_time": datetime.now().isoformat(),
        })

        # 逐时间步加载到内存 (带实时进度)
        ds_loaded = self._load_with_progress(ds)

        # 本地导出
        logger.info(f"  Writing to {output_path}...")
        if output_format == "netcdf4":
            self._export_netcdf(ds_loaded, output_path, raw_bytes, compress=compress)
        elif output_format == "zarr":
            self._export_zarr(ds_loaded, output_path)

        # 校验 (从本地文件读取)
        if validate and output_format == "netcdf4":
            logger.info("  Validating...")
            ds_check = xr.open_dataset(output_path)
            validate_data(ds_check, self.variable)
            ds_check.close()

        # 标记完成并清理 checkpoint
        if ckpt:
            ckpt.mark_done(f"{self.variable}_{self.frequency}")
            try:
                ckpt.path.unlink()
            except Exception:
                pass

        return output_path


# ==================== 自动命名 ====================
def auto_filename(
    variable: str,
    frequency: str,
    time_range: Optional[Tuple[str, str]] = None,
    region: Optional[Tuple[float, float, float, float]] = None,
    suffix: str = ".nc",
) -> str:
    name = f"era5_{variable}_{frequency}"
    if time_range:
        name += f"_{time_range[0]}_{time_range[1]}"
    if region:
        name += f"_{int(region[0])}-{int(region[1])}E_{int(region[2])}-{int(region[3])}N"
    return name + suffix


# ==================== 单变量下载封装 ====================
def download_one(var: str, args, available_vars: Optional[List[str]] = None) -> Tuple[str, bool, str]:
    if available_vars is not None and var not in available_vars:
        return (var, False, f"Variable '{var}' not available on S3")

    fmt = getattr(args, "format", "netcdf4")
    suffix = ".nc" if fmt == "netcdf4" else ".zarr"

    if args.auto_name or (len(args.variable) > 1 and Path(args.output).is_dir()):
        fname = auto_filename(var, args.frequency, args.time_range, args.region, suffix)
        out = str(Path(args.output) / fname)
    else:
        out = args.output

    try:
        dl = ERA5Downloader(
            variable=var,
            frequency=args.frequency,
            grid=args.grid,
            convert_units=not args.no_convert,
            resume=not args.no_resume,
            workers=args.workers,
        )
        dl.download(
            time_range=tuple(args.time_range) if args.time_range else None,
            region=tuple(args.region) if args.region else None,
            output_path=out,
            output_format=fmt,
            validate=not args.no_validate,
            compress=not args.no_compress,
        )
        return (var, True, out)
    except KeyboardInterrupt:
        return (var, False, "Interrupted")
    except Exception as e:
        return (var, False, str(e))


# ==================== CLI ====================
def _format_eta_global(seconds: float) -> str:
    if seconds < 60:
        return f"{seconds:.1f}s"
    m, s = divmod(int(seconds), 60)
    if m < 60:
        return f"{m}m{s:02d}s"
    h, m = divmod(m, 60)
    return f"{h}h{m:02d}m"


def main():
    parser = argparse.ArgumentParser(
        description=f"Planette ERA5 Downloader v{__version__}",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Download monthly 2m temperature
  %(prog)s -v t2m -f month -t 2020-01-01 2024-12-31 -o ./t2m_monthly.nc

  # Download with region crop
  %(prog)s -v t2m -f month -t 2020-01-01 2024-12-31 -r 70 140 15 55 -o ./t2m.nc

  # Multi-variable concurrent download
  %(prog)s -v t2m tp slp -f month -o ./output/ --auto-name --concurrent

  # Export as Zarr
  %(prog)s -v t2m -f day -o ./t2m.zarr --format zarr

  # List available variables
  %(prog)s --list-variables

  # Show data tree for a variable
  %(prog)s -v t2m --list-tree

Variables: t2m, d2m, tp, sp, msl, slp, sst, u10m, v10m, u850, v850, t850, z500, r500
Frequencies: day, 7day, month, 3month
""",
    )

    parser.add_argument("-v", "--variable", nargs="+", help="Variable name(s)")
    parser.add_argument("-f", "--frequency", choices=FREQUENCY_OPTIONS, help="Time frequency")
    parser.add_argument("-g", "--grid", default="0p25latx0p25lon", help="Grid resolution")

    parser.add_argument("-t", "--time-range", nargs=2, metavar=("START", "END"), help="Time range (YYYY-MM-DD)")
    parser.add_argument("-r", "--region", nargs=4, type=float, metavar=("LON_MIN", "LON_MAX", "LAT_MIN", "LAT_MAX"),
                        help="Spatial region")
    parser.add_argument("-o", "--output", help="Output file or directory")

    parser.add_argument("--format", choices=["netcdf4", "zarr"], default="netcdf4", help="Output format")
    parser.add_argument("--auto-name", action="store_true", help="Auto-generate filenames")
    parser.add_argument("--concurrent", action="store_true", help="Download variables concurrently")

    parser.add_argument("--no-convert", action="store_true", help="Disable unit conversion")
    parser.add_argument("--no-resume", action="store_true", help="Disable checkpoint resume")
    parser.add_argument("--no-validate", action="store_true", help="Skip data validation")
    parser.add_argument("--no-compress", action="store_true", help="Disable compression (faster export)")
    parser.add_argument("--workers", type=int, default=4, help="Concurrent download workers (default: 4)")

    parser.add_argument("--list-variables", action="store_true", help="List available S3 variables")
    parser.add_argument("--list-tree", action="store_true", help="Show data tree for variable")

    parser.add_argument("--debug", action="store_true")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")

    args = parser.parse_args()

    setup_logging(debug=args.debug)
    signal.signal(signal.SIGINT, _cleanup_handler)
    signal.signal(signal.SIGTERM, _cleanup_handler)

    # 信息查询模式
    if args.list_variables:
        print("Fetching available variables from S3...")
        variables = discover_variables()
        print(f"\n  Found {len(variables)} variables:\n")
        for var in variables:
            conv = UNIT_CONVERSIONS.get(var)
            if conv:
                print(f"    {var:<8} {conv['name']} ({conv['from']} -> {conv['to']})")
            else:
                print(f"    {var:<8}")
        return 0

    if args.list_tree:
        if not args.variable:
            parser.error("--list-tree requires -v")
        for var in args.variable:
            list_s3_tree(var)
        return 0

    # 下载模式参数校验
    if not args.variable:
        parser.error("Specify -v variable (or --list-variables)")
    if not args.frequency:
        parser.error("Specify -f frequency")
    if not args.output:
        parser.error("Specify -o output path")

    variables = args.variable
    logger.info(f"ERA5 Downloader v{__version__} | vars={variables} freq={args.frequency}")

    # 验证变量存在
    available = discover_variables()
    missing = [v for v in variables if v not in available]
    if missing:
        logger.error(f"Variables not found: {missing}")
        logger.info("Use --list-variables to see available variables")
        return 1

    # 执行下载
    t_total_start = time.time()
    results = []
    ok_count = 0
    fail_count = 0

    if args.concurrent and len(variables) > 1:
        logger.info(f"Concurrent download: {len(variables)} variables")
        with ThreadPoolExecutor(max_workers=min(len(variables), 4)) as pool:
            futures = {pool.submit(download_one, var, args, available): var for var in variables}
            for future in as_completed(futures):
                var, ok, msg = future.result()
                results.append((var, ok, msg))
                if ok:
                    ok_count += 1
                    logger.info(f"  {var}: done -> {msg}")
                else:
                    fail_count += 1
                    logger.error(f"  {var}: failed -> {msg}")
    else:
        for var in variables:
            logger.info(f"\n{'=' * 50}")
            logger.info(f"Downloading: {var}")
            logger.info(f"{'=' * 50}")
            var, ok, msg = download_one(var, args, available)
            results.append((var, ok, msg))
            if ok:
                ok_count += 1
                logger.info(f"  {var}: done -> {msg}")
            else:
                fail_count += 1
                logger.error(f"  {var}: failed -> {msg}")

    # 汇总
    t_total_elapsed = time.time() - t_total_start
    eta_fmt = _format_eta_global(t_total_elapsed)
    print(f"\n{'=' * 50}")
    print(f"  Summary: {ok_count} ok | {fail_count} failed | Total: {eta_fmt}")
    for var, ok, msg in results:
        print(f"    {'OK' if ok else 'FAIL'} {var}: {msg}")
    print(f"{'=' * 50}")

    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
