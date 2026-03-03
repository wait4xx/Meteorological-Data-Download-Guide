# 🌤️ 公开气象数据下载资源库

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](CONTRIBUTING.md)
[![GitHub Stars](https://img.shields.io/github/stars/wait4xx/Meteorological-Data-Download-Guide.svg?style=flat-square)](https://github.com/wait4xx/Meteorological-Data-Download-Guide)
[![Status](https://img.shields.io/badge/状态-持续更新中-blue.svg?style=flat-square)](https://github.com/wait4xx/Meteorological-Data-Download-Guide)

> 一个收集整理各类公开气象数据下载网址的资源库，旨在为气象研究、数据分析和应用开发提供便捷的数据获取渠道。

---

### 📢 最新动态
> **2026-03-03** · 🎇 更新readme文档，优化显示
> 
> **2025-12-09** · ✨ ECMWF 下载脚本升级 — 新增 **IFS / EFS / AIFS / AIEFS** 全系列数据支持
>
> **2025-12-05** · 🚀 ECMWF 下载脚本发布 — 支持 **4 线程并行下载**，大幅提升效率

---

### 🔧 项目进展

| 类别 | 状态 |
|:-----|:----:|
| 数值预报数据 | ✅ |
| 大模型预报数据 | ✅ |
| 再分析数据 | ✅ |
| 实时观测数据 | 🔜 |
| 卫星数据 | 🔜 |
| 雷达数据 | 🔜 |
| 气候数据 | 🔜 |
| 海洋气象数据 | 🔜 |
| 空气质量数据 | 🔜 |
| 开源代码与工具 | 🔜 |

---

## 📚 目录

| 数据类型 | 工具与社区 |
|:--------:|:----------:|
| [数值预报](#数值预报数据) · [大模型](#大模型预报数据) · [再分析数据](#气候与再分析数据) | [贡献指南](#贡献指南) · [许可证](#许可证) |
| [实况观测](#实况观测数据) · [海洋气象](#海洋气象数据) · [空气质量](#空气质量数据) | [开源工具](#开源代码与工具) |
| [卫星数据](#卫星数据) · [雷达数据](#雷达数据) | [致谢](#致谢) |


## 数值预报数据

### 实时预报数据

<details>
<summary><b>ECMWF</b> · 欧洲中期天气预报中心</summary>

---

**IFS** · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~144h(3h)_144~360h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-官方-9CF?style=flat-square)

🔗 [ECMWF Open Data](https://data.ecmwf.int/forecasts/) · 📅 最近 4 日

---

**EFS** · 集合预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~144h(3h)_144~360h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-官方-9CF?style=flat-square)

🔗 [ECMWF Open Data](https://data.ecmwf.int/forecasts/) · 📅 最近 4 日

---

**IFS 数据格式说明**

> ![ec_file](./pics/ec_file.png)


</details>

<details>
<summary><b>NCEP</b> · 美国全球预报系统</summary>

---

**GFS** · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°/0.5°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~144h(3h)_144~360h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-UCAR-800080?style=flat-square)

🔗 [GFS_UCAR](https://motherlode.ucar.edu/native/grid/NCEP/GFS/) · 📅 最近 3 个月

---

**GFS** · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~120h(1h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-OpeNDAP-00BFFF?style=flat-square)

🔗 [GFS_OpeNDAP](https://nomads.ncep.noaa.gov/dods/gfs_0p25_1hr/) · 📅 最近 10 日 · 📝 [Python/xarray 示例](./sources/download_from_opendap.py)

---

**GFS** · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~384h(3h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-OpeNDAP-00BFFF?style=flat-square)

🔗 [GFS_OpeNDAP](https://nomads.ncep.noaa.gov/dods/gfs_0p25//) · 📅 最近 10 日 · 📝 [Python/xarray 示例](./sources/download_from_opendap.py)

---

**GFS** · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~120h(1h)_120~384h(3h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-NOAA-00CED1?style=flat-square)

🔗 [GFS_NOAA](https://nomads.ncep.noaa.gov/pub/data/nccf/com/gfs/) · 📅 最近 10 日

---

**GFS** · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.5°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~384h(3h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-OpeNDAP-00BFFF?style=flat-square)

🔗 [GFS_OpeNDAP](https://nomads.ncep.noaa.gov/dods/gfs_0p50/) · 📅 最近 10 日 · 📝 [Python/xarray 示例](./sources/download_from_opendap.py)

---

**GFS** · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-1°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~384h(3h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-OpeNDAP-00BFFF?style=flat-square)

🔗 [GFS_OpeNDAP](https://nomads.ncep.noaa.gov/dods/gfs_1p00/) · 📅 最近 10 日 · 📝 [Python/xarray 示例](./sources/download_from_opendap.py)

---

**GEFS** · 集合预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~240h(3h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-NOAA-00CED1?style=flat-square)

🔗 [GEFS_NOAA](https://nomads.ncep.noaa.gov/pub/data/nccf/com/gens/) · 📅 最近 4 日

---

**GEFS** · 集合预报

![分辨率](https://img.shields.io/badge/分辨率-0.5°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~240h(3h)_240~840h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-NOAA-00CED1?style=flat-square)

🔗 [GEFS_NOAA](https://nomads.ncep.noaa.gov/pub/data/nccf/com/gens/) · 📅 最近 4 日

</details>

<details>
<summary><b>DWD</b> · 德国天气局</summary>

---

**ICON** · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.125°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~144h(3h)_144~360h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-官方-9CF?style=flat-square)

🔗 [ICON Open Data](https://opendata.dwd.de/weather/nwp/icon/grib/) · 📅 最近 4 个起报

</details>

<details>
<summary><b>JMA</b> · 日本气象厅（无法直接下载，需要申请账号）</summary>

---

**GSM** · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°/0.5°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~144h(3h)_144~360h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-官方-9CF?style=flat-square)

🔗 [JMA GSM](https://www.wis-jma.go.jp/cms/gsm/download.html) · 📅 最近 5 日

</details>


### 历史预报数据

<details>
<summary><b>ECMWF</b> · 欧洲中期天气预报中心</summary>

---

**IFS (HRES ~ 地面)** · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.1°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~12h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-UCAR-800080?style=flat-square)

🔗 [IFS_UCAR](https://gdex.ucar.edu/datasets/d113001/dataaccess/#) · 📅 2016 年 1 月 1 日至今

---

**IFS** · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°/0.4°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~144h(3h)_144~360h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-Google-4285F4?style=flat-square)
![魔法](https://img.shields.io/badge/魔法-√-3126F0?style=flat-square)

🔗 [🪜 ECMWF_GOOGLE](https://console.cloud.google.com/storage/browser/ecmwf-open-data) · 📅 2023 年 7 月 12 日至今（有延迟）

---

**IFS** · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°/0.4°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~144h(3h)_144~360h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://ecmwf-forecasts.s3.amazonaws.com/) · 📅 2023 年 3 月 18 日至今 · ⚠️ 需 awscli 或补全 URL

---

**EFS** · 集合预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°/0.4°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~144h(3h)_144~360h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-Google-4285F4?style=flat-square)
![魔法](https://img.shields.io/badge/魔法-√-3126F0?style=flat-square)

🔗 [🪜 ECMWF_GOOGLE](https://console.cloud.google.com/storage/browser/ecmwf-open-data) · 📅 2023 年 7 月 12 日至今（有延迟）

---

**EFS** · 集合预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°/0.4°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~144h(3h)_144~360h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://ecmwf-forecasts.s3.amazonaws.com/) · 📅 2023 年 3 月 18 日至今 · ⚠️ 需 awscli 或补全 URL

</details>

<details>
<summary><b>NCEP</b> · 美国全球预报系统</summary>

---

**GFS** · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°/0.5°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~240h(3h)_240~384h(12h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-UCAR-800080?style=flat-square)

🔗 [GFS_UCAR](https://gdex.ucar.edu/datasets/d084001/dataaccess/) · 📅 2015 年 1 月 15 日至今（2026 年停更）

---

**GFS** · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°/0.5°/1°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~384h(3h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-gfs-bdp-pds.s3.amazonaws.com/index.html) · 📅 2021 年 1 月 1 日至今 · 🔍 搜索 `gfs`

---

**GFS** · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°/0.5°/1°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~384h(3h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-Google-4285F4?style=flat-square)
![魔法](https://img.shields.io/badge/魔法-√-3126F0?style=flat-square)

🔗 [🪜 GFS_GOOGLE](https://console.cloud.google.com/storage/browser/global-forecast-system) · 📅 2021 年 1 月 1 日至今 · 🔍 搜索 `gfs`

---

**GEFS** · 集合预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°/0.5°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~384h(6h)_0~240h(3h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-gefs-pds.s3.amazonaws.com/index.html) · 📅 2017 年 1 月 1 日至今

---

**GEFS** · 集合预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°/0.5°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~240h(3h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-Google-4285F4?style=flat-square)
![魔法](https://img.shields.io/badge/魔法-√-3126F0?style=flat-square)

🔗 [🪜 GFS_GOOGLE](https://console.cloud.google.com/storage/browser/gfs-ensemble-forecast-system) · 📅 2020 年 9 月 25 日至今

</details>

## 大模型预报数据

### 实时数据

<details>
<summary><b>ECMWF</b> · 欧洲中期天气预报中心</summary>

---

**AIFS** · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~360h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-官方-9CF?style=flat-square)

🔗 [ECMWF Open Data](https://data.ecmwf.int/forecasts/) · 📅 最近 4 日

---

**AIEFS** · 集合预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~360h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-官方-9CF?style=flat-square)

🔗 [ECMWF Open Data](https://data.ecmwf.int/forecasts/) · 📅 最近 4 日

</details>

<details>
<summary><b>NCEP</b> · 美国全球预报系统</summary>

---

**AIGFS** · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°/0.5°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~360h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-NOAA-00CED1?style=flat-square)

🔗 [AIGFS_NOAA](https://nomads.ncep.noaa.gov/pub/data/nccf/com/aigfs/) · 📅 最近 2 日

---

**AIGEFS** · 集合预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°/0.5°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~360h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-NOAA-00CED1?style=flat-square)

🔗 [AIGEFS_NOAA](https://nomads.ncep.noaa.gov/pub/data/nccf/com/aigefs/) · 📅 最近 2 日

</details>

<details>
<summary><b>AI 模型集合</b> · Aurora / FourCastNet / GraphCast / PANGU</summary>

---

**Aurora** · 微软 · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.5°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~240h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日2次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) · 📝 [数据说明](./docs/noaa-oar-mlwp-data.txt)

---

**FourCastNet** · NVIDIA · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.5°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~240h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日2次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) · 📝 [数据说明](./docs/noaa-oar-mlwp-data.txt)

---

**GraphCast** · Google / DeepMind · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.5°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~240h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日2次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) · 📝 [数据说明](./docs/noaa-oar-mlwp-data.txt)

---

**PANGU** · 华为 · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.5°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~240h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日2次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) · 📝 [数据说明](./docs/noaa-oar-mlwp-data.txt)

</details>

### 历史数据

<details>
<summary><b>ECMWF</b> · 欧洲中期天气预报中心</summary>

---

**AIFS** · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~360h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://ecmwf-forecasts.s3.amazonaws.com/) · 📅 2024 年 2 月 29 日至今 · ⚠️ 需 awscli 或补全 URL

---

**AIEFS** · 集合预报

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~360h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日4次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://ecmwf-forecasts.s3.amazonaws.com/) · ⚠️ 需 awscli 或补全 URL

</details>

<details>
<summary><b>AI 模型集合</b> · Aurora / FourCastNet / GraphCast / PANGU</summary>

---

**Aurora** · 微软 · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.5°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~240h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日2次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) · 📅 2025 年 1 月 23 日至今 · 📝 [数据说明](./docs/noaa-oar-mlwp-data.txt)

---

**FourCastNet** · NVIDIA · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.5°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~240h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日2次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) · 📅 2020 年 9 月 30 日至今 · 📝 [数据说明](./docs/noaa-oar-mlwp-data.txt)

---

**GraphCast** · Google / DeepMind · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.5°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~240h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日2次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) · 📅 2020 年 9 月 30 日至今 · 📝 [数据说明](./docs/noaa-oar-mlwp-data.txt)

---

**PANGU** · 华为 · 确定性预报

![分辨率](https://img.shields.io/badge/分辨率-0.5°-blue?style=flat-square)
![时效](https://img.shields.io/badge/时效-0~240h(6h)-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日2次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) · 📅 2020 年 9 月 30 日至今 · 📝 [数据说明](./docs/noaa-oar-mlwp-data.txt)

</details>

## 气候与再分析数据

### 再分析数据集

<details>
<summary><b>ERA5-land</b> · ECMWF 地面再分析 </summary>

***无魔法情况下推荐通过AWS+IDM多线程下载，下载速度最快***

---

**ERA5-land (hourly)**

![分辨率](https://img.shields.io/badge/分辨率-0.1°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-hourly-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1950年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-CDS-00CED1?style=flat-square)

🔗 [ERA5-land](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-land?tab=download)

---

**ERA5-land (hourly)**

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-hourly-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1940年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://nsf-ncar-era5.s3.amazonaws.com/index.html#e5.oper.an.sfc/) · 📅 数据延迟三个月

---

**ERA5-land (monthly)**

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-monthly_mean-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1950年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-CDS-00CED1?style=flat-square)

🔗 [ERA5-land (monthly)](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-land-monthly-means?tab=download)

---

**ERA5 (hourly)**

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-hourly/monthly-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1940年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-Google-4285F4?style=flat-square)
![魔法](https://img.shields.io/badge/魔法-√-3126F0?style=flat-square)

🔗 [🪜 ERA5_GOOGLE](https://console.cloud.google.com/storage/browser/gcp-public-data-arco-era5/raw/ERA5GRIB/HRES)

</details>

<details>
<summary><b>ERA5-pressure</b> · ECMWF 气压层再分析</summary>

***无魔法情况下推荐通过AWS+IDM多线程下载，下载速度最快***

---

**ERA5-pressure (hourly)**

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-hourly-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1940年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-CDS-00CED1?style=flat-square)

🔗 [ERA5-pressure](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-pressure-levels?tab=download)

---

**ERA5-pressure (hourly)**

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-hourly-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1940年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://nsf-ncar-era5.s3.amazonaws.com/index.html#e5.oper.an.pl/) · 📅 数据延迟三个月

---

**ERA5-pressure (monthly)**

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-monthly_mean-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1940年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-CDS-00CED1?style=flat-square)

🔗 [ERA5-pressure (monthly)](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-pressure-levels-monthly-means?tab=download)

---

**ERA5 (hourly)**

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-hourly/monthly-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1940年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-Google-4285F4?style=flat-square)
![魔法](https://img.shields.io/badge/魔法-√-3126F0?style=flat-square)

🔗 [🪜 ERA5_GOOGLE](https://console.cloud.google.com/storage/browser/gcp-public-data-arco-era5/raw/ERA5GRIB/HRES)

</details>


<details>
<summary><b>FNL</b> · NCEP 最终分析</summary>

---

**FNL**

![分辨率](https://img.shields.io/badge/分辨率-0.25°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-6_hourly-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-2015年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-UCAR-800080?style=flat-square)

🔗 [FNL_UCAR](https://gdex.ucar.edu/datasets/d083003/dataaccess/#)

---

**FNL**

![分辨率](https://img.shields.io/badge/分辨率-1°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-6_hourly-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1999年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-UCAR-800080?style=flat-square)

🔗 [FNL_UCAR](https://gdex.ucar.edu/datasets/d083002/dataaccess/#)

</details>

<details>
<summary><b>JRA-3Q</b> · JMA 再分析</summary>

---

**DIAS**

![分辨率](https://img.shields.io/badge/分辨率-1.25°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-hourly/monthly_mean-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1947年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-DIAS-9CF?style=flat-square)

🔗 [JRA-3Q_DIAS](https://data.diasjp.net/dl/storages/filelist/dataset:645) · ⚠️ 需登录

---

**UCAR (historical)**

![分辨率](https://img.shields.io/badge/分辨率-1.25°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-hourly-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1947年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-UCAR-800080?style=flat-square)

🔗 [JRA-3Q_UCAR](https://gdex.ucar.edu/datasets/d640000/dataaccess/#)

---

**UCAR (near-real)**

![分辨率](https://img.shields.io/badge/分辨率-1.25°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-hourly-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-2023年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-UCAR-800080?style=flat-square)

🔗 [JRA-3Q_UCAR](https://gdex.ucar.edu/datasets/d640001/dataaccess/#) · 🔄 近实时

---

**UCAR (monthly)**

![分辨率](https://img.shields.io/badge/分辨率-1.25°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-monthly_mean-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1947年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-UCAR-800080?style=flat-square)

🔗 [JRA-3Q_UCAR](https://gdex.ucar.edu/datasets/d640002/dataaccess/#)

</details>

<details>
<summary><b>MERRA-2</b> · NASA 再分析</summary>

![分辨率](https://img.shields.io/badge/分辨率-0.5°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-hourly/monthly-green?style=flat-square)
![时间范围](https://img.shields.io/badge/时间范围-1980年至今-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-NASA-FF0000?style=flat-square)

🔗 [MERRA_GSFC](https://disc.gsfc.nasa.gov/datasets?project=MERRA-2) · [MERRA_FTP](https://goldsmr4.gesdisc.eosdis.nasa.gov/data/)

</details>

### 气候数据集

<details>
<summary><b>CRU TS</b> · 格点化观测</summary>

![类型](https://img.shields.io/badge/类型-格点化观测-blue?style=flat-square)
![分辨率](https://img.shields.io/badge/分辨率-0.5°-green?style=flat-square)
![时段](https://img.shields.io/badge/时段-1901~现在-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-UEA-00BFFF?style=flat-square)

🔗 [UEA](https://crudata.uea.ac.uk/cru/data/hrg/)

</details>

<details>
<summary><b>GPCC</b> · 降水数据集</summary>

![类型](https://img.shields.io/badge/类型-降水-blue?style=flat-square)
![分辨率](https://img.shields.io/badge/分辨率-0.25°~2.5°-green?style=flat-square)
![时段](https://img.shields.io/badge/时段-1891~现在-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-DWD-00BFFF?style=flat-square)

🔗 [DWD](https://www.dwd.de/EN/ourservices/gpcc/gpcc.html)

</details>


## 实况观测数据

### 地面观测

<details>
<summary><b>ASOS/AWOS</b> · 全球机场观测</summary>

![覆盖](https://img.shields.io/badge/覆盖-全球机场-blue?style=flat-square)
![要素](https://img.shields.io/badge/要素-多要素-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-实时-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-NOAA-00CED1?style=flat-square)

🔗 [NOAA](https://www.ncei.noaa.gov/maps/hourly/)

</details>

<details>
<summary><b>SYNOP</b> · 全球地面观测</summary>

![覆盖](https://img.shields.io/badge/覆盖-全球-blue?style=flat-square)
![要素](https://img.shields.io/badge/要素-基本气象要素-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-3/6小时-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-OGIMET-9CF?style=flat-square)

🔗 [OGIMET](https://www.ogimet.com/)

</details>

<details>
<summary><b>MADIS</b> · 北美多源数据</summary>

![覆盖](https://img.shields.io/badge/覆盖-北美-blue?style=flat-square)
![要素](https://img.shields.io/badge/要素-多源数据-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-实时-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-NOAA-00CED1?style=flat-square)

🔗 [NOAA MADIS](https://madis.ncep.noaa.gov/)

</details>

### 高空观测

<details>
<summary><b>IGRA</b> · 全球探空</summary>

![覆盖](https://img.shields.io/badge/覆盖-全球-blue?style=flat-square)
![层次](https://img.shields.io/badge/层次-标准层-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日2次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-NOAA-00CED1?style=flat-square)

🔗 [NOAA IGRA](https://www.ncei.noaa.gov/access/weather/igra/)

</details>

<details>
<summary><b>AMDAR</b> · 全球航线观测</summary>

![覆盖](https://img.shields.io/badge/覆盖-全球航线-blue?style=flat-square)
![层次](https://img.shields.io/badge/层次-飞行层-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-实时-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-WMO-9CF?style=flat-square)

🔗 [WMO AMDAR](https://amdar.wmo.int/)

</details>

### 自动气象站

<details>
<summary><b>MesoWest</b> · 美国区域站网</summary>

![规模](https://img.shields.io/badge/规模-数千站-blue?style=flat-square)
![区域](https://img.shields.io/badge/区域-美国-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-官方-9CF?style=flat-square)

🔗 [MesoWest](https://mesowest.utah.edu/)

</details>

<details>
<summary><b>Weather Underground</b> · 全球个人站</summary>

![规模](https://img.shields.io/badge/规模-全球个人站-blue?style=flat-square)
![区域](https://img.shields.io/badge/区域-全球-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-官方-9CF?style=flat-square)

🔗 [WUnderground](https://www.wunderground.com/)

</details>

## 卫星数据

### 地球同步卫星

<details>
<summary><b>Himawari-8/9</b> · JMA · 亚太</summary>

![产品](https://img.shields.io/badge/产品-云图/气溶胶-blue?style=flat-square)
![覆盖](https://img.shields.io/badge/覆盖-亚太-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-JAXA-9CF?style=flat-square)

🔗 [JAXA](https://www.eorc.jaxa.jp/ptree/)

</details>

<details>
<summary><b>GOES-16/18</b> · NOAA · 美洲</summary>

![产品](https://img.shields.io/badge/产品-多通道图像-blue?style=flat-square)
![覆盖](https://img.shields.io/badge/覆盖-美洲-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-NOAA-00CED1?style=flat-square)

🔗 [NOAA GOES](https://www.noaa.gov/goes-16-and-goes-17-satellite-data)

</details>

<details>
<summary><b>FY-4A/4B</b> · CMA · 亚洲</summary>

![产品](https://img.shields.io/badge/产品-云图/降水-blue?style=flat-square)
![覆盖](https://img.shields.io/badge/覆盖-亚洲-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-NSMC-9CF?style=flat-square)

🔗 [NSMC](http://satellite.nsmc.org.cn/)

</details>

### 极轨卫星

<details>
<summary><b>Suomi NPP</b> · NASA/NOAA</summary>

![分辨率](https://img.shields.io/badge/分辨率-750m-blue?style=flat-square)
![产品](https://img.shields.io/badge/产品-VIIRS数据-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-NASA-FF0000?style=flat-square)

🔗 [NASA LAADS](https://ladsweb.modaps.eosdis.nasa.gov/)

</details>

<details>
<summary><b>JPSS</b> · NOAA</summary>

![分辨率](https://img.shields.io/badge/分辨率-375m-blue?style=flat-square)
![产品](https://img.shields.io/badge/产品-多光谱数据-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-NOAA-00CED1?style=flat-square)

🔗 [NOAA CLASS](https://www.avl.class.noaa.gov/)

</details>

<details>
<summary><b>Sentinel-3</b> · ESA</summary>

![分辨率](https://img.shields.io/badge/分辨率-300m-blue?style=flat-square)
![产品](https://img.shields.io/badge/产品-海洋颜色-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-ESA-003399?style=flat-square)

🔗 [Copernicus](https://scihub.copernicus.eu/)

</details>

### 卫星降水产品

<details>
<summary><b>GPM IMERG</b> · 全球降水</summary>

![空间分辨率](https://img.shields.io/badge/空间分辨率-0.1°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-30分钟-green?style=flat-square)
![覆盖](https://img.shields.io/badge/覆盖-全球-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-NASA-FF0000?style=flat-square)

🔗 [NASA GES DISC](https://disc.gsfc.nasa.gov/)

</details>

<details>
<summary><b>CMORPH</b> · 全球降水</summary>

![空间分辨率](https://img.shields.io/badge/空间分辨率-0.25°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-30分钟-green?style=flat-square)
![覆盖](https://img.shields.io/badge/覆盖-全球-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-NOAA-00CED1?style=flat-square)

🔗 [CPC](https://www.cpc.ncep.noaa.gov/products/janowiak/cmorph_description.html)

</details>

## 雷达数据

### 天气雷达

<details>
<summary><b>NEXRAD</b> · 美国天气雷达网</summary>

![覆盖](https://img.shields.io/badge/覆盖-美国-blue?style=flat-square)
![产品](https://img.shields.io/badge/产品-基数据/产品-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-NOAA-00CED1?style=flat-square)

🔗 [NOAA NCEI](https://www.ncdc.noaa.gov/nexradinv/)

</details>

<details>
<summary><b>OPERA</b> · 欧洲雷达网</summary>

![覆盖](https://img.shields.io/badge/覆盖-欧洲-blue?style=flat-square)
![产品](https://img.shields.io/badge/产品-合成产品-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-EUMETNET-9CF?style=flat-square)

🔗 [EUMETNET](https://www.eumetnet.eu/activities/observations-programme/current-activities/opera/)

</details>


## 实况观测数据

### 地面观测

<details>
<summary><b>ASOS/AWOS</b> · 全球机场观测</summary>

![覆盖](https://img.shields.io/badge/覆盖-全球机场-blue?style=flat-square)
![要素](https://img.shields.io/badge/要素-多要素-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-实时-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-NOAA-00CED1?style=flat-square)

🔗 [NOAA](https://www.ncei.noaa.gov/maps/hourly/)

</details>

<details>
<summary><b>SYNOP</b> · 全球地面观测</summary>

![覆盖](https://img.shields.io/badge/覆盖-全球-blue?style=flat-square)
![要素](https://img.shields.io/badge/要素-基本气象要素-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-3/6小时-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-OGIMET-00BFFF?style=flat-square)

🔗 [OGIMET](https://www.ogimet.com/)

</details>

<details>
<summary><b>MADIS</b> · 北美多源数据</summary>

![覆盖](https://img.shields.io/badge/覆盖-北美-blue?style=flat-square)
![要素](https://img.shields.io/badge/要素-多源数据-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-实时-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-NOAA-00CED1?style=flat-square)

🔗 [NOAA MADIS](https://madis.ncep.noaa.gov/)

</details>

### 高空观测

<details>
<summary><b>IGRA</b> · 全球探空</summary>

![覆盖](https://img.shields.io/badge/覆盖-全球-blue?style=flat-square)
![层次](https://img.shields.io/badge/层次-标准层-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-每日2次-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-NOAA-00CED1?style=flat-square)

🔗 [NOAA IGRA](https://www.ncei.noaa.gov/access/weather/igra/)

</details>

<details>
<summary><b>AMDAR</b> · 全球航线观测</summary>

![覆盖](https://img.shields.io/badge/覆盖-全球航线-blue?style=flat-square)
![层次](https://img.shields.io/badge/层次-飞行层-green?style=flat-square)
![更新](https://img.shields.io/badge/更新-实时-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-WMO-9CF?style=flat-square)

🔗 [WMO AMDAR](https://amdar.wmo.int/)

</details>

### 自动气象站

<details>
<summary><b>MesoWest</b> · 美国区域站网</summary>

![规模](https://img.shields.io/badge/规模-数千站-blue?style=flat-square)
![区域](https://img.shields.io/badge/区域-美国-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-MesoWest-00BFFF?style=flat-square)

🔗 [MesoWest](https://mesowest.utah.edu/)

</details>

<details>
<summary><b>Weather Underground</b> · 全球个人站</summary>

![规模](https://img.shields.io/badge/规模-全球个人站-blue?style=flat-square)
![区域](https://img.shields.io/badge/区域-全球-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-WUnderground-00BFFF?style=flat-square)

🔗 [WUnderground](https://www.wunderground.com/)

</details>

## 卫星数据

### 地球同步卫星

<details>
<summary><b>Himawari-8/9</b> · JMA · 亚太</summary>

![产品](https://img.shields.io/badge/产品-云图/气溶胶-blue?style=flat-square)
![覆盖](https://img.shields.io/badge/覆盖-亚太-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-JAXA-9CF?style=flat-square)

🔗 [JAXA](https://www.eorc.jaxa.jp/ptree/)

</details>

<details>
<summary><b>GOES-16/18</b> · NOAA · 美洲</summary>

![产品](https://img.shields.io/badge/产品-多通道图像-blue?style=flat-square)
![覆盖](https://img.shields.io/badge/覆盖-美洲-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-NOAA-00CED1?style=flat-square)

🔗 [NOAA GOES](https://www.noaa.gov/goes-16-and-goes-17-satellite-data)

</details>

<details>
<summary><b>FY-4A/4B</b> · CMA · 亚洲</summary>

![产品](https://img.shields.io/badge/产品-云图/降水-blue?style=flat-square)
![覆盖](https://img.shields.io/badge/覆盖-亚洲-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-NSMC-9CF?style=flat-square)

🔗 [NSMC](http://satellite.nsmc.org.cn/)

</details>

### 极轨卫星

<details>
<summary><b>Suomi NPP</b> · NASA/NOAA</summary>

![分辨率](https://img.shields.io/badge/分辨率-750m-blue?style=flat-square)
![产品](https://img.shields.io/badge/产品-VIIRS数据-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-NASA-FF0000?style=flat-square)

🔗 [NASA LAADS](https://ladsweb.modaps.eosdis.nasa.gov/)

</details>

<details>
<summary><b>JPSS</b> · NOAA</summary>

![分辨率](https://img.shields.io/badge/分辨率-375m-blue?style=flat-square)
![产品](https://img.shields.io/badge/产品-多光谱数据-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-NOAA-00CED1?style=flat-square)

🔗 [NOAA CLASS](https://www.avl.class.noaa.gov/)

</details>

<details>
<summary><b>Sentinel-3</b> · ESA</summary>

![分辨率](https://img.shields.io/badge/分辨率-300m-blue?style=flat-square)
![产品](https://img.shields.io/badge/产品-海洋颜色-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-ESA-003399?style=flat-square)

🔗 [Copernicus](https://scihub.copernicus.eu/)

</details>

### 卫星降水产品

<details>
<summary><b>GPM IMERG</b> · 全球降水</summary>

![空间分辨率](https://img.shields.io/badge/空间分辨率-0.1°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-30分钟-green?style=flat-square)
![覆盖](https://img.shields.io/badge/覆盖-全球-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-NASA-FF0000?style=flat-square)

🔗 [NASA GES DISC](https://disc.gsfc.nasa.gov/)

</details>

<details>
<summary><b>CMORPH</b> · 全球降水</summary>

![空间分辨率](https://img.shields.io/badge/空间分辨率-0.25°-blue?style=flat-square)
![时间分辨率](https://img.shields.io/badge/时间分辨率-30分钟-green?style=flat-square)
![覆盖](https://img.shields.io/badge/覆盖-全球-orange?style=flat-square)
![来源](https://img.shields.io/badge/来源-NOAA-00CED1?style=flat-square)

🔗 [CPC](https://www.cpc.ncep.noaa.gov/products/janowiak/cmorph_description.html)

</details>

## 雷达数据

### 天气雷达

<details>
<summary><b>NEXRAD</b> · 美国天气雷达网</summary>

![覆盖](https://img.shields.io/badge/覆盖-美国-blue?style=flat-square)
![产品](https://img.shields.io/badge/产品-基数据/产品-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-NOAA-00CED1?style=flat-square)

🔗 [NOAA NCEI](https://www.ncdc.noaa.gov/nexradinv/)

</details>

<details>
<summary><b>OPERA</b> · 欧洲雷达网</summary>

![覆盖](https://img.shields.io/badge/覆盖-欧洲-blue?style=flat-square)
![产品](https://img.shields.io/badge/产品-合成产品-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-EUMETNET-9CF?style=flat-square)

🔗 [EUMETNET](https://www.eumetnet.eu/activities/observations-programme/current-activities/opera/)

</details>


## 海洋气象数据

### 海洋观测

<details>
<summary><b>Argo</b> · 剖面浮标观测</summary>

![平台](https://img.shields.io/badge/平台-剖面浮标-blue?style=flat-square)
![要素](https://img.shields.io/badge/要素-温盐深-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-Argo-00BFFF?style=flat-square)

🔗 [Argo GDAC](https://argo.ucsd.edu/data/argo-data/)

</details>

<details>
<summary><b>TAO/TRITON</b> · 锚定浮标阵列</summary>

![平台](https://img.shields.io/badge/平台-锚定浮标-blue?style=flat-square)
![要素](https://img.shields.io/badge/要素-海洋气象-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-NOAA-00CED1?style=flat-square)

🔗 [PMEL](https://www.pmel.noaa.gov/tao/)

</details>

### 海洋模式

<details>
<summary><b>HYCOM</b> · 美国海军海洋模式</summary>

![分辨率](https://img.shields.io/badge/分辨率-1/12°-blue?style=flat-square)
![产品](https://img.shields.io/badge/产品-海洋分析预报-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-HYCOM-00BFFF?style=flat-square)

🔗 [HYCOM](https://www.hycom.org/)

</details>

<details>
<summary><b>CMEMS</b> · 欧盟海洋监测预报</summary>

![分辨率](https://img.shields.io/badge/分辨率-多种-blue?style=flat-square)
![产品](https://img.shields.io/badge/产品-海洋监测预报-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-Copernicus-003399?style=flat-square)

🔗 [Copernicus Marine](https://marine.copernicus.eu/)

</details>

## 空气质量数据

### 空气质量监测

<details>
<summary><b>AirNow</b> · 美国空气质量</summary>

![覆盖](https://img.shields.io/badge/覆盖-美国-blue?style=flat-square)
![污染物](https://img.shields.io/badge/污染物-主要污染物-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-AirNow-00BFFF?style=flat-square)

🔗 [AirNow](https://www.airnow.gov/)

</details>

<details>
<summary><b>OpenAQ</b> · 全球空气质量</summary>

![覆盖](https://img.shields.io/badge/覆盖-全球-blue?style=flat-square)
![污染物](https://img.shields.io/badge/污染物-多种污染物-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-OpenAQ-00BFFF?style=flat-square)

🔗 [OpenAQ](https://openaq.org/)

</details>

### 空气质量模式

<details>
<summary><b>CAMS</b> · ECMWF 全球空气质量预报</summary>

![分辨率](https://img.shields.io/badge/分辨率-0.4°-blue?style=flat-square)
![产品](https://img.shields.io/badge/产品-全球空气质量预报-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-CAMS-00CED1?style=flat-square)

🔗 [CAMS](https://atmosphere.copernicus.eu/)

</details>

## 开源代码与工具

### 数据下载与处理

<details>
<summary><b>Herbie</b> · Python · GFS/HRRR 数据下载</summary>

![语言](https://img.shields.io/badge/语言-Python-blue?style=flat-square)
![功能](https://img.shields.io/badge/功能-GFS/HRRR数据下载-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-GitHub-9CF?style=flat-square)

🔗 [GitHub](https://github.com/blaylockbk/Herbie)

</details>

<details>
<summary><b>Siphon</b> · Python · 远程数据访问</summary>

![语言](https://img.shields.io/badge/语言-Python-blue?style=flat-square)
![功能](https://img.shields.io/badge/功能-远程数据访问-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-Unidata-9CF?style=flat-square)

🔗 [Unidata](https://github.com/Unidata/siphon)

</details>

<details>
<summary><b>cfgrib</b> · Python · GRIB 文件处理</summary>

![语言](https://img.shields.io/badge/语言-Python-blue?style=flat-square)
![功能](https://img.shields.io/badge/功能-GRIB文件处理-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-ECMWF-00CED1?style=flat-square)

🔗 [ECMWF](https://github.com/ecmwf/cfgrib)

</details>

### 可视化与分析

<details>
<summary><b>MetPy</b> · Python · 气象数据分析可视化</summary>

![语言](https://img.shields.io/badge/语言-Python-blue?style=flat-square)
![功能](https://img.shields.io/badge/功能-气象数据分析可视化-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-Unidata-9CF?style=flat-square)

🔗 [Unidata](https://github.com/Unidata/MetPy)

</details>

<details>
<summary><b>Cartopy</b> · Python · 地图制图</summary>

![语言](https://img.shields.io/badge/语言-Python-blue?style=flat-square)
![功能](https://img.shields.io/badge/功能-地图制图-green?style=flat-square)
![来源](https://img.shields.io/badge/来源-SciTools-9CF?style=flat-square)

🔗 [SciTools](https://github.com/SciTools/cartopy)

</details>

## 贡献指南

我们欢迎并感谢所有形式的贡献！请参阅 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详细指南。

### 参与方式

| 🐛 报告问题 | 📦 添加资源 | 📝 改进文档 | 💬 分享用例 |
|:----------:|:----------:|:----------:|:----------:|
| 通过 [Issues](https://github.com/wait4xx/Meteorological-Data-Download-Guide/issues) 反馈 | 提交 Pull Request | 帮助完善或翻译 | 在 Discussions 分享 |

### 提交规范

> ✓ 链接有效且可公开访问 · ✓ 清晰的数据描述 · ✓ 遵循现有分类格式 · ✓ 注明许可限制  

## 许可证

> ⚠️ 本资源库中列出的数据源可能有各自的使用条款和许可协议，使用前请务必查阅并遵守相应数据提供方的规定。

## 致谢

感谢所有数据提供机构以及为本项目做出贡献的开发者们！

<div align="center">

![CMA](https://img.shields.io/badge/CMA-中国气象局-blue?style=flat-square)
![NOAA](https://img.shields.io/badge/NOAA-美国国家海洋和大气管理局-green?style=flat-square)
![ECMWF](https://img.shields.io/badge/ECMWF-欧洲中期天气预报中心-orange?style=flat-square)
![ESA](https://img.shields.io/badge/ESA-欧洲空间局-purple?style=flat-square)
![NASA](https://img.shields.io/badge/NASA-美国国家航空航天局-red?style=flat-square)
![Google Cloud](https://img.shields.io/badge/Google-Cloud-4285F4?style=flat-square)
![AWS](https://img.shields.io/badge/AWS-Amazon-FF9900?style=flat-square)

</div>

---

> ⚠️ **注意**：数据链接和可用性可能会发生变化。如发现失效链接或有新资源推荐，请通过 [Issues](https://github.com/wait4xx/Meteorological-Data-Download-Guide/issues) 告知我们。

<div align="center">

**⭐ 如果这个项目对您有帮助，请给我们一个星标！**

</div>
