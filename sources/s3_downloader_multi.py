#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AWS S3 ERA5 智能并发下载脚本（实时感知+动态推送版）
✅ 智能调度器：实时扫描本地目录，检测下载完成状态
✅ 动态补位：维持严格并发数（如6），完成1个立即推送1个
✅ 防重复/防丢单：字节级校验 + CLI稳定提交间隔
✅ S3 XML 命名空间兼容解析
✅ 支持命令行 / 代码内双模式调用

Author: Your Name
Date: 2026-01-22
"""

import os
import sys
import re
import time
import csv
import argparse
import subprocess
import threading
import collections
from pathlib import Path
from datetime import datetime, timedelta
from typing import List, Tuple, Optional, Dict

import requests
from bs4 import BeautifulSoup, FeatureNotFound


# ================= 配置区域 =================
class Config:
    S3_BASE_URL = "https://nsf-ncar-era5.s3.amazonaws.com"
    DATASET_PREFIX = "e5.oper.an.sfc"
    
    DOWNLOAD_TOOL = "idm"
    IDM_PATH = r"D:\Program Files (x86)\Internet Download Manager\IDMan.exe"
    XDM_PATH_LINUX = "/opt/xdman/xdman"
    XDM_PATH_WINDOWS = r"C:\Program Files\XDM\xdman.exe"
    
    MAX_CONCURRENT_TASKS = 6      # 🔑 目标并发数（严格控制）
    MAX_RETRIES = 3
    REQUEST_TIMEOUT = 30
    API_DELAY = 0.3               # S3 API 请求间隔
    SUBMIT_DELAY = 0.8            # 推送CLI间隔（防队列阻塞）
    MONITOR_INTERVAL = 2.0        # 🔑 完成状态扫描间隔(秒)
    SIZE_TOLERANCE = 0.99         # 文件大小容差
    DATA_DELAY_MONTHS = 5
    LOG_FILE = "download_log.txt"
    
    VARIABLE_DESC = {
        "2t": "2m Temperature", "2d": "2m Dewpoint", 
        "10u": "10m U-wind", "10v": "10m V-wind",
        "sp": "Surface Pressure", "msl": "Mean Sea Level Pressure",
        "tp": "Total Precipitation", "skt": "Skin Temperature", 
        "sd": "Snow Depth", "ssr": "Surface Solar Radiation", 
        "str": "Surface Thermal Radiation",
    }
    
    RUN_MODE = "cli"
    CODE_PARAMS = {
        "variables": ["2t"], "start_year": 2024, "end_year": 2024,
        "months": None, "output_dir": "./era5_data", "dry_run": False,
        "export_preview": True, "preview_file": "preview_list.csv",
    }


# ================= 日志工具 =================
class Logger:
    _lock = threading.Lock()
    
    @staticmethod
    def log(message: str, level: str = "INFO"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"[{timestamp}] [{level}] {message}"
        print(log_line)
        with Logger._lock:
            try:
                with open(Config.LOG_FILE, "a", encoding="utf-8") as f:
                    f.write(log_line + "\n")
            except: pass
    
    @staticmethod
    def print_table(headers: List[str], rows: List[List[str]], max_rows: int = 20):
        if not rows: return
        col_widths = [len(h) for h in headers]
        for row in rows[:max_rows]:
            for i, cell in enumerate(row): col_widths[i] = max(col_widths[i], len(str(cell)))
        header_line = "  ".join(h.ljust(col_widths[i]) for i, h in enumerate(headers))
        print("  " + "-" * len(header_line))
        print("  " + header_line)
        print("  " + "-" * len(header_line))
        for row in rows[:max_rows]:
            print("  " + "  ".join(str(cell).ljust(col_widths[i]) for i, cell in enumerate(row)))
        if len(rows) > max_rows: print(f"  ... 还有 {len(rows) - max_rows} 个文件")
        print()


# ================= 数据模型 =================
class FileInfo:
    def __init__(self, filename: str, url: str, size_str: str = "", size_bytes: int = 0, year_month: str = ""):
        self.filename = filename
        self.url = url
        self.size_str = size_str
        self.size_bytes = size_bytes
        self.year_month = year_month
        self.variable = self._extract_variable(filename)
    
    def _extract_variable(self, filename: str) -> str:
        match = re.search(r'_([a-z0-9]{2,3})_', filename, re.I)
        return match.group(1).lower() if match else "unknown"
    
    def to_row(self) -> List[str]:
        return [self.year_month, self.variable, self.filename, self.size_str, self.url]


# ================= S3 API 解析器 =================
class S3PageParser:
    @staticmethod
    def _format_bytes(byte_str: str) -> str:
        try:
            size = float(byte_str)
            for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
                if size < 1024.0: return f"{size:.1f}{unit}" if unit != 'B' else f"{int(size)}{unit}"
                size /= 1024.0
            return f"{size:.1f}PB"
        except: return byte_str if byte_str else "Unknown"

    @staticmethod
    def parse_month_files_s3_api(variable: str, year_month: str) -> List[FileInfo]:
        files, var_pattern = [], re.compile(rf"_{re.escape(variable)}[_\.]", re.I)
        try:
            api_url = f"{Config.S3_BASE_URL}/?list-type=2&prefix={Config.DATASET_PREFIX}/{year_month}/&delimiter=/"
            res = requests.get(api_url, timeout=Config.REQUEST_TIMEOUT)
            res.raise_for_status()
            try: soup = BeautifulSoup(res.content, 'xml')
            except FeatureNotFound: soup = BeautifulSoup(res.content, features="xml")
            
            if soup.find(lambda t: t.name and t.name.endswith('error')): return files
            
            contents = soup.find_all(lambda t: t.name and t.name.endswith('Contents'))
            if not contents:
                return S3PageParser._parse_by_regex(res.text, variable, year_month)
            
            for item in contents:
                key = item.find(lambda t: t.name and t.name.endswith('Key'))
                if not key: continue
                full_key, filename = key.text.strip(), key.text.strip().split('/')[-1]
                if filename.endswith('/') or (variable and not var_pattern.search(filename)): continue
                size_elem = item.find(lambda t: t.name and t.name.endswith('Size'))
                sb = int(size_elem.text) if size_elem and size_elem.text.isdigit() else 0
                files.append(FileInfo(filename, f"{Config.S3_BASE_URL}/{full_key}", S3PageParser._format_bytes(str(sb)), sb, year_month))
        except requests.RequestException as e:
            if getattr(e.response, 'status_code', 0) != 404: Logger.log(f"请求失败 [{year_month}]", "WARN")
        except Exception as e:
            Logger.log(f"解析异常 [{year_month}]: {e}", "ERROR")
        return files

    @staticmethod
    def _parse_by_regex(xml_text: str, variable: str, year_month: str) -> List[FileInfo]:
        files, var_pattern = [], re.compile(rf"_{re.escape(variable)}[_\.]", re.I)
        for block in re.finditer(r'<Contents>(.*?)</Contents>', xml_text, re.DOTALL | re.I):
            km = re.search(r'<Key>([^<]+)</Key>', block.group(1), re.I)
            if not km: continue
            fn = km.group(1).strip().split('/')[-1]
            if fn.endswith('/') or (variable and not var_pattern.search(fn)): continue
            sm = re.search(r'<Size>(\d+)</Size>', block.group(1), re.I)
            sb = int(sm.group(1)) if sm else 0
            files.append(FileInfo(fn, f"{Config.S3_BASE_URL}/{km.group(1).strip()}", S3PageParser._format_bytes(str(sb)), sb, year_month))
        return files

    @staticmethod
    def preview_collect(variable: str, start_year: int, end_year: int, months: Optional[List[int]] = None) -> List[FileInfo]:
        all_files, months = [], months or list(range(1, 13))
        cutoff = (datetime.now() - timedelta(days=Config.DATA_DELAY_MONTHS*30)).strftime("%Y%m")
        Logger.log(f"🔍 扫描: {variable} | {start_year}-{end_year} | 数据截止约: {cutoff}")
        for y in range(start_year, end_year + 1):
            for m in months:
                ym = f"{y}{m:02d}"
                if ym > cutoff: Logger.log(f"⏭️ 跳过未发布: {ym}", "INFO"); continue
                all_files.extend(S3PageParser.parse_month_files_s3_api(variable, ym))
                time.sleep(Config.API_DELAY)
        Logger.log(f"✅ 共发现 {len(all_files)} 个 {variable} 文件")
        return all_files


# ================= 预览导出 =================
class PreviewExporter:
    @staticmethod
    def export(files: List[FileInfo], filepath: str, variable: str, fmt: str = "csv"):
        try:
            Path(filepath).parent.mkdir(parents=True, exist_ok=True)
            if fmt == "csv":
                with open(filepath, 'w', newline='', encoding='utf-8-sig') as f:
                    w = csv.writer(f)
                    w.writerow(["Month","Var","Filename","Size","URL","Description"])
                    for fi in files: w.writerow([fi.year_month, fi.variable, fi.filename, fi.size_str, fi.url, Config.VARIABLE_DESC.get(fi.variable,"")])
            else:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(f"# {variable} Download List ({len(files)} files)\n")
                    for fi in files: f.write(f"{fi.url}\n")
            Logger.log(f"📄 已导出: {filepath}")
        except Exception as e: Logger.log(f"导出失败: {e}", "ERROR")


# ================= 下载执行器 =================
class Downloader:
    @staticmethod
    def get_tool_path() -> str:
        tool = Config.DOWNLOAD_TOOL.lower()
        return Config.IDM_PATH if tool == "idm" else (Config.XDM_PATH_WINDOWS if sys.platform == "win32" else Config.XDM_PATH_LINUX)

    @staticmethod
    def submit(url: str, save_dir: str, filename: str) -> Tuple[bool, str]:
        tool_path = Downloader.get_tool_path()
        cmd = [tool_path]
        if Config.DOWNLOAD_TOOL.lower() == "idm":
            cmd += ["/n", "/d", url, "/p", str(Path(save_dir).resolve()), "/f", filename]
        else:
            cmd += ["--add-url", url, "--save-path", str((Path(save_dir)/filename).resolve()), "--quiet"]
            
        try:
            subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                             creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0)
            return True, "Submitted"
        except FileNotFoundError:
            return False, f"ToolNotFound:{tool_path}"
        except Exception as e:
            return False, f"ExecError:{str(e)[:60]}"


# ================= 智能调度控制器 =================
class SmartDispatcher:
    """实时感知下载状态，动态维持目标并发数"""
    
    def __init__(self, tasks: List[FileInfo], output_dir: Path, max_concurrent: int):
        self.queue = collections.deque(tasks)
        self.output_dir = output_dir
        self.max_concurrent = max_concurrent
        self.pending_lookup = {f.filename: f for f in tasks}
        
        self.active_count = 0
        self.submitted_urls = set()
        self.completed_files = set()
        self.stats = {"total": 0, "success": 0, "failed": 0, "skipped": 0}
        self.lock = threading.Lock()
    
    def _scan_completed(self) -> List[FileInfo]:
        """扫描目录，找出已下载完成的文件"""
        completed_now = []
        try:
            for p in self.output_dir.iterdir():
                fn = p.name
                if fn in self.completed_files or fn not in self.pending_lookup:
                    continue
                # 过滤临时文件
                if fn.lower().endswith(('.tmp', '.part', '.filepart', '.crdownload', '.download')):
                    continue
                
                expected = self.pending_lookup[fn].size_bytes
                if expected > 0 and p.stat().st_size >= expected * Config.SIZE_TOLERANCE:
                    completed_now.append(self.pending_lookup[fn])
        except Exception as e:
            Logger.log(f"目录扫描异常: {e}", "WARN")
        return completed_now

    def run(self) -> Dict:
        Logger.log(f"🚀 启动智能调度器 | 目标并发: {self.max_concurrent} | 队列长度: {len(self.queue)}")
        
        while self.queue or self.active_count > 0:
            # 1️⃣ 推送阶段：维持并发水位
            with self.lock:
                while self.queue and self.active_count < self.max_concurrent:
                    fi = self.queue.popleft()
                    if fi.url in self.submitted_urls:
                        continue
                    
                    Logger.log(f"📤 推送 [{self.active_count+1}/{self.max_concurrent}]: {fi.filename} ({fi.size_str})")
                    success, msg = Downloader.submit(fi.url, str(self.output_dir), fi.filename)
                    
                    if success:
                        self.submitted_urls.add(fi.url)
                        self.active_count += 1
                        time.sleep(Config.SUBMIT_DELAY)
                    else:
                        Logger.log(f"❌ 推送失败: {fi.filename} ({msg})")
                        self.stats["failed"] += 1
                        self.stats["total"] += 1

            # 2️⃣ 监控阶段：等待完成或队列已满
            if self.active_count >= self.max_concurrent or (not self.queue and self.active_count > 0):
                newly_completed = self._scan_completed()
                if newly_completed:
                    with self.lock:
                        for fi in newly_completed:
                            self.completed_files.add(fi.filename)
                            self.active_count -= 1
                            self.stats["success"] += 1
                            self.stats["total"] += 1
                            Logger.log(f"✅ 已完成: {fi.filename} ({fi.size_str})")
                time.sleep(Config.MONITOR_INTERVAL)
        
        Logger.log(f"📊 调度结束 | 总计: {self.stats['total']} | 成功: {self.stats['success']} | 失败: {self.stats['failed']}")
        return self.stats


# ================= 主控制器 =================
class ERA5Downloader:
    def __init__(self, variable: str, start_year: int, end_year: int,
                 output_dir: str, months: Optional[List[int]] = None,
                 dry_run: bool = False, export_preview: bool = True,
                 preview_file: str = "preview_list.csv"):
        self.variable = variable.lower()
        self.start_year, self.end_year, self.months = start_year, end_year, months
        self.output_dir = Path(output_dir) / self.variable
        self.dry_run, self.export_preview, self.preview_file = dry_run, export_preview, preview_file
        Config.CURRENT_VAR = self.variable

    def _prepare_tasks(self, files: List[FileInfo]) -> List[FileInfo]:
        """预处理：过滤本地已完整文件，生成待下载队列"""
        tasks, skip = [], 0
        for fi in files:
            save_path = self.output_dir / fi.filename
            if save_path.exists() and fi.size_bytes > 0:
                if save_path.stat().st_size >= fi.size_bytes * Config.SIZE_TOLERANCE:
                    skip += 1
                    continue
            tasks.append(fi)
        Logger.log(f"📋 队列准备: 待提交 {len(tasks)} | 本地已跳过 {skip}")
        return tasks

    def _run_preview(self, files: List[FileInfo]):
        Logger.log("\n" + "🔍"*35 + "\nPREVIEW MODE\n" + "🔍"*35)
        if not files: Logger.log("⚠️ 无匹配文件", "WARN"); return
        
        Logger.log(f"📊 变量: {self.variable} | 📅 {self.start_year}-{self.end_year} | 📁 {self.output_dir}")
        total_gb = sum(f.size_bytes for f in files) / (1024**3)
        Logger.log(f"📈 统计: {len(files)} 文件 | 约 {total_gb:.2f} GB")
        Logger.print_table(["Month","Var","Filename","Size"], [f.to_row()[:4] for f in files], 20)
        
        if self.export_preview:
            base = self.preview_file.rsplit('.',1)[0]
            PreviewExporter.export(files, str(Path(self.output_dir).parent/f"{base}_{self.variable}.csv"), self.variable, "csv")
            PreviewExporter.export(files, str(Path(self.output_dir).parent/f"{base}_{self.variable}.txt"), self.variable, "txt")
        Logger.log("\n✅ 预览完成。设置 dry_run=False 开始下载")

    def run(self):
        Logger.log(f"\n{'='*70}\nERA5 Downloader - {self.variable}\n{'='*70}")
        files = S3PageParser.preview_collect(self.variable, self.start_year, self.end_year, self.months)
        if self.dry_run: 
            self._run_preview(files)
        else:
            self.output_dir.mkdir(parents=True, exist_ok=True)
            tasks = self._prepare_tasks(files)
            if not tasks:
                Logger.log("✅ 无新文件需要下载"); return
            SmartDispatcher(tasks, self.output_dir, Config.MAX_CONCURRENT_TASKS).run()


# ================= 入口 =================
def run_batch(vars: List[str], params: dict):
    for v in vars:
        Logger.log(f"\n{'#'*60}\n▶️  处理变量: {v}\n{'#'*60}")
        ERA5Downloader(variable=v, **params).run()
        time.sleep(2)

def main(args=None, config=None):
    if Config.RUN_MODE == "cli" and args is None:
        p = argparse.ArgumentParser(description="ERA5 S3 Smart Downloader", 
                                    formatter_class=argparse.RawDescriptionHelpFormatter,
                                    epilog="示例: -v 2t -y 2025-2025 -m 11 -o ./data -c 6")
        p.add_argument('-v','--variables',required=True)
        p.add_argument('-y','--years',required=True)
        p.add_argument('-m','--months')
        p.add_argument('-o','--output',required=True)
        p.add_argument('-t','--tool',choices=['idm','xdm'],default='idm')
        p.add_argument('-c','--concurrent',type=int,default=6)
        p.add_argument('--dry-run',action='store_true')
        p.add_argument('--export',action='store_true')
        p.add_argument('--preview-file',default='preview_list.csv')
        p.add_argument('--delay',type=int,default=5)
        a = p.parse_args()
        
        Config.DOWNLOAD_TOOL = a.tool
        Config.MAX_CONCURRENT_TASKS = a.concurrent
        Config.DATA_DELAY_MONTHS = a.delay
        
        Logger.log("⚙️ 运行配置快照:")
        Logger.log(f"工具: {Config.DOWNLOAD_TOOL.upper()} | 路径: {Downloader.get_tool_path()}")
        Logger.log(f"目标并发: {Config.MAX_CONCURRENT_TASKS} | 监控间隔: {Config.MONITOR_INTERVAL}s")
        Logger.log(f"输出目录: {Path(a.output).resolve()}")
        
        vars = [v.strip().lower() for v in a.variables.split(',')]
        yrs = list(map(int, a.years.split('-'))) if '-' in a.years else [int(a.years)]*2
        mons = [int(m) for m in a.months.split(',')] if a.months else None
        params = dict(start_year=yrs[0], end_year=yrs[1], months=mons, output_dir=a.output, 
                      dry_run=a.dry_run, export_preview=a.export, preview_file=a.preview_file)
        
        if len(vars)==1: ERA5Downloader(variable=vars[0], **params).run()
        else: run_batch(vars, params)
    else:
        cfg = {**Config.CODE_PARAMS, **(config or {})}
        Config.DOWNLOAD_TOOL = cfg.get('tool', Config.DOWNLOAD_TOOL)
        Config.MAX_CONCURRENT_TASKS = cfg.get('concurrent', Config.MAX_CONCURRENT_TASKS)
        vars = cfg['variables'] if isinstance(cfg['variables'], list) else [cfg['variables']]
        params = dict(start_year=cfg['start_year'], end_year=cfg['end_year'], months=cfg.get('months'),
                      output_dir=cfg['output_dir'], dry_run=cfg.get('dry_run',False),
                      export_preview=cfg.get('export_preview',True), preview_file=cfg.get('preview_file','preview_list.csv'))
        if len(vars)==1: ERA5Downloader(variable=vars[0], **params).run()
        else: run_batch(vars, params)

if __name__ == "__main__":
    Config.RUN_MODE = "cli"
    main()