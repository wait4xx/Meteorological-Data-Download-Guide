# 🌤️ 公开气象数据下载资源库（完善中...）

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![GitHub Stars](https://img.shields.io/github/stars/wait4xx/Meteorological-Data-Download-Guide.svg)](https://github.com/wait4xx/Meteorological-Data-Download-Guide)

一个收集整理各类公开气象数据下载网址的资源库，旨在为气象研究、数据分析和应用开发提供便捷的数据获取渠道。

---

### 📅 2025 年 12 月 5 日更新内容

- ✅ **新增功能**：上传了 [ECMWF Open Data](https://data.ecmwf.int/forecasts/) **实时 IFS 预报数据下载脚本**  
  - 默认使用 **4 线程并行下载**，提升效率  
  - ⚠️ 注意：请求频率过高或过多可能导致连接被拒绝（建议合理控制请求速率）

---

### 🔧 项目进展

#### ✅ 已完成

- 数值预报数据  
- 大模型预报数据  
- 再分析数据  

#### 🚧 待完成

- 实时观测数据  
- 卫星数据  
- 雷达数据  
- 气候数据  
- 海洋气象数据  
- 空气质量数据  
- 开源代码与工具集成

---

## 📚 目录

- [数值预报数据](#数值预报数据)
- [大模型预报数据](#大模型预报数据)
- [实况观测数据](#实况观测数据)
- [卫星数据](#卫星数据)
- [雷达数据](#雷达数据)
- [气候与再分析数据](#气候与再分析数据)
- [海洋气象数据](#海洋气象数据)
- [空气质量数据](#空气质量数据)
- [开源代码与工具](#开源代码与工具)
- [贡献指南](#贡献指南)
- [许可证](#许可证)
- [致谢](#致谢)

## 数值预报数据

### 实时预报数据

| 数据源 | 描述 | 子产品 / 配置 | 预报方法 | 分辨率 | 时效 | 更新频率 | 访问方式 | 时间范围 | 备注 |
|--------|------|----------------|----------|--------|------|----------|----------|----------|------|
| **ECMWF** | 欧洲中期天气预报中心 | **IFS** | 确定性预报 | 0.25° | 0–144h (3h)<br>144–360h (6h) | 每日 4 次 | [ECMWF Open Data](https://data.ecmwf.int/forecasts/) | 最近 4 日 | |
| | | **EFS** | 集合预报 | 0.25° | 0–144h (3h)<br>144–360h (6h) | 每日 4 次 | [ECMWF Open Data](https://data.ecmwf.int/forecasts/) | 最近 4 日 | |
| **NCEP** | 美国全球预报系统 | **GFS** | 确定性预报 | 0.25° / 0.5° | 0–144h (3h)<br>144–360h (6h) | 每日 4 次 | [GFS_UCAR](https://motherlode.ucar.edu/native/grid/NCEP/GFS/) | 最近 3 个月 | |
| | | **GFS** | 确定性预报 | 0.25° | 0–120h (1h) | 每日 4 次 | [GFS_OpeNDAP (1h)](https://nomads.ncep.noaa.gov/dods/gfs_0p25_1hr/) | 最近 10 日 | [Python/xarray 示例](./sources/download_from_opendap.py) |
| | | **GFS** | 确定性预报 | 0.25° | 0–384h (3h) | 每日 4 次 | [GFS_OpeNDAP (0.25°)](https://nomads.ncep.noaa.gov/dods/gfs_0p25//) | 最近 10 日 | [Python/xarray 示例](./sources/download_from_opendap.py) |
| | | **GFS** | 确定性预报 | 0.25° | 0–120h (1h)<br>120–384h (3h) | 每日 4 次 | [GFS_NOAA](https://nomads.ncep.noaa.gov/pub/data/nccf/com/gfs/) | 最近 10 日 | |
| | | **GFS** | 确定性预报 | 0.5° | 0–384h (3h) | 每日 4 次 | [GFS_OpeNDAP (0.5°)](https://nomads.ncep.noaa.gov/dods/gfs_0p50/) | 最近 10 日 | [Python/xarray 示例](./sources/download_from_opendap.py) |
| | | **GFS** | 确定性预报 | 1° | 0–384h (3h) | 每日 4 次 | [GFS_OpeNDAP (1°)](https://nomads.ncep.noaa.gov/dods/gfs_1p00/) | 最近 10 日 | [Python/xarray 示例](./sources/download_from_opendap.py) |
| | | **GEFS** | 集合预报 | 0.25° | 0–240h (3h) | 每日 4 次 | [GEFS_NOAA](https://nomads.ncep.noaa.gov/pub/data/nccf/com/gens/) | 最近 4 日 | |
| | | **GEFS** | 集合预报 | 0.5° | 0–240h (3h)<br>240–840h (6h) | 每日 4 次 | [GEFS_NOAA](https://nomads.ncep.noaa.gov/pub/data/nccf/com/gens/) | 最近 4 日 | |
| **DWD** | 德国天气局 | **ICON** | 确定性预报 | 0.125° | 0–144h (3h)<br>144–360h (6h) | 每日 4 次 | [ICON Open Data](https://opendata.dwd.de/weather/nwp/icon/grib/) | 最近 4 个起报 | |
| **JMA** | 日本气象厅 | **GSM** | 确定性预报 | 0.25° / 0.5° | 0–144h (3h)<br>144–360h (6h) | 每日 4 次 | [JMA GSM](https://www.wis-jma.go.jp/cms/gsm/download.html) | 最近 5 日 | |

> [ECMWF Free & Open Data Portal](https://data.ecmwf.int/forecasts/) —— ECMWF 公开数据说明  
> 包含 IFS 及 AIFS，其中 IFS 数据格式说明如下：  
> ![ec_file](./pics/ec_file.png)

### 历史预报数据

| 主数据源 | 描述 | 子产品 / 配置 | 预报方法 | 分辨率 | 时效 | 更新频率 | 访问方式 | 时间范围 | 备注 |
|----------|------|----------------|----------|--------|------|----------|----------|----------|------|
| **ECMWF** | 欧洲中期天气预报中心 | **IFS (HRES ~ 地面)** | 确定性预报 | 0.1° | 0–12h (6h) | 每日 4 次 | [IFS_UCAR](https://gdex.ucar.edu/datasets/d113001/dataaccess/#) | 2016 年 1 月 1 日至今 | |
| | | **IFS** | 确定性预报 | 0.25° / 0.4° | 0–144h (3h)<br>144–360h (6h) | 每日 4 次 | [🪜 ECMWF_GOOGLE](https://console.cloud.google.com/storage/browser/ecmwf-open-data) | 2023 年 7 月 12 日至今（有延迟） | |
| | | **IFS** | 确定性预报 | 0.25° / 0.4° | 0–144h (3h)<br>144–360h (6h) | 每日 4 次 | [AWS-S3](https://ecmwf-forecasts.s3.amazonaws.com/) | 2023 年 3 月 18 日至今 | 需 awscli 或补全 URL 下载 |
| | | **EFS** | 集合预报 | 0.25° / 0.4° | 0–144h (3h)<br>144–360h (6h) | 每日 4 次 | [🪜 ECMWF_GOOGLE](https://console.cloud.google.com/storage/browser/ecmwf-open-data) | 2023 年 7 月 12 日至今（有延迟） | |
| | | **EFS** | 集合预报 | 0.25° / 0.4° | 0–144h (3h)<br>144–360h (6h) | 每日 4 次 | [AWS-S3](https://ecmwf-forecasts.s3.amazonaws.com/) | 2023 年 3 月 18 日至今 | 需 awscli 或补全 URL 下载 |
| **NCEP** | 美国全球预报系统 | **GFS** | 确定性预报 | 0.25° / 0.5° | 0–240h (3h)<br>240–384h (12h) | 每日 4 次 | [GFS_UCAR](https://gdex.ucar.edu/datasets/d084001/dataaccess/) | 2015 年 1 月 15 日至今（2026 年停更）| |
| | | **GFS** | 确定性预报 | 0.25° / 0.5° / 1° | 0–384h (3h) | 每日 4 次 | [AWS-S3](https://noaa-gfs-bdp-pds.s3.amazonaws.com/index.html) | 2021 年 1 月 1 日至今 | 搜索 `gfs` |
| | | **GFS** | 确定性预报 | 0.25° / 0.5° / 1° | 0–384h (3h) | 每日 4 次 | [🪜 GFS_GOOGLE](https://console.cloud.google.com/storage/browser/global-forecast-system) | 2021 年 1 月 1 日至今 | 搜索 `gfs` |
| | | **GEFS** | 集合预报 | 0.25° / 0.5° | 0–384h (6h) / 0–240h (3h) | 每日 4 次 | [AWS-S3](https://noaa-gefs-pds.s3.amazonaws.com/index.html) | 2017 年 1 月 1 日至今 | |
| | | **GEFS** | 集合预报 | 0.25° / 0.5° | 0–240h (3h) | 每日 4 次 | [🪜 GFS_GOOGLE](https://console.cloud.google.com/storage/browser/gfs-ensemble-forecast-system) | 2020 年 9 月 25 日至今 | |

## 大模型预报数据

### 实时数据

| 数据源 | 描述 | 预报方法 | 分辨率 | 时效 | 更新频率 | 访问方式 | 时间范围 | 备注 |
|--------|------|----------|--------|------|----------|----------|----------|------|
| **ECMWF-AIFS** | 欧洲中期天气预报中心 | 确定性预报 | 0.25° | 0–360h (6h) | 每日 4 次 | [ECMWF Open Data](https://data.ecmwf.int/forecasts/) | 最近 4 日 | |
| **ECMWF-AIEFS** | 欧洲中期天气预报中心 | 集合预报 | 0.25° | 0–360h (6h) | 每日 4 次 | [ECMWF Open Data](https://data.ecmwf.int/forecasts/) | 最近 4 日 | |
| **NCEP-AIGFS** | 美国全球预报系统 | 确定性预报 | 0.25° / 0.5° | 0–360h (6h) | 每日 4 次 | [AIGFS_NOAA](https://nomads.ncep.noaa.gov/pub/data/nccf/com/aigfs/) | 最近 2 日 | |
| **NCEP-AIGEFS** | 美国全球预报系统 | 集合预报 | 0.25° / 0.5° | 0–360h (6h) | 每日 4 次 | [AIGEFS_NOAA](https://nomads.ncep.noaa.gov/pub/data/nccf/com/aigefs/) | 最近 2 日 | |
| **Aurora** | 微软 | 确定性预报 | 0.5° | 0–240h (6h) | 每日 2 次 | [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) | — | [数据说明](./docs/noaa-oar-mlwp-data.txt) |
| **FourCastNet** | NVIDIA | 确定性预报 | 0.5° | 0–240h (6h) | 每日 2 次 | [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) | — | [数据说明](./docs/noaa-oar-mlwp-data.txt) |
| **GraphCast** | Google / DeepMind | 确定性预报 | 0.5° | 0–240h (6h) | 每日 2 次 | [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) | — | [数据说明](./docs/noaa-oar-mlwp-data.txt) |
| **PANGU** | 华为 | 确定性预报 | 0.5° | 0–240h (6h) | 每日 2 次 | [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) | — | [数据说明](./docs/noaa-oar-mlwp-data.txt) |

### 历史数据

| 数据源 | 描述 | 预报方法 | 分辨率 | 时效 | 更新频率 | 访问方式 | 时间范围 | 备注 |
|--------|------|----------|--------|------|----------|----------|----------|------|
| **ECMWF-AIFS** | 欧洲中期天气预报中心 | 确定性预报 | 0.25° | 0–360h (6h) | 每日 4 次 | [AWS-S3](https://ecmwf-forecasts.s3.amazonaws.com/) | 2024 年 2 月 29 日至今 | 需 awscli 或补全 URL |
| **ECMWF-AIEFS** | 欧洲中期天气预报中心 | 集合预报 | 0.25° | 0–360h (6h) | 每日 4 次 | [AWS-S3](https://ecmwf-forecasts.s3.amazonaws.com/) | — | 需 awscli 或补全 URL |
| **Aurora** | 微软 | 确定性预报 | 0.5° | 0–240h (6h) | 每日 2 次 | [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) | 2025 年 1 月 23 日至今 | [数据说明](./docs/noaa-oar-mlwp-data.txt) |
| **FourCastNet** | NVIDIA | 确定性预报 | 0.5° | 0–240h (6h) | 每日 2 次 | [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) | 2020 年 9 月 30 日至今 | [数据说明](./docs/noaa-oar-mlwp-data.txt) |
| **GraphCast** | Google / DeepMind | 确定性预报 | 0.5° | 0–240h (6h) | 每日 2 次 | [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) | 2020 年 9 月 30 日至今 | [数据说明](./docs/noaa-oar-mlwp-data.txt) |
| **PANGU** | 华为 | 确定性预报 | 0.5° | 0–240h (6h) | 每日 2 次 | [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) | 2020 年 9 月 30 日至今 | [数据说明](./docs/noaa-oar-mlwp-data.txt) |

## 实况观测数据

### 地面观测

| 数据源 | 覆盖范围 | 要素 | 更新频率 | 访问方式 | 备注 |
|--------|----------|------|----------|----------|------|
| **ASOS/AWOS** | 全球机场 | 多要素 | 实时 | [NOAA](https://www.ncei.noaa.gov/maps/hourly/) | |
| **SYNOP** | 全球 | 基本气象要素 | 3/6 小时 | [OGIMET](https://www.ogimet.com/) | |
| **MADIS** | 北美 | 多源数据 | 实时 | [NOAA MADIS](https://madis.ncep.noaa.gov/) | |

### 高空观测

| 数据源 | 覆盖范围 | 层次 | 更新频率 | 访问方式 | 备注 |
|--------|----------|------|----------|----------|------|
| **IGRA** | 全球 | 标准层 | 每日 2 次 | [NOAA IGRA](https://www.ncei.noaa.gov/access/weather/igra/) | |
| **AMDAR** | 全球航线 | 飞行层 | 实时 | [WMO AMDAR](https://amdar.wmo.int/) | |

### 自动气象站

| 数据源 | 网络规模 | 区域 | 访问方式 | 备注 |
|--------|----------|------|----------|------|
| **MesoWest** | 数千站 | 美国 | [MesoWest](https://mesowest.utah.edu/) | |
| **Weather Underground** | 全球个人站 | 全球 | [WUnderground](https://www.wunderground.com/) | |

## 卫星数据

### 地球同步卫星

| 卫星 | 机构 | 覆盖区域 | 主要产品 | 数据访问 | 备注 |
|------|------|----------|----------|----------|------|
| **Himawari-8/9** | JMA | 亚太 | 云图、气溶胶 | [JAXA](https://www.eorc.jaxa.jp/ptree/) | |
| **GOES-16/18** | NOAA | 美洲 | 多通道图像 | [NOAA GOES](https://www.noaa.gov/goes-16-and-goes-17-satellite-data) | |
| **FY-4A/4B** | CMA | 亚洲 | 云图、降水 | [NSMC](http://satellite.nsmc.org.cn/) | |

### 极轨卫星

| 卫星 | 机构 | 分辨率 | 主要产品 | 数据访问 | 备注 |
|------|------|--------|----------|----------|------|
| **Suomi NPP** | NASA/NOAA | 750m | VIIRS 数据 | [NASA LAADS](https://ladsweb.modaps.eosdis.nasa.gov/) | |
| **JPSS** | NOAA | 375m | 多光谱数据 | [NOAA CLASS](https://www.avl.class.noaa.gov/) | |
| **Sentinel-3** | ESA | 300m | 海洋颜色 | [Copernicus](https://scihub.copernicus.eu/) | |

### 卫星降水产品

| 产品 | 空间分辨率 | 时间分辨率 | 覆盖范围 | 访问方式 | 备注 |
|------|------------|------------|----------|----------|------|
| **GPM IMERG** | 0.1° | 30 分钟 | 全球 | [NASA GES DISC](https://disc.gsfc.nasa.gov/) | |
| **CMORPH** | 0.25° | 30 分钟 | 全球 | [CPC](https://www.cpc.ncep.noaa.gov/products/janowiak/cmorph_description.html) | |

## 雷达数据

### 天气雷达

| 网络 | 覆盖区域 | 产品类型 | 访问方式 | 备注 |
|------|----------|----------|----------|------|
| **NEXRAD** | 美国 | 基数据、产品 | [NOAA NCEI](https://www.ncdc.noaa.gov/nexradinv/) | |
| **OPERA** | 欧洲 | 合成产品 | [EUMETNET](https://www.eumetnet.eu/activities/observations-programme/current-activities/opera/) | |

## 气候与再分析数据

### 再分析数据集

| 数据源 | 描述 | 空间分辨率 | 时间分辨率 | 访问方式 | 时间范围 | 备注 |
|--------|------|------------|------------|----------|----------|------|
| **ERA5-land** | ECMWF | 0.25° | hourly | [ERA5-land](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-land?tab=download) | 1950 年 1 月 1 日至今 | |
| **ERA5-land** | ECMWF | 0.25° | monthly-mean | [ERA5-land (monthly)](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-land-monthly-means?tab=download) | 1950 年 1 月 1 日至今 | |
| **ERA5-land** | ECMWF | 0.25° | hourly | [AWS-S3](https://nsf-ncar-era5.s3.amazonaws.com/index.html#e5.oper.an.sfc/) | 1940 年 1 月 1 日至今 | |
| **ERA5-pressure** | ECMWF | 0.25° | hourly | [ERA5-pressure](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-pressure-levels?tab=download) | 1940 年 1 月 1 日至今 | |
| **ERA5-pressure** | ECMWF | 0.25° | monthly-mean | [ERA5-pressure (monthly)](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-pressure-levels-monthly-means?tab=download) | 1940 年 1 月 1 日至今 | |
| **ERA5-pressure** | ECMWF | 0.25° | hourly | [AWS-S3](https://nsf-ncar-era5.s3.amazonaws.com/index.html#e5.oper.an.pl/) | 1940 年 1 月 1 日至今 | |
| **ERA5** | ECMWF | 0.25° | hourly / monthly | [🪜 ERA5_GOOGLE](https://console.cloud.google.com/storage/browser/gcp-public-data-arco-era5/raw/ERA5GRIB/HRES) | 1940 年 1 月 1 日至今 | |
| **FNL** | NCEP | 0.25° | 6-hourly | [FNL_UCAR (0.25°)](https://gdex.ucar.edu/datasets/d083003/dataaccess/#) | 2015 年 7 月 8 日至今 | |
| **FNL** | NCEP | 1° | 6-hourly | [FNL_UCAR (1°)](https://gdex.ucar.edu/datasets/d083002/dataaccess/#) | 1999 年 7 月 30 日至今 | |
| **JRA-3Q** | JMA | 1.25° | hourly / monthly-mean | [JRA-3Q_DIAS](https://data.diasjp.net/dl/storages/filelist/dataset:645) | 1947 年 9 月 1 日至今 | 需登录 |
| **JRA-3Q** | JMA | 1.25° | hourly | [JRA-3Q_UCAR (historical)](https://gdex.ucar.edu/datasets/d640000/dataaccess/#) | 1947 年 9 月 1 日至今 | |
| **JRA-3Q** | JMA | 1.25° | hourly | [JRA-3Q_UCAR (near-real)](https://gdex.ucar.edu/datasets/d640001/dataaccess/#) | 2023 年 12 月 9 日至今 | 近实时 |
| **JRA-3Q** | JMA | 1.25° | monthly-mean | [JRA-3Q_UCAR (monthly)](https://gdex.ucar.edu/datasets/d640002/dataaccess/#) | 1947 年 9 月 1 日至今 | |
| **JRA-3Q** | JMA | 1.25° | monthly-mean | [JRA-3Q_UCAR (near-real)](https://gdex.ucar.edu/datasets/d640003/dataaccess/#) | 1991 年 1 月 1 日至今 | 近实时 |
| **MERRA-2** | NASA | 0.5° | hourly / monthly | [MERRA_GSFC](https://disc.gsfc.nasa.gov/datasets?project=MERRA-2) | 1980 年 1 月 1 日至今 | |
| **MERRA-2** | NASA | 0.5° | hourly / monthly | [MERRA_FTP](https://goldsmr4.gesdisc.eosdis.nasa.gov/data/) | 1980 年 1 月 1 日至今 | |

### 气候数据集

| 数据集 | 类型 | 分辨率 | 时段 | 访问方式 | 备注 |
|--------|------|--------|------|----------|------|
| **CRU TS** | 格点化观测 | 0.5° | 1901–现在 | [UEA](https://crudata.uea.ac.uk/cru/data/hrg/) | |
| **GPCC** | 降水 | 0.25°–2.5° | 1891–现在 | [DWD](https://www.dwd.de/EN/ourservices/gpcc/gpcc.html) | |

## 海洋气象数据

### 海洋观测

| 数据源 | 观测平台 | 要素 | 访问方式 | 备注 |
|--------|----------|------|----------|------|
| **Argo** | 剖面浮标 | 温盐深 | [Argo GDAC](https://argo.ucsd.edu/data/argo-data/) | |
| **TAO/TRITON** | 锚定浮标 | 海洋气象 | [PMEL](https://www.pmel.noaa.gov/tao/) | |

### 海洋模式

| 模式 | 机构 | 分辨率 | 产品 | 访问方式 | 备注 |
|------|------|--------|------|----------|------|
| **HYCOM** | 美国海军 | 1/12° | 海洋分析预报 | [HYCOM](https://www.hycom.org/) | |
| **CMEMS** | 欧盟 | 多种 | 海洋监测预报 | [Copernicus Marine](https://marine.copernicus.eu/) | |

## 空气质量数据

### 空气质量监测

| 数据源 | 覆盖范围 | 污染物 | 访问方式 | 备注 |
|--------|----------|--------|----------|------|
| **AirNow** | 美国 | 主要污染物 | [AirNow](https://www.airnow.gov/) | |
| **OpenAQ** | 全球 | 多种污染物 | [OpenAQ](https://openaq.org/) | |

### 空气质量模式

| 模式 | 机构 | 分辨率 | 产品 | 访问方式 | 备注 |
|------|------|--------|------|----------|------|
| **CAMS** | ECMWF | 0.4° | 全球空气质量预报 | [CAMS](https://atmosphere.copernicus.eu/) | |

## 开源代码与工具

### 数据下载与处理

| 工具 | 语言 | 功能 | 链接 | 备注 |
|------|------|------|------|------|
| **Herbie** | Python | GFS/HRRR 数据下载 | [GitHub](https://github.com/blaylockbk/Herbie) | |
| **Siphon** | Python | 远程数据访问 | [Unidata](https://github.com/Unidata/siphon) | |
| **cfgrib** | Python | GRIB 文件处理 | [ECMWF](https://github.com/ecmwf/cfgrib) | |

### 可视化与分析

| 工具 | 语言 | 功能 | 链接 | 备注 |
|------|------|------|------|------|
| **MetPy** | Python | 气象数据分析可视化 | [Unidata](https://github.com/Unidata/MetPy) | |
| **Cartopy** | Python | 地图制图 | [SciTools](https://github.com/SciTools/cartopy) | |

## 贡献指南

我们欢迎并感谢所有形式的贡献！请参阅 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详细的贡献指南。

### 如何贡献

1. **报告问题**：通过 [Issues](https://github.com/wait4xx/Meteorological-Data-Download-Guide/issues) 报告错误或建议新功能  
2. **添加资源**：提交 Pull Request 添加新的气象数据资源  
3. **改进文档**：帮助改进文档或翻译内容  
4. **分享用例**：在 Discussions 中分享你的数据使用案例  

### 提交规范

- 确保链接有效且可公开访问  
- 提供清晰的数据描述和访问方式  
- 遵循现有的分类和格式  
- 注明数据许可和使用限制  

## 许可证

**重要提示**：本资源库中列出的数据源可能有各自的使用条款和许可协议。在使用任何数据前，请务必查阅并遵守相应数据提供方的规定。

## 致谢

感谢所有数据提供机构以及为本项目做出贡献的开发者们！

### 主要数据提供机构

- 中国气象局 (CMA)  
- 美国国家海洋和大气管理局 (NOAA)  
- 欧洲中期天气预报中心 (ECMWF)  
- 欧洲空间局 (ESA)  
- 美国国家航空航天局 (NASA)  
- 谷歌云  
- 亚马逊云  

---

**注意**：数据链接和可用性可能会发生变化。如果您发现任何失效链接或有新的资源推荐，请通过 Issues 告知我们。

⭐ 如果这个项目对您有帮助，请给我们一个星标！
