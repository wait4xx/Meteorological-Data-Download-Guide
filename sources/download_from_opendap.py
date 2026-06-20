#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generic OPeNDAP subset downloader.

说明:
    OPeNDAP 协议本身仍可通过 xarray 使用，但 NOAA NOMADS GFS OPeNDAP
    已经退役。请传入仍可用的具体 OPeNDAP 数据集 URL，不要传目录页。

示例:
    python sources/download_from_opendap.py \\
        --url "https://example.opendap.org/dataset" \\
        -v tmp2m \\
        --time-range 2024-01-01 2024-01-02 \\
        --region 100 120 20 40 \\
        -o subset.nc

依赖:
    pip install xarray netCDF4
"""

from __future__ import annotations

import argparse
import sys
import urllib.error
import urllib.request
import warnings
from pathlib import Path
from typing import Iterable

import xarray as xr


RETIRED_MARKERS = [
    "opendap format has been retired",
    "request for opendap data",
    "service change notice",
]


def _metadata_url(url: str) -> str:
    clean = url.rstrip("/")
    if clean.endswith((".dds", ".das", ".html")):
        return clean
    return clean + ".dds"


def check_opendap_url(url: str, timeout: int = 20) -> tuple[bool, str]:
    """Return whether URL looks like a real OPeNDAP dataset."""
    probe_url = _metadata_url(url)
    try:
        content_type, text = _read_probe(probe_url, timeout)
    except urllib.error.HTTPError as exc:
        if 300 <= exc.code < 500:
            try:
                content_type, text = _read_probe(url, timeout)
                html_result = _check_html_response(content_type, text)
                if html_result:
                    return False, html_result
            except Exception:
                pass
        if 300 <= exc.code < 400:
            return False, f"HTTP {exc.code} while fetching DDS metadata; endpoint is redirected and not usable as OPeNDAP"
        return False, f"HTTP {exc.code}: {probe_url}"
    except urllib.error.URLError as exc:
        return False, f"URL error: {exc.reason}"

    html_result = _check_html_response(content_type, text)
    if html_result:
        return False, html_result
    if "dataset" in text or "dimensions" in text:
        return True, "OPeNDAP metadata detected"
    return False, "response does not look like OPeNDAP DDS metadata"


def _read_probe(url: str, timeout: int) -> tuple[str, str]:
    req = urllib.request.Request(url, headers={"User-Agent": "meteo-opendap-check/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        content_type = resp.headers.get("content-type", "").lower()
        text = resp.read(4096).decode("utf-8", "ignore").lower()
    return content_type, text


def _check_html_response(content_type: str, text: str) -> str | None:
    if "text/html" not in content_type and not text.lstrip().startswith(("<!doctype html", "<html")):
        return None
    for marker in RETIRED_MARKERS:
        if marker in text:
            return "server returned NOAA retirement/error HTML; this OPeNDAP endpoint is not usable"
    return "server returned HTML instead of OPeNDAP DDS metadata; pass a concrete dataset URL"


def subset_dataset(
    ds: xr.Dataset,
    variables: list[str] | None = None,
    time_range: tuple[str, str] | None = None,
    region: tuple[float, float, float, float] | None = None,
) -> xr.Dataset:
    if variables:
        missing = [name for name in variables if name not in ds.variables]
        if missing:
            available = ", ".join(list(ds.variables)[:30])
            raise KeyError(f"variables not found: {missing}. Available examples: {available}")
        ds = ds[variables]

    if time_range:
        if "time" in ds.coords:
            ds = ds.sel(time=slice(time_range[0], time_range[1]))
        else:
            candidates = [c for c in ds.coords if "time" in c.lower()]
            warnings.warn(
                f"time_range requested but no 'time' coordinate found. "
                f"Time filtering skipped. "
                f"Available time-like coords: {candidates or list(ds.coords)}",
                stacklevel=2,
            )

    if region:
        lon_min, lon_max, lat_min, lat_max = region
        lon_name = _first_existing(ds.coords, ["lon", "longitude", "x"])
        lat_name = _first_existing(ds.coords, ["lat", "latitude", "y"])
        if not lon_name or not lat_name:
            available = list(ds.coords)
            missing = "longitude" if not lon_name else ""
            missing += (" and " if not lon_name and not lat_name else "") + ("latitude" if not lat_name else "")
            warnings.warn(
                f"region requested but {missing} coordinate(s) not found. "
                f"Spatial filtering skipped. Available coords: {available}",
                stacklevel=2,
            )
        if lon_name:
            ds = ds.sel({lon_name: slice(lon_min, lon_max)})
        if lat_name:
            values = ds[lat_name].values
            if len(values) >= 2 and values[0] > values[-1]:
                ds = ds.sel({lat_name: slice(lat_max, lat_min)})
            else:
                ds = ds.sel({lat_name: slice(lat_min, lat_max)})
    return ds


def _first_existing(keys: Iterable[str], candidates: list[str]) -> str | None:
    for name in candidates:
        if name in keys:
            return name
    return None


def clear_encoding(ds: xr.Dataset) -> None:
    for name in ds.variables:
        ds[name].encoding = {}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Download a subset from a concrete OPeNDAP dataset URL.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--url", required=True, help="Concrete OPeNDAP dataset URL, not a directory page")
    parser.add_argument("-v", "--variables", nargs="+", help="Variables to export")
    parser.add_argument("--time-range", nargs=2, metavar=("START", "END"), help="Time range")
    parser.add_argument(
        "--region",
        nargs=4,
        type=float,
        metavar=("LON_MIN", "LON_MAX", "LAT_MIN", "LAT_MAX"),
        help="Spatial region",
    )
    parser.add_argument("-o", "--output", default="opendap_subset.nc", help="Output NetCDF path")
    parser.add_argument("--list", action="store_true", help="Only list dataset metadata and variables")
    parser.add_argument("--skip-check", action="store_true", help="Skip .dds metadata preflight check")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if not args.skip_check:
        ok, message = check_opendap_url(args.url)
        print(f"preflight: {message}")
        if not ok:
            return 2

    ds = None
    try:
        print(f"opening: {args.url}")
        ds = xr.open_dataset(args.url)
        print(ds)

        if args.list:
            print("\nvariables:")
            for name, data in ds.data_vars.items():
                dims = "x".join(str(ds.sizes[d]) for d in data.dims)
                units = data.attrs.get("units", "")
                print(f"  {name:<24} dims={data.dims} size={dims} units={units}")
            return 0

        subset = subset_dataset(
            ds,
            variables=args.variables,
            time_range=tuple(args.time_range) if args.time_range else None,
            region=tuple(args.region) if args.region else None,
        )
        clear_encoding(subset)
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        print(f"selected dims: {dict(subset.sizes)}")
        print(f"writing: {output}")
        subset.load().to_netcdf(output)
        print(f"done: {output}")
        return 0
    except Exception as exc:
        print(f"failed: {exc}", file=sys.stderr)
        return 1
    finally:
        if ds is not None:
            ds.close()


if __name__ == "__main__":
    raise SystemExit(main())
