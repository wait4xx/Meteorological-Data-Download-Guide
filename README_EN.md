<div align="center">

# 🌍 Public Earth-System Data Download Resource Guide

**A one-stop index of public meteorological · oceanographic · climate · environmental data, with download channels, access notes and companion scripts**

[![GitHub Stars](https://img.shields.io/github/stars/wait4xx/open-earth-data-guide?style=for-the-badge&logo=github)](https://github.com/wait4xx/open-earth-data-guide/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/wait4xx/open-earth-data-guide?style=for-the-badge&logo=github)](https://github.com/wait4xx/open-earth-data-guide/network/members)
[![License: MIT](https://img.shields.io/github/license/wait4xx/open-earth-data-guide?style=for-the-badge&logo=github)](#license)
[![Last Commit](https://img.shields.io/github/last-commit/wait4xx/open-earth-data-guide?style=for-the-badge&logo=git)](https://github.com/wait4xx/open-earth-data-guide/commits)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=for-the-badge&logo=github)](CONTRIBUTING_EN.md)

🌍 Global data sources · 📥 Companion scripts · 🔄 Continuously updated · 🤝 Contributions welcome

`Meteorological` `NWP` `AI Models` `Reanalysis` `Climate` `Observations` `Satellite` `Radar` `Air Quality` `Marine` `Marine Obs` `SST/Sea Ice` `Marine Models`

[中文](README.md) · **English**

</div>

> 📌 A curated collection of download channels and access notes for public meteorological, oceanographic, climate and environmental data, providing convenient data access for research, analysis and application development.

---

### 🧩 Companion Toolkit: [Open Earth Data Kit](https://github.com/wait4xx/open-earth-data-kit)

This repository is the **resource guide** — it focuses on “what data exists and where to download it”, collecting public data-source links, access notes and companion download scripts. If you’d rather converge these sources into a **unified command-line download platform**, check out its sibling project:

> 🌍 **[Open Earth Data Kit](https://github.com/wait4xx/open-earth-data-kit)** · Unified CLI toolkit for public earth-system data access
>
> Provides the `meteo` CLI (`list` / `info` / `plan` / `download` / `tasks`), a structured data-source catalog (59 sources), multi-protocol adapters (HTTP index / S3 / OPeNDAP / Zarr), swappable download backends (Python / IDM / XDM), and SQLite-based task state tracking.

**In short: the Guide tells you *where* to download, the Kit downloads *for you*.** The two share the same origin and complement each other — usable independently or together.

---

### 📢 Latest Updates
> **2026-06-13** · 🎉 Major update: added 18 public data sources (climate / observations / satellite / marine / air quality); open-source tools expanded to 20 as category tables; added MIT License & Star History; bilingual docs fully synced
>
> **2026-05-21** · 📝 Added Planette ERA5 AWS S3 download script for ERA5 daily, weekly and monthly mean data (`era5_planette_downloader.py`), supporting multi-variable concurrency, unit conversion, real-time progress
>
> **2026-04-11** · 📝 Added tutorial for ERA5 AWS S3 multi-threaded download script (`s3_downloader_multi.py`)
>
> **2026-03-03** · 🎇 Updated README, improved display
>
> **2025-12-09** · ✨ ECMWF download script upgraded — now supports **IFS / EFS / AIFS / AIEFS** full data series
>
> **2025-12-05** · 🚀 ECMWF download script released — supports **4-thread parallel downloads**, significantly improving efficiency

---

### 🔧 Project Progress

| Category | Sub-category | Status |
|:--------:|:-----|:----:|
| 🌐 Met | Numerical Weather Prediction | ✅ |
| | AI Model Forecasts | ✅ |
| | Reanalysis | ✅ |
| | Climate Data | ✅ |
| | Observations | ✅ |
| | Satellite | ✅ |
| | Radar | ✅ |
| | Air Quality | ✅ |
| 🌊 Marine | Marine Observations | ✅ |
| | SST & Sea Ice | ✅ |
| | Marine Models | ✅ |
| | Ocean Color | ✅ |
| 🛠️ Tools | Open Source Tools | ✅ |

---

## 📚 Contents

| Data Types | Tools & Community |
|:--------:|:----------:|
| **[🌐 Meteorological Data](#meteorological-data)** · [NWP](#numerical-weather-prediction) · [AI Models](#ai-model-forecasts) · [Reanalysis](#reanalysis) · [Climate](#climate-data) · [Observations](#observations) · [Satellite](#satellite) · [Radar](#radar) · [Air Quality](#air-quality) | [Contributing](#contributing) · [License](#license) |
| **[🌊 Marine Data](#marine-data)** · [Marine Obs](#marine-observations) · [SST/Sea Ice](#sst--sea-ice) · [Marine Models](#marine-models) · [Ocean Color](#ocean-color) | [Open Source Tools](#open-source-tools) · [Acknowledgements](#acknowledgements) |


## Meteorological Data

### Numerical Weather Prediction

#### Real-time Forecasts

<details>
<summary><b>ECMWF</b> · European Centre for Medium-Range Weather Forecasts</summary>

---

**IFS** · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~144h(3h)_144~360h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-4x_daily-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-Official-9CF?style=flat-square)

🔗 [ECMWF Open Data](https://data.ecmwf.int/forecasts/) · 📅 Last 4 days

---

**EFS** · Ensemble Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~144h(3h)_144~360h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-4x_daily-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-Official-9CF?style=flat-square)

🔗 [ECMWF Open Data](https://data.ecmwf.int/forecasts/) · 📅 Last 4 days

---

**IFS Data Format Guide**

> ![ec_file](./pics/ec_file.png)


</details>

<details>
<summary><b>NCEP</b> · Global Forecast System (USA)</summary>

---

**GFS** · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°/0.5°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~144h(3h)_144~360h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-4x_daily-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-UCAR-800080?style=flat-square)

🔗 [GFS_UCAR](https://motherlode.ucar.edu/native/grid/NCEP/GFS/) · 📅 Last 3 months

---

**GFS** · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~120h(1h)_120~384h(3h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-4x_daily-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-NOAA-00CED1?style=flat-square)

🔗 [GFS_NOAA](https://nomads.ncep.noaa.gov/pub/data/nccf/com/gfs/) · 📅 Last 10 days

---

**GFS OPeNDAP** · ⚠️ Retired

![Status](https://img.shields.io/badge/Status-Retired-red?style=flat-square)
![Source](https://img.shields.io/badge/Source-NOMADS_OpeNDAP-lightgrey?style=flat-square)

> ❌ NOMADS GFS OPeNDAP endpoints (`gfs_0p25_1hr` / `gfs_0p25` / `gfs_0p50` / `gfs_1p00`) were all retired in 2025 (Service Change Notice 25-81). Alternatives: raw GRIB via [GFS_NOAA](https://nomads.ncep.noaa.gov/pub/data/nccf/com/gfs/) above, [GFS_UCAR](https://motherlode.ucar.edu/native/grid/NCEP/GFS/) THREDDS; historical climate/reanalysis data see [NOAA PSL THREDDS](#reanalysis) below.

---

**GEFS** · Ensemble Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~240h(3h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-4x_daily-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-NOAA-00CED1?style=flat-square)

🔗 [GEFS_NOAA](https://nomads.ncep.noaa.gov/pub/data/nccf/com/gens/) · 📅 Last 4 days

---

**GEFS** · Ensemble Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.5°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~240h(3h)_240~840h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-4x_daily-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-NOAA-00CED1?style=flat-square)

🔗 [GEFS_NOAA](https://nomads.ncep.noaa.gov/pub/data/nccf/com/gens/) · 📅 Last 4 days

</details>

<details>
<summary><b>DWD</b> · German Weather Service</summary>

---

**ICON** · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.125°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~144h(3h)_144~360h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-4x_daily-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-Official-9CF?style=flat-square)

🔗 [ICON Open Data](https://opendata.dwd.de/weather/nwp/icon/grib/) · 📅 Last 4 runs

</details>

<details>
<summary><b>JMA</b> · Japan Meteorological Agency (no direct download, account required)</summary>

---

**GSM** · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°/0.5°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~144h(3h)_144~360h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-4x_daily-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-Official-9CF?style=flat-square)

🔗 [JMA GSM](https://www.wis-jma.go.jp/cms/gsm/download.html) · 📅 Last 5 days

</details>


#### Historical Forecasts

<details>
<summary><b>ECMWF</b> · European Centre for Medium-Range Weather Forecasts</summary>

---

**IFS (HRES ~ surface)** · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.1°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~12h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-4x_daily-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-UCAR-800080?style=flat-square)

🔗 [IFS_UCAR](https://gdex.ucar.edu/datasets/d113001/dataaccess/#) · 📅 2016-01-01 to present

---

**IFS** · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°/0.4°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~144h(3h)_144~360h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-4x_daily-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-Google-4285F4?style=flat-square)
![VPN](https://img.shields.io/badge/VPN-√-3126F0?style=flat-square)

🔗 [🪜 ECMWF_GOOGLE](https://console.cloud.google.com/storage/browser/ecmwf-open-data) · 📅 2023-07-12 to present (with delay)

---

**IFS** · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°/0.4°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~144h(3h)_144~360h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-4x_daily-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://ecmwf-forecasts.s3.amazonaws.com/) · 📅 2023-03-18 to present · ⚠️ awscli or full URL required

---

**EFS** · Ensemble Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°/0.4°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~144h(3h)_144~360h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-4x_daily-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-Google-4285F4?style=flat-square)
![VPN](https://img.shields.io/badge/VPN-√-3126F0?style=flat-square)

🔗 [🪜 ECMWF_GOOGLE](https://console.cloud.google.com/storage/browser/ecmwf-open-data) · 📅 2023-07-12 to present (with delay)

---

**EFS** · Ensemble Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°/0.4°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~144h(3h)_144~360h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-4x_daily-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://ecmwf-forecasts.s3.amazonaws.com/) · 📅 2023-03-18 to present · ⚠️ awscli or full URL required

</details>

<details>
<summary><b>NCEP</b> · Global Forecast System (USA)</summary>

---

**GFS** · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°/0.5°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~240h(3h)_240~384h(12h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-4x_daily-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-UCAR-800080?style=flat-square)

🔗 [GFS_UCAR](https://gdex.ucar.edu/datasets/d084001/dataaccess/) · 📅 2015-01-15 to present (discontinued 2026)

---

**GFS** · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°/0.5°/1°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~384h(3h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-4x_daily-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-gfs-bdp-pds.s3.amazonaws.com/index.html) · 📅 2021-01-01 to present · 🔍 search `gfs`

---

**GFS** · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°/0.5°/1°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~384h(3h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-4x_daily-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-Google-4285F4?style=flat-square)
![VPN](https://img.shields.io/badge/VPN-√-3126F0?style=flat-square)

🔗 [🪜 GFS_GOOGLE](https://console.cloud.google.com/storage/browser/global-forecast-system) · 📅 2021-01-01 to present · 🔍 search `gfs`

---

**GEFS** · Ensemble Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°/0.5°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~384h(6h)_0~240h(3h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-4x_daily-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-gefs-pds.s3.amazonaws.com/index.html) · 📅 2017-01-01 to present

---

**GEFS** · Ensemble Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°/0.5°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~240h(3h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-4x_daily-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-Google-4285F4?style=flat-square)
![VPN](https://img.shields.io/badge/VPN-√-3126F0?style=flat-square)

🔗 [🪜 GFS_GOOGLE](https://console.cloud.google.com/storage/browser/gfs-ensemble-forecast-system) · 📅 2020-09-25 to present

</details>

### AI Model Forecasts

#### Real-time Data

<details>
<summary><b>ECMWF</b> · European Centre for Medium-Range Weather Forecasts</summary>

---

**AIFS** · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~360h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-4x_daily-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-Official-9CF?style=flat-square)

🔗 [ECMWF Open Data](https://data.ecmwf.int/forecasts/) · 📅 Last 4 days

---

**AIEFS** · Ensemble Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~360h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-4x_daily-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-Official-9CF?style=flat-square)

🔗 [ECMWF Open Data](https://data.ecmwf.int/forecasts/) · 📅 Last 4 days

</details>

<details>
<summary><b>NCEP</b> · Global Forecast System (USA)</summary>

---

**AIGFS** · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°/0.5°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~360h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-4x_daily-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-NOAA-00CED1?style=flat-square)

🔗 [AIGFS_NOAA](https://nomads.ncep.noaa.gov/pub/data/nccf/com/aigfs/) · 📅 Last 2 days

---

**AIGEFS** · Ensemble Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°/0.5°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~360h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-4x_daily-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-NOAA-00CED1?style=flat-square)

🔗 [AIGEFS_NOAA](https://nomads.ncep.noaa.gov/pub/data/nccf/com/aigefs/) · 📅 Last 2 days

</details>

<details>
<summary><b>AI Model Collection</b> · Aurora / FourCastNet / GraphCast / PANGU</summary>

---

**Aurora** · Microsoft · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.5°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~240h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-2x_daily-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) · 📝 [Data notes](./docs/noaa-oar-mlwp-data.txt)

---

**FourCastNet** · NVIDIA · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.5°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~240h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-2x_daily-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) · 📝 [Data notes](./docs/noaa-oar-mlwp-data.txt)

---

**GraphCast** · Google / DeepMind · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.5°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~240h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-2x_daily-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) · 📝 [Data notes](./docs/noaa-oar-mlwp-data.txt)

---

**PANGU** · Huawei · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.5°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~240h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-2x_daily-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) · 📝 [Data notes](./docs/noaa-oar-mlwp-data.txt)

</details>

#### Historical Data

<details>
<summary><b>ECMWF</b> · European Centre for Medium-Range Weather Forecasts</summary>

---

**AIFS** · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~360h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-4x_daily-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://ecmwf-forecasts.s3.amazonaws.com/) · 📅 2024-02-29 to present · ⚠️ awscli or full URL required

---

**AIEFS** · Ensemble Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~360h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-4x_daily-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://ecmwf-forecasts.s3.amazonaws.com/) · ⚠️ awscli or full URL required

</details>

<details>
<summary><b>AI Model Collection</b> · Aurora / FourCastNet / GraphCast / PANGU</summary>

---

**Aurora** · Microsoft · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.5°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~240h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-2x_daily-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) · 📅 2025-01-23 to present · 📝 [Data notes](./docs/noaa-oar-mlwp-data.txt)

---

**FourCastNet** · NVIDIA · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.5°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~240h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-2x_daily-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) · 📅 2020-09-30 to present · 📝 [Data notes](./docs/noaa-oar-mlwp-data.txt)

---

**GraphCast** · Google / DeepMind · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.5°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~240h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-2x_daily-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) · 📅 2020-09-30 to present · 📝 [Data notes](./docs/noaa-oar-mlwp-data.txt)

---

**PANGU** · Huawei · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.5°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~240h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-2x_daily-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) · 📅 2020-09-30 to present · 📝 [Data notes](./docs/noaa-oar-mlwp-data.txt)

</details>

### Reanalysis

<details>
<summary><b>ERA5-land</b> · ECMWF land reanalysis</summary>

***Without VPN, AWS + IDM multi-threaded download is recommended for the fastest speed.***

---

**ERA5-land (hourly)**

![Resolution](https://img.shields.io/badge/Resolution-0.1°-blue?style=flat-square)
![Temporal Res](https://img.shields.io/badge/Temporal_Res-hourly-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1950--present-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-CDS-00CED1?style=flat-square)

🔗 [ERA5-land](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-land?tab=download)

---

**ERA5-land (hourly)**

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Temporal Res](https://img.shields.io/badge/Temporal_Res-hourly-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1940--present-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://nsf-ncar-era5.s3.amazonaws.com/index.html#e5.oper.an.sfc/) · 📅 3-4 month delay · 📝 [Python multi-thread script](./sources/s3_downloader_multi.py)

<details>
<summary>📖 s3_downloader_multi.py tutorial</summary>

---

**Overview**

`s3_downloader_multi.py` is a smart concurrent download script for ERA5 data on AWS S3. It calls IDM or XDM for multi-task parallel download, supporting resume, byte-level verification and auto-skip of completed files.

**Dependencies**

```bash
pip install requests beautifulsoup4 lxml
```

Also install one of:
- **IDM** (Windows, recommended): [Internet Download Manager](https://www.internetdownloadmanager.com/)
- **XDM** (cross-platform): [Xtreme Download Manager](https://xtremedownloadmanager.com/)

**Configure the download tool path**

Edit the `Config` class in the script:

```python
class Config:
    DOWNLOAD_TOOL = "idm"   # or "xdm"
    IDM_PATH = r"D:\Program Files (x86)\Internet Download Manager\IDMan.exe"
    XDM_PATH_LINUX  = "/opt/xdman/xdman"
    XDM_PATH_WINDOWS = r"C:\Program Files\XDM\xdman.exe"
```

**Command-line mode (recommended)**

```bash
python s3_downloader_multi.py -v <variables> -y <year range> -o <output dir> [options]
```

| Flag | Description | Example |
|------|-------------|---------|
| `-v` | Variable name(s), comma-separated | `2t` / `2t,10u,10v` |
| `-y` | Year range, single or interval | `2024` / `2020-2024` |
| `-m` | Months, comma-separated (default all year) | `1,2,3` |
| `-o` | Local output directory | `./era5_data` |
| `-t` | Download tool, `idm` or `xdm` (default `idm`) | `idm` |
| `-c` | Max concurrency (default 6) | `4` |
| `--dry-run` | Preview mode, no actual download | — |
| `--export` | Export file list as CSV/TXT | — |
| `--delay` | Data delay in months (default 5) | `3` |

**Examples**

```bash
# Preview 2024 2m temperature (no download)
python s3_downloader_multi.py -v 2t -y 2024 -o ./era5_data --dry-run --export

# Download 2023-2024 2m temp + 10m wind, 6-thread concurrent
python s3_downloader_multi.py -v 2t,10u,10v -y 2023-2024 -o ./era5_data -c 6

# Only Jun-Aug 2024 surface pressure
python s3_downloader_multi.py -v sp -y 2024 -m 6,7,8 -o ./era5_data
```

**Supported datasets (change `DATASET_PREFIX`)**

| Prefix | Description | Vars |
|--------|-------------|------|
| `e5.oper.an.sfc` | Surface analysis (default) | 62 |
| `e5.oper.an.pl` | Pressure-level analysis | 16 |
| `e5.oper.an.vinteg` | Vertically integrated | 36 |
| `e5.oper.fc.sfc.accumu` | Surface forecast accumulation | 38 |
| `e5.oper.fc.sfc.instan` | Surface forecast instantaneous | 14 |
| `e5.oper.fc.sfc.meanflux` | Surface forecast mean flux | 39 |
| `e5.oper.fc.sfc.minmax` | Surface forecast extremes | 5 |
| `e5.oper.invariant` | Constant invariants | 14 |

> The full variable tables for each dataset (codes, meaning, units) are in [README.md (中文)](README.md). Common surface variables: `2t` (2m temp), `2d` (2m dewpoint), `10u/10v` (10m wind), `100u/100v` (100m wind), `sp` (surface pressure), `msl` (MSL pressure), `tp`/`cp`/`lsp` (precipitation), `sd` (snow depth), `tcc/lcc/mcc/hcc` (cloud cover), `cape`, `blh`, soil temp/moisture (`stl1-4`, `swvl1-4`), etc.

**Notes**

- Data is usually delayed ~3-5 months; the script auto-skips unpublished months.
- Downloads are handed to IDM/XDM; completion is judged by scanning local file sizes.
- Logs are written to `download_log.txt` in the working directory.
- Fully downloaded files (≥ 99% of expected) are auto-skipped; resume is supported.

</details>

---

**ERA5-land (monthly)**

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Temporal Res](https://img.shields.io/badge/Temporal_Res-monthly_mean-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1950--present-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-CDS-00CED1?style=flat-square)

🔗 [ERA5-land (monthly)](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-land-monthly-means?tab=download)

---

**ERA5-land (daily / 7-day / monthly / 3-month)**

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Temporal Res](https://img.shields.io/badge/Temporal_Res-hourly-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1940--present-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://planette-era5.s3.amazonaws.com/index.html#era5/) · 📅 3-4 month delay · Zarr format · 📝 [Python script](./sources/era5_planette_downloader.py)

<details>
<summary>📖 era5_planette_downloader.py tutorial</summary>

---

**Overview**

`era5_planette_downloader.py` downloads ERA5 from the Planette AWS S3 bucket, supporting multi-variable concurrency, automatic unit conversion, spatial/temporal subsetting, and real-time progress/speed display.

**Dependencies**

```bash
pip install xarray icechunk s3fs numpy netcdf4 requests dask
```

**Basic usage**

```bash
python era5_planette_downloader.py -v <variables> -f <frequency> -o <output path> [options]
```

| Flag | Description | Example |
|------|-------------|---------|
| `-v` | Variable(s), space-separated | `t2m` / `t2m pr slp` |
| `-f` | Temporal frequency | `day` / `7day` / `month` / `3month` |
| `-g` | Grid resolution (default 0p25latx0p25lon) | `0p25latx0p25lon` |
| `-t` | Time range (YYYY-MM-DD) | `2020-01-01 2024-12-31` |
| `-r` | Spatial subset (lon_min lon_max lat_min lat_max) | `70 140 15 55` |
| `-o` | Output file or dir (dir = multi-variable) | `./t2m.nc` / `./output/` |
| `--format` | Output format (default netcdf4) | `netcdf4` / `zarr` |
| `--auto-name` | Auto-generate filename | — |
| `--concurrent` | Multi-variable concurrent download | — |
| `--workers` | Concurrent workers (default 4) | `8` |
| `--no-convert` | Disable unit conversion | — |
| `--no-resume` | Disable resume | — |
| `--list-variables` | List S3 variables | — |

**Examples**

```bash
# List available variables
python era5_planette_downloader.py --list-variables

# Download monthly 2m temp (2020-2024)
python era5_planette_downloader.py -v t2m -f month -t 2020-01-01 2024-12-31 -o ./t2m_monthly.nc

# Download and clip to China region
python era5_planette_downloader.py -v t2m -f month -t 2020-01-01 2020-12-31 -r 70 140 15 55 -o ./t2m_china.nc

# Multi-variable concurrent + auto naming
python era5_planette_downloader.py -v t2m pr slp -f month -t 2020-01-01 2024-12-31 -o ./output/ --auto-name --concurrent
```

**Supported variables (64 total)**

> Use `--list-variables` for the live list. The script auto-converts units for common variables (e.g. `t2m` K→°C, `ps`/`slp` Pa→hPa). Includes: surface (`t2m`, `t2m_max/min`, `td2m`, `ts`, `sst`, `ps`, `slp`, `pr`, `tcwv`, `cape`, `olr`, `sic`), wind (`u10m/v10m`, `u100m/v100m`, `tau_x/y`), pressure-level (`u/v/t/z/w/q` at 10/50/100/200/500/700/850 hPa), soil moisture (`swv_1-4`). The full variable list with units/conversions is in [README.md (中文)](README.md).

> ⚠️ **OLR sign**: ERA5 native `ttr` is positive downward, so OLR (positive upward) is usually `OLR = -ttr`.
> ⚠️ **Precipitation**: if the source is `tp` (m), convert to mm/day with `×1000×24`.

**Notes**

- Data is **Icechunk Zarr**, accessed via the Icechunk library (different from direct GRIB/NetCDF download).
- Output is standard **NetCDF4** or **Zarr**, openable directly with `xarray`.

</details>

---

**ERA5 (hourly/monthly)**

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Temporal Res](https://img.shields.io/badge/Temporal_Res-hourly/monthly-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1940--present-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-Google-4285F4?style=flat-square)
![VPN](https://img.shields.io/badge/VPN-√-3126F0?style=flat-square)

🔗 [🪜 ERA5_GOOGLE](https://console.cloud.google.com/storage/browser/gcp-public-data-arco-era5/raw/ERA5GRIB/HRES)

</details>

<details>
<summary><b>ERA5-pressure</b> · ECMWF pressure-level reanalysis</summary>

***Without VPN, AWS + IDM multi-threaded download is recommended for the fastest speed.***

---

**ERA5-pressure (hourly)**

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Temporal Res](https://img.shields.io/badge/Temporal_Res-hourly-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1940--present-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-CDS-00CED1?style=flat-square)

🔗 [ERA5-pressure](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-pressure-levels?tab=download)

---

**ERA5-pressure (hourly)**

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Temporal Res](https://img.shields.io/badge/Temporal_Res-hourly-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1940--present-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://nsf-ncar-era5.s3.amazonaws.com/index.html#e5.oper.an.pl/) · 📅 3-4 month delay · 📝 [Python multi-thread script](./sources/s3_downloader_multi.py) (set `DATASET_PREFIX` to `e5.oper.an.pl`)

---

**ERA5-pressure (monthly)**

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Temporal Res](https://img.shields.io/badge/Temporal_Res-monthly_mean-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1940--present-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-CDS-00CED1?style=flat-square)

🔗 [ERA5-pressure (monthly)](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-pressure-levels-monthly-means?tab=download)

---

**ERA5-pressure (daily / 7-day / monthly / 3-month)**

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Temporal Res](https://img.shields.io/badge/Temporal_Res-hourly-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1940--present-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://planette-era5.s3.amazonaws.com/index.html#era5/) · 📅 3-4 month delay · Zarr format · 📝 [Python script](./sources/era5_planette_downloader.py)

---

**ERA5 (hourly/monthly)**

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Temporal Res](https://img.shields.io/badge/Temporal_Res-hourly/monthly-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1940--present-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-Google-4285F4?style=flat-square)
![VPN](https://img.shields.io/badge/VPN-√-3126F0?style=flat-square)

🔗 [🪜 ERA5_GOOGLE](https://console.cloud.google.com/storage/browser/gcp-public-data-arco-era5/raw/ERA5GRIB/HRES)

</details>


<details>
<summary><b>FNL</b> · NCEP Final Analysis</summary>

---

**FNL**

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Temporal Res](https://img.shields.io/badge/Temporal_Res-6_hourly-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-2015--present-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-UCAR-800080?style=flat-square)

🔗 [FNL_UCAR](https://gdex.ucar.edu/datasets/d083003/dataaccess/#)

---

**FNL**

![Resolution](https://img.shields.io/badge/Resolution-1°-blue?style=flat-square)
![Temporal Res](https://img.shields.io/badge/Temporal_Res-6_hourly-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1999--present-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-UCAR-800080?style=flat-square)

🔗 [FNL_UCAR](https://gdex.ucar.edu/datasets/d083002/dataaccess/#)

</details>

<details>
<summary><b>JRA-3Q</b> · JMA Reanalysis</summary>

---

**DIAS**

![Resolution](https://img.shields.io/badge/Resolution-1.25°-blue?style=flat-square)
![Temporal Res](https://img.shields.io/badge/Temporal_Res-hourly/monthly_mean-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1947--present-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-DIAS-9CF?style=flat-square)

🔗 [JRA-3Q_DIAS](https://data.diasjp.net/dl/storages/filelist/dataset:645) · ⚠️ Login required

---

**UCAR (historical)**

![Resolution](https://img.shields.io/badge/Resolution-1.25°-blue?style=flat-square)
![Temporal Res](https://img.shields.io/badge/Temporal_Res-hourly-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1947--present-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-UCAR-800080?style=flat-square)

🔗 [JRA-3Q_UCAR](https://gdex.ucar.edu/datasets/d640000/dataaccess/#)

---

**UCAR (near-real-time)**

![Resolution](https://img.shields.io/badge/Resolution-1.25°-blue?style=flat-square)
![Temporal Res](https://img.shields.io/badge/Temporal_Res-hourly-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-2023--present-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-UCAR-800080?style=flat-square)

🔗 [JRA-3Q_UCAR](https://gdex.ucar.edu/datasets/d640001/dataaccess/#) · 🔄 near-real-time

---

**UCAR (monthly)**

![Resolution](https://img.shields.io/badge/Resolution-1.25°-blue?style=flat-square)
![Temporal Res](https://img.shields.io/badge/Temporal_Res-monthly_mean-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1947--present-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-UCAR-800080?style=flat-square)

🔗 [JRA-3Q_UCAR](https://gdex.ucar.edu/datasets/d640002/dataaccess/#)

</details>

<details>
<summary><b>MERRA-2</b> · NASA Reanalysis</summary>

![Resolution](https://img.shields.io/badge/Resolution-0.5°-blue?style=flat-square)
![Temporal Res](https://img.shields.io/badge/Temporal_Res-hourly/monthly-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1980--present-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-NASA-FF0000?style=flat-square)

🔗 [MERRA_GSFC](https://disc.gsfc.nasa.gov/datasets?project=MERRA-2) · [MERRA_FTP](https://goldsmr4.gesdisc.eosdis.nasa.gov/data/)

</details>

<details>
<summary><b>NCEP/NCAR R1</b> · Classic global reanalysis · OPeNDAP</summary>

![Resolution](https://img.shields.io/badge/Resolution-2.5°-blue?style=flat-square)
![Temporal Res](https://img.shields.io/badge/Temporal_Res-daily/monthly-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1948--present-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-PSL_THREDDS-00CED1?style=flat-square)

Surface (slp/air/pr_wtr/rhum), 17 pressure levels (hgt/uwnd/vwnd/air/shum); plus 2m temp, soil moisture, tropopause, sulfate AOD, etc. Daily data split by year.

🔗 📂 [Catalog](https://psl.noaa.gov/thredds/catalog/Datasets/ncep.reanalysis.derived/surface/catalog.html) · OPeNDAP `https://psl.noaa.gov/thredds/dodsC/Datasets/ncep.reanalysis.derived/surface/air.mon.mean.nc` · 📝 [Script](./sources/download_from_opendap.py)

</details>

<details>
<summary><b>NCEP/DOE R2</b> · Improved R1 · OPeNDAP</summary>

![Resolution](https://img.shields.io/badge/Resolution-2.5°-blue?style=flat-square)
![Temporal Res](https://img.shields.io/badge/Temporal_Res-daily/monthly-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1979--present-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-PSL_THREDDS-00CED1?style=flat-square)

🔗 📂 [Catalog](https://psl.noaa.gov/thredds/catalog/Datasets/ncep.reanalysis2.derived/surface/catalog.html) · OPeNDAP `https://psl.noaa.gov/thredds/dodsC/Datasets/ncep.reanalysis2.derived/surface/mslp.mon.mean.nc` · 📝 [Script](./sources/download_from_opendap.py)

</details>

<details>
<summary><b>NARR</b> · North American Regional Reanalysis · OPeNDAP</summary>

![Resolution](https://img.shields.io/badge/Resolution-~32km-blue?style=flat-square)
![Temporal Res](https://img.shields.io/badge/Temporal_Res-daily/3-hourly-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1979--present-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-PSL_THREDDS-00CED1?style=flat-square)

⚠️ Lambert Conformal projection; lat/lon are 2D arrays and need extra handling.

🔗 📂 [Catalog](https://psl.noaa.gov/thredds/catalog/Datasets/NARR/monolevel/catalog.html) · OPeNDAP `https://psl.noaa.gov/thredds/dodsC/Datasets/NARR/monolevel/air.2m.2024.nc` · 📝 [Script](./sources/download_from_opendap.py)

</details>

<details>
<summary><b>20th Century Reanalysis V2/V2c</b> · Long historical reanalysis · OPeNDAP</summary>

![Resolution](https://img.shields.io/badge/Resolution-~2°-blue?style=flat-square)
![Temporal Res](https://img.shields.io/badge/Temporal_Res-daily-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1851~2014-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-PSL_THREDDS-00CED1?style=flat-square)

Historical reanalysis assimilating surface pressure observations; extremely long time span.

🔗 📂 [Catalog](https://psl.noaa.gov/thredds/catalog/Datasets/20thC_ReanV2c/Dailies/pressure/catalog.html) · OPeNDAP `https://psl.noaa.gov/thredds/dodsC/Datasets/20thC_ReanV2c/Dailies/pressure/hgt.2014.nc` · 📝 [Script](./sources/download_from_opendap.py)

</details>


### Climate Data

<details>
<summary><b>CRU TS</b> · Gridded observations</summary>

![Type](https://img.shields.io/badge/Type-gridded_obs-blue?style=flat-square)
![Resolution](https://img.shields.io/badge/Resolution-0.5°-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1901~present-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-UEA-00BFFF?style=flat-square)

🔗 [UEA](https://crudata.uea.ac.uk/cru/data/hrg/)

</details>

<details>
<summary><b>GPCC</b> · Precipitation dataset</summary>

![Type](https://img.shields.io/badge/Type-precipitation-blue?style=flat-square)
![Resolution](https://img.shields.io/badge/Resolution-0.25°~2.5°-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1891~present-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-DWD-00BFFF?style=flat-square)

🔗 [DWD](https://www.dwd.de/EN/ourservices/gpcc/gpcc.html)

</details>

<details>
<summary><b>GPCP</b> · Global Precipitation Climatology (satellite + station) · OPeNDAP</summary>

![Resolution](https://img.shields.io/badge/Resolution-2.5°-blue?style=flat-square)
![Temporal Res](https://img.shields.io/badge/Temporal_Res-monthly-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1979--present-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-PSL_THREDDS-00CED1?style=flat-square)

Global precipitation product combining satellite and surface observations.

🔗 📂 [Catalog](https://psl.noaa.gov/thredds/catalog/Datasets/gpcp/catalog.html) · OPeNDAP `https://psl.noaa.gov/thredds/dodsC/Datasets/gpcp/precip.mon.mean.nc` · 📝 [Script](./sources/download_from_opendap.py)

</details>

<details>
<summary><b>CPC Global Precip / Tmax</b> · High-res gridded observations · OPeNDAP</summary>

![Resolution](https://img.shields.io/badge/Resolution-0.5°-blue?style=flat-square)
![Temporal Res](https://img.shields.io/badge/Temporal_Res-daily-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1979--present-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-PSL_THREDDS-00CED1?style=flat-square)

Station-based gridded product, `precip` / `tmax`; 5× higher resolution than GPCP (2.5°).

🔗 📂 [Catalog](https://psl.noaa.gov/thredds/catalog/Datasets/cpc_global_precip/catalog.html) · OPeNDAP `https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_global_precip/precip.2024.nc` · 📝 [Script](./sources/download_from_opendap.py)

</details>

<details>
<summary><b>CPC Blended OLR</b> · Outgoing Longwave Radiation · OPeNDAP</summary>

![Resolution](https://img.shields.io/badge/Resolution-1.0°/2.5°-blue?style=flat-square)
![Temporal Res](https://img.shields.io/badge/Temporal_Res-daily-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1979--present-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-PSL_THREDDS-00CED1?style=flat-square)

Core data for typhoon / tropical convection research, `olr` (W/m²).

🔗 📂 [Catalog](https://psl.noaa.gov/thredds/catalog/Datasets/cpc_blended_olr-1deg/catalog.html) · OPeNDAP `https://psl.noaa.gov/thredds/dodsC/Datasets/cpc_blended_olr-1deg/olr.day.mean.nc` · 📝 [Script](./sources/download_from_opendap.py)

</details>

<details>
<summary><b>Dai PDSI</b> · Palmer Drought Severity Index · OPeNDAP</summary>

![Resolution](https://img.shields.io/badge/Resolution-2.5°-blue?style=flat-square)
![Temporal Res](https://img.shields.io/badge/Temporal_Res-monthly-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1850--present-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-PSL_THREDDS-00CED1?style=flat-square)

Land-only, 170+ years of long-term drought monitoring data.

🔗 📂 [Catalog](https://psl.noaa.gov/thredds/catalog/Datasets/dai_pdsi/catalog.html) · OPeNDAP `https://psl.noaa.gov/thredds/dodsC/Datasets/dai_pdsi/pdsi.mon.mean.nc` · 📝 [Script](./sources/download_from_opendap.py)

</details>

<details>
<summary><b>NOAA Global Temperature Anomaly</b> · Climate monitoring · OPeNDAP</summary>

![Resolution](https://img.shields.io/badge/Resolution-5.0°-blue?style=flat-square)
![Temporal Res](https://img.shields.io/badge/Temporal_Res-monthly-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1880--present-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-PSL_THREDDS-00CED1?style=flat-square)

Global surface temperature anomaly (`air`, °C), a foundational climate-change monitoring dataset.

🔗 📂 [Catalog](https://psl.noaa.gov/thredds/catalog/Datasets/noaaglobaltemp/catalog.html) · OPeNDAP `https://psl.noaa.gov/thredds/dodsC/Datasets/noaaglobaltemp/air.mon.anom.nc` · 📝 [Script](./sources/download_from_opendap.py)

</details>

<details>
<summary><b>JMA Global Temperature Anomaly</b> · Climate monitoring · OPeNDAP</summary>

![Resolution](https://img.shields.io/badge/Resolution-5.0°-blue?style=flat-square)
![Temporal Res](https://img.shields.io/badge/Temporal_Res-monthly-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1891--present-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-PSL_THREDDS-00CED1?style=flat-square)

JMA global surface temperature anomaly (`air`, °C); cross-validates the NOAA anomaly.

🔗 📂 [Catalog](https://psl.noaa.gov/thredds/catalog/Datasets/jmatemp/catalog.html) · OPeNDAP `https://psl.noaa.gov/thredds/dodsC/Datasets/jmatemp/air.mon.anom.nc` · 📝 [Script](./sources/download_from_opendap.py)

</details>

<details>
<summary><b>Berkeley Earth</b> · Independent global surface temperature</summary>

![Type](https://img.shields.io/badge/Type-surface_temp-blue?style=flat-square)
![Resolution](https://img.shields.io/badge/Resolution-1°-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1753~present-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-Berkeley_Earth-00BFFF?style=flat-square)

Independently constructed global land + ocean surface temperature dataset, often used to cross-validate climate warming.

🔗 [Berkeley Earth](http://berkeleyearth.org/data/)

</details>

<details>
<summary><b>HadCRUT5</b> · Met Office land + ocean temperature</summary>

![Type](https://img.shields.io/badge/Type-land+ocean_temp-blue?style=flat-square)
![Resolution](https://img.shields.io/badge/Resolution-5°-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1850~present-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-Met_Office-00BFFF?style=flat-square)

Maintained by the UK Met Office Hadley Centre and UEA CRU; includes an ensemble version with uncertainty.

🔗 [HadCRUT5](https://www.metoffice.gov.uk/hadobs/hadcrut5/)

</details>

<details>
<summary><b>GHCN-Daily</b> · Global Historical Climatology Network (daily)</summary>

![Type](https://img.shields.io/badge/Type-station_obs-blue?style=flat-square)
![Variables](https://img.shields.io/badge/Variables-temp/precip/snow-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1763~present-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-NCEI-00CED1?style=flat-square)

Daily observations from global land stations (temp, precip, snow, etc.); foundational station data for long-term climate studies.

🔗 [NCEI GHCN-Daily](https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily)

</details>

<details>
<summary><b>GHCN-Monthly</b> · Global Historical Climatology Network (monthly)</summary>

![Type](https://img.shields.io/badge/Type-station_obs-blue?style=flat-square)
![Variables](https://img.shields.io/badge/Variables-temp/precip-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1680~present-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-NCEI-00CED1?style=flat-square)

Monthly statistics from global land stations; suited to long-term trend and decadal variability analysis.

🔗 [NCEI GHCN-Monthly](https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-monthly)

</details>


### Observations

#### Surface Observations

<details>
<summary><b>ASOS/AWOS</b> · Global airport observations</summary>

![Coverage](https://img.shields.io/badge/Coverage-global_airports-blue?style=flat-square)
![Variables](https://img.shields.io/badge/Variables-multi--element-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-real_time-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-NOAA-00CED1?style=flat-square)

🔗 [NOAA](https://www.ncei.noaa.gov/maps/hourly/)

</details>

<details>
<summary><b>SYNOP</b> · Global surface observations</summary>

![Coverage](https://img.shields.io/badge/Coverage-global-blue?style=flat-square)
![Variables](https://img.shields.io/badge/Variables-basic_meteo-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-3/6h-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-OGIMET-00BFFF?style=flat-square)

🔗 [OGIMET](https://www.ogimet.com/)

</details>

<details>
<summary><b>MADIS</b> · North American multi-source data</summary>

![Coverage](https://img.shields.io/badge/Coverage-N._America-blue?style=flat-square)
![Variables](https://img.shields.io/badge/Variables-multi--source-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-real_time-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-NOAA-00CED1?style=flat-square)

🔗 [NOAA MADIS](https://madis.ncep.noaa.gov/)

</details>

<details>
<summary><b>NOAA ISD</b> · Integrated Surface Database</summary>

![Coverage](https://img.shields.io/badge/Coverage-20k+_stations-blue?style=flat-square)
![Variables](https://img.shields.io/badge/Variables-hourly_multi--element-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1901~present-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-NCEI-00CED1?style=flat-square)

Hourly observations integrated from global surface stations (temp, dewpoint, wind, pressure, visibility, present weather, etc.).

🔗 [NOAA ISD](https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database)

</details>

<details>
<summary><b>Iowa Environmental Mesonet</b> · Multi-source meteo aggregator</summary>

![Coverage](https://img.shields.io/badge/Coverage-mainly_US-blue?style=flat-square)
![Variables](https://img.shields.io/badge/Variables-ASOS/NWS/radar-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-near_real_time-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-IEM-00BFFF?style=flat-square)

Aggregates ASOS/METAR, NWS alerts, radar mosaics, road weather, etc.; offers convenient archives and APIs.

🔗 [IEM](https://mesonet.agron.iastate.edu/)

</details>

#### Upper-air Observations

<details>
<summary><b>IGRA</b> · Global radiosonde</summary>

![Coverage](https://img.shields.io/badge/Coverage-global-blue?style=flat-square)
![Levels](https://img.shields.io/badge/Levels-standard-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-2x_daily-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-NOAA-00CED1?style=flat-square)

🔗 [NOAA IGRA](https://www.ncei.noaa.gov/data/integrated-global-radiosonde-archive/)

</details>

<details>
<summary><b>AMDAR</b> · Global aircraft-based observations</summary>

![Coverage](https://img.shields.io/badge/Coverage-global_air_routes-blue?style=flat-square)
![Levels](https://img.shields.io/badge/Levels-flight_levels-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-real_time-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-WMO-9CF?style=flat-square)

🔗 [WMO AMDAR](https://community.wmo.int/en/activity-areas/aircraft-based-observations)

</details>

#### Automatic Weather Stations

<details>
<summary><b>MesoWest</b> · US regional networks</summary>

![Scale](https://img.shields.io/badge/Scale-thousands-blue?style=flat-square)
![Region](https://img.shields.io/badge/Region-US-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-MesoWest-00BFFF?style=flat-square)

🔗 [MesoWest](https://mesowest.utah.edu/)

</details>

<details>
<summary><b>Weather Underground</b> · Global personal stations</summary>

![Scale](https://img.shields.io/badge/Scale-global_personal-blue?style=flat-square)
![Region](https://img.shields.io/badge/Region-global-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-WUnderground-00BFFF?style=flat-square)

🔗 [WUnderground](https://www.wunderground.com/)

</details>

### Satellite

#### Geostationary Satellites

<details>
<summary><b>Himawari-8/9</b> · JMA · Asia-Pacific</summary>

![Product](https://img.shields.io/badge/Product-imagery/aerosol-blue?style=flat-square)
![Coverage](https://img.shields.io/badge/Coverage-Asia_Pacific-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-JAXA-9CF?style=flat-square)

🔗 [JAXA](https://www.eorc.jaxa.jp/ptree/)

</details>

<details>
<summary><b>GOES-16/18</b> · NOAA · Americas</summary>

![Product](https://img.shields.io/badge/Product-multichannel-blue?style=flat-square)
![Coverage](https://img.shields.io/badge/Coverage-Americas-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-NOAA-00CED1?style=flat-square)

🔗 [NOAA STAR GOES](https://www.star.nesdis.noaa.gov/goes/)

</details>

<details>
<summary><b>FY-4A/4B</b> · CMA · Asia</summary>

![Product](https://img.shields.io/badge/Product-imagery/precip-blue?style=flat-square)
![Coverage](https://img.shields.io/badge/Coverage-Asia-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-NSMC-9CF?style=flat-square)

🔗 [NSMC](http://satellite.nsmc.org.cn/)

</details>

#### Polar-orbiting Satellites

<details>
<summary><b>Suomi NPP</b> · NASA/NOAA</summary>

![Resolution](https://img.shields.io/badge/Resolution-750m-blue?style=flat-square)
![Product](https://img.shields.io/badge/Product-VIIRS-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-NASA-FF0000?style=flat-square)

🔗 [NASA LAADS](https://ladsweb.modaps.eosdis.nasa.gov/)

</details>

<details>
<summary><b>JPSS</b> · NOAA</summary>

![Resolution](https://img.shields.io/badge/Resolution-375m-blue?style=flat-square)
![Product](https://img.shields.io/badge/Product-multispectral-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-NOAA-00CED1?style=flat-square)

🔗 [NOAA STAR JPSS](https://www.star.nesdis.noaa.gov/jpss/)

</details>

<details>
<summary><b>MODIS</b> · NASA Terra/Aqua atmospheric products</summary>

![Resolution](https://img.shields.io/badge/Resolution-250m~1km-blue?style=flat-square)
![Product](https://img.shields.io/badge/Product-aerosol/cloud/WV-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-NASA-FF0000?style=flat-square)

Terra/Aqua MODIS atmospheric products (aerosol optical depth, cloud properties, water vapor, etc.).

🔗 [NASA LAADS DAAC](https://ladsweb.modaps.eosdis.nasa.gov/)

</details>

#### Satellite Precipitation Products

<details>
<summary><b>GPM IMERG</b> · Global precipitation</summary>

![Spatial Res](https://img.shields.io/badge/Spatial_Res-0.1°-blue?style=flat-square)
![Temporal Res](https://img.shields.io/badge/Temporal_Res-30min-green?style=flat-square)
![Coverage](https://img.shields.io/badge/Coverage-global-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-NASA-FF0000?style=flat-square)

🔗 [NASA GES DISC](https://disc.gsfc.nasa.gov/)

</details>

<details>
<summary><b>CMORPH</b> · Global precipitation</summary>

![Spatial Res](https://img.shields.io/badge/Spatial_Res-0.25°-blue?style=flat-square)
![Temporal Res](https://img.shields.io/badge/Temporal_Res-30min-green?style=flat-square)
![Coverage](https://img.shields.io/badge/Coverage-global-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-NOAA-00CED1?style=flat-square)

🔗 [CPC](https://www.cpc.ncep.noaa.gov/products/janowiak/cmorph_description.html)

</details>

### Radar

#### Weather Radar

<details>
<summary><b>NEXRAD</b> · US weather radar network</summary>

![Coverage](https://img.shields.io/badge/Coverage-US-blue?style=flat-square)
![Product](https://img.shields.io/badge/Product-basedata/products-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-NOAA-00CED1?style=flat-square)

🔗 [NOAA NCEI](https://www.ncdc.noaa.gov/nexradinv/)

</details>

<details>
<summary><b>OPERA</b> · European radar network</summary>

![Coverage](https://img.shields.io/badge/Coverage-Europe-blue?style=flat-square)
![Product](https://img.shields.io/badge/Product-composite-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-EUMETNET-9CF?style=flat-square)

🔗 [EUMETNET](https://www.eumetnet.eu/activities/observations-programme/current-activities/opera/)

</details>

### Air Quality

#### Air Quality Monitoring

<details>
<summary><b>AirNow</b> · US air quality</summary>

![Coverage](https://img.shields.io/badge/Coverage-US-blue?style=flat-square)
![Pollutants](https://img.shields.io/badge/Pollutants-major-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-AirNow-00BFFF?style=flat-square)

🔗 [AirNow](https://www.airnow.gov/)

</details>

<details>
<summary><b>OpenAQ</b> · Global air quality</summary>

![Coverage](https://img.shields.io/badge/Coverage-global-blue?style=flat-square)
![Pollutants](https://img.shields.io/badge/Pollutants-multi-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-OpenAQ-00BFFF?style=flat-square)

🔗 [OpenAQ](https://openaq.org/)

</details>

<details>
<summary><b>EPA AirData</b> · US outdoor air quality</summary>

![Coverage](https://img.shields.io/badge/Coverage-US-blue?style=flat-square)
![Pollutants](https://img.shields.io/badge/Pollutants-PM2.5/O3/SO2/NO2/CO-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-EPA-00BFFF?style=flat-square)

Hourly/daily air quality from the EPA monitoring network, including historical archive downloads.

🔗 [EPA AirData](https://www.epa.gov/outdoor-air-quality-data)

</details>

<details>
<summary><b>WAQI</b> · World Air Quality Index</summary>

![Coverage](https://img.shields.io/badge/Coverage-global-blue?style=flat-square)
![Pollutants](https://img.shields.io/badge/Pollutants-PM2.5/PM10/AQI-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-WAQI-00BFFF?style=flat-square)

Aggregates real-time AQI from thousands of global stations; provides an API and historical queries.

🔗 [WAQI](https://waqi.info/)

</details>

<details>
<summary><b>EEA Air Quality</b> · European air quality</summary>

![Coverage](https://img.shields.io/badge/Coverage-Europe-blue?style=flat-square)
![Pollutants](https://img.shields.io/badge/Pollutants-PM/NO2/O3/SO2-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-EEA-003399?style=flat-square)

Hourly air quality observations and historical archives from EEA member-state stations.

🔗 [EEA Air Index](https://airindex.eea.europa.eu/)

</details>

#### Air Quality Modeling

<details>
<summary><b>CAMS</b> · ECMWF global air quality forecast</summary>

![Resolution](https://img.shields.io/badge/Resolution-0.4°-blue?style=flat-square)
![Product](https://img.shields.io/badge/Product-global_AQ_forecast-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-CAMS-00CED1?style=flat-square)

🔗 [CAMS](https://atmosphere.copernicus.eu/)

</details>


## Marine Data

### Marine Observations

<details>
<summary><b>Argo</b> · Profiling float observations</summary>

![Platform](https://img.shields.io/badge/Platform-profiling_floats-blue?style=flat-square)
![Variables](https://img.shields.io/badge/Variables-CTD-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-Argo-00BFFF?style=flat-square)

🔗 [Argo GDAC](https://argo.ucsd.edu/data/argo-data/)

</details>

<details>
<summary><b>TAO/TRITON</b> · Moored buoy array</summary>

![Platform](https://img.shields.io/badge/Platform-moored_buoys-blue?style=flat-square)
![Variables](https://img.shields.io/badge/Variables-marine_meteo-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-NOAA-00CED1?style=flat-square)

🔗 [PMEL](https://www.pmel.noaa.gov/tao/)

</details>

<details>
<summary><b>NDBC</b> · National Data Buoy Center</summary>

![Platform](https://img.shields.io/badge/Platform-buoys/coastal-blue?style=flat-square)
![Variables](https://img.shields.io/badge/Variables-wind/wave/SST/pressure-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-NOAA-00CED1?style=flat-square)

Real-time and historical marine meteorological observations from US coastal and global buoys/stations.

🔗 [NOAA NDBC](https://www.ndbc.noaa.gov/)

</details>

<details>
<summary><b>WOD</b> · World Ocean Database ocean profiles</summary>

![Platform](https://img.shields.io/badge/Platform-CTD/XBT/Argo-blue?style=flat-square)
![Variables](https://img.shields.io/badge/Variables-T/S/O2/nutrients-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1772~present-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-NCEI-00CED1?style=flat-square)

The world's largest ocean profile database maintained by NCEI, integrating historical T/S/chemistry observations.

🔗 [NCEI WOD](https://www.ncei.noaa.gov/products/world-ocean-database)

</details>

### SST & Sea Ice

<details>
<summary><b>OISST v2</b> · High-res sea surface temperature + sea ice concentration · OPeNDAP</summary>

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Temporal Res](https://img.shields.io/badge/Temporal_Res-daily-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1981--present-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-PSL_THREDDS-00CED1?style=flat-square)

`sst` and `icec` share a 0.25° grid; a 1° monthly version also exists. Daily data split by year.

🔗 📂 [Catalog](https://psl.noaa.gov/thredds/catalog/Datasets/noaa.oisst.v2.highres/catalog.html) · OPeNDAP `https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.oisst.v2.highres/sst.day.mean.2024.nc` · 📝 [Script](./sources/download_from_opendap.py)

</details>

<details>
<summary><b>ERSST</b> · Reconstructed SST (v3/v4/v5/v6) · OPeNDAP</summary>

![Resolution](https://img.shields.io/badge/Resolution-2.0°-blue?style=flat-square)
![Temporal Res](https://img.shields.io/badge/Temporal_Res-monthly-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1854--present-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-PSL_THREDDS-00CED1?style=flat-square)

Observation-reconstructed global SST, with v3/v4/v5/v6 (v6 recommended).

🔗 📂 [Catalog](https://psl.noaa.gov/thredds/catalog/Datasets/noaa.ersst.v6/catalog.html) · OPeNDAP (v3–v6, change version) `https://psl.noaa.gov/thredds/dodsC/Datasets/noaa.ersst.v6/sst.mnmean.nc` · 📝 [Script](./sources/download_from_opendap.py)

</details>

<details>
<summary><b>COBE / COBE2</b> · JMA sea surface temperature · OPeNDAP</summary>

![Resolution](https://img.shields.io/badge/Resolution-1.0°-blue?style=flat-square)
![Temporal Res](https://img.shields.io/badge/Temporal_Res-monthly-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1850--present-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-PSL_THREDDS-00CED1?style=flat-square)

JMA long-term historical SST reconstruction (COBE2 current, COBE predecessor).

🔗 📂 [COBE2 catalog](https://psl.noaa.gov/thredds/catalog/Datasets/COBE2/catalog.html) · [COBE catalog](https://psl.noaa.gov/thredds/catalog/Datasets/COBE/catalog.html) · OPeNDAP `https://psl.noaa.gov/thredds/dodsC/Datasets/COBE2/sst.mon.mean.nc` · 📝 [Script](./sources/download_from_opendap.py)

</details>

<details>
<summary><b>Kaplan SST</b> · Reconstructed SST anomaly · OPeNDAP</summary>

![Resolution](https://img.shields.io/badge/Resolution-5.0°-blue?style=flat-square)
![Temporal Res](https://img.shields.io/badge/Temporal_Res-monthly-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1856--present-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-PSL_THREDDS-00CED1?style=flat-square)

Coarse-grid (5°) SST anomaly reconstruction, suited to long-term trend studies.

🔗 📂 [Catalog](https://psl.noaa.gov/thredds/catalog/Datasets/kaplan_sst/catalog.html) · OPeNDAP `https://psl.noaa.gov/thredds/dodsC/Datasets/kaplan_sst/sst.mon.anom.nc` · 📝 [Script](./sources/download_from_opendap.py)

</details>

<details>
<summary><b>CoastWatch IMS Sea Ice</b> · Arctic snow/sea ice 1km · OPeNDAP</summary>

![Resolution](https://img.shields.io/badge/Resolution-1km-blue?style=flat-square)
![Temporal Res](https://img.shields.io/badge/Temporal_Res-15day-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-2006~2020-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-CoastWatch-00CED1?style=flat-square)

IMS (Interactive Multisensor Snow and Ice Mapping) product hosted on NOAA CoastWatch ERDDAP, `IMS_mean`.

🔗 [IMS 1km sea ice](https://coastwatch.noaa.gov/erddap/griddap/ims1k_15day_baseline_stats) · 📝 [Script](./sources/download_from_opendap.py)

</details>

### Marine Models

<details>
<summary><b>HYCOM</b> · US Navy ocean model</summary>

![Resolution](https://img.shields.io/badge/Resolution-1/12°-blue?style=flat-square)
![Product](https://img.shields.io/badge/Product-ocean_analysis/forecast-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-HYCOM-00BFFF?style=flat-square)

🔗 [HYCOM project](https://www.hycom.org/) · [THREDDS data catalog](https://tds.hycom.org/thredds/catalog.html)

</details>

<details>
<summary><b>CMEMS</b> · EU marine monitoring & forecasting</summary>

![Resolution](https://img.shields.io/badge/Resolution-multiple-blue?style=flat-square)
![Product](https://img.shields.io/badge/Product-marine_monitoring/forecast-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-Copernicus-003399?style=flat-square)

🔗 [Copernicus Marine](https://marine.copernicus.eu/)

</details>

### Ocean Color

<details>
<summary><b>Sentinel-3</b> · ESA · ocean color</summary>

![Resolution](https://img.shields.io/badge/Resolution-300m-blue?style=flat-square)
![Product](https://img.shields.io/badge/Product-ocean_color-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-ESA-003399?style=flat-square)

🔗 [Copernicus Data Space](https://dataspace.copernicus.eu/)

</details>

<details>
<summary><b>NASA OB.DAAC</b> · Ocean color</summary>

![Resolution](https://img.shields.io/badge/Resolution-1km~4km-blue?style=flat-square)
![Product](https://img.shields.io/badge/Product-chl/transparency/SST-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-NASA-FF0000?style=flat-square)

MODIS-Aqua / Sentinel-3 / OC-CCI ocean color products (chlorophyll-a, transparency, inherent optical properties).

🔗 [NASA OceanColor](https://oceancolor.gsfc.nasa.gov/)

</details>

<details>
<summary><b>CoastWatch ERDDAP</b> · NOAA coastal data</summary>

![Resolution](https://img.shields.io/badge/Resolution-multiple-blue?style=flat-square)
![Product](https://img.shields.io/badge/Product-chl/SST/ice-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-CoastWatch-00CED1?style=flat-square)

NOAA CoastWatch ERDDAP server providing ocean color, SST, sea ice and other gridded data (griddap browsable/downloadable).

🔗 [CoastWatch ERDDAP](https://coastwatch.noaa.gov/erddap/index.html)

</details>

## Open Source Tools

<div align="center">

<i>The companion download toolkit for this project is [Open Earth Data Kit](https://github.com/wait4xx/open-earth-data-kit) (unified CLI · catalog · multi-protocol adapters). Below is a curated selection of community tools for each stage, covering data download → format processing → physical analysis → visualization.</i>

</div>

---

#### 🔽 Data Download & Access

| Tool | Function | ⭐ Stars | 📅 Last Update |
|:-----|:-----|:-------:|:----------:|
| [**cdsapi**](https://github.com/ecmwf/cdsapi) | ECMWF Climate Data Store official API (ERA5 etc.) | ![GitHub Stars](https://img.shields.io/github/stars/ecmwf/cdsapi?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/ecmwf/cdsapi?style=flat-square) |
| [**ecmwf-opendata**](https://github.com/ecmwf/ecmwf-opendata) | ECMWF real-time open data (IFS / EFS / AIFS) | ![GitHub Stars](https://img.shields.io/github/stars/ecmwf/ecmwf-opendata?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/ecmwf/ecmwf-opendata?style=flat-square) |
| [**Herbie**](https://github.com/blaylockbk/Herbie) | Download NOAA HRRR / GFS model data | ![GitHub Stars](https://img.shields.io/github/stars/blaylockbk/Herbie?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/blaylockbk/Herbie?style=flat-square) |
| [**Siphon**](https://github.com/Unidata/siphon) | THREDDS / OPeNDAP remote data access | ![GitHub Stars](https://img.shields.io/github/stars/Unidata/siphon?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/Unidata/siphon?style=flat-square) |
| [**satpy**](https://github.com/pytroll/satpy) | Multi-source satellite data reading & calibration | ![GitHub Stars](https://img.shields.io/github/stars/pytroll/satpy?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/pytroll/satpy?style=flat-square) |

#### 📊 Gridded Data Processing

| Tool | Function | ⭐ Stars | 📅 Last Update |
|:-----|:-----|:-------:|:----------:|
| [**xarray**](https://github.com/pydata/xarray) | NetCDF / GRIB multi-dim array processing (de-facto standard) | ![GitHub Stars](https://img.shields.io/github/stars/pydata/xarray?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/pydata/xarray?style=flat-square) |
| [**cfgrib**](https://github.com/ecmwf/cfgrib) | Map GRIB onto xarray datasets | ![GitHub Stars](https://img.shields.io/github/stars/ecmwf/cfgrib?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/ecmwf/cfgrib?style=flat-square) |
| [**netCDF4**](https://github.com/Unidata/netcdf4-python) | Classic NetCDF read/write library | ![GitHub Stars](https://img.shields.io/github/stars/Unidata/netcdf4-python?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/Unidata/netcdf4-python?style=flat-square) |
| [**pygrib**](https://github.com/jswhit/pygrib) | GRIB1 / GRIB2 read/write | ![GitHub Stars](https://img.shields.io/github/stars/jswhit/pygrib?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/jswhit/pygrib?style=flat-square) |
| [**dask**](https://github.com/dask/dask) | Large-scale parallel computing (xarray backend) | ![GitHub Stars](https://img.shields.io/github/stars/dask/dask?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/dask/dask?style=flat-square) |

#### 🌡️ Meteorological Analysis & Computation

| Tool | Function | ⭐ Stars | 📅 Last Update |
|:-----|:-----|:-------:|:----------:|
| [**MetPy**](https://github.com/Unidata/MetPy) | Meteorological computation, analysis & visualization | ![GitHub Stars](https://img.shields.io/github/stars/Unidata/MetPy?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/Unidata/MetPy?style=flat-square) |
| [**WRF-python**](https://github.com/NCAR/wrf-python) | WRF post-processing diagnostic computation | ![GitHub Stars](https://img.shields.io/github/stars/NCAR/wrf-python?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/NCAR/wrf-python?style=flat-square) |
| [**xwrf**](https://github.com/xarray-contrib/xwrf) | WRF data xarray post-processing | ![GitHub Stars](https://img.shields.io/github/stars/xarray-contrib/xwrf?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/xarray-contrib/xwrf?style=flat-square) |
| [**tropycal**](https://github.com/tropycal/tropycal) | Tropical cyclone tracking & analysis | ![GitHub Stars](https://img.shields.io/github/stars/tropycal/tropycal?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/tropycal/tropycal?style=flat-square) |

#### 📡 Radar Data Processing

| Tool | Function | ⭐ Stars | 📅 Last Update |
|:-----|:-----|:-------:|:----------:|
| [**Py-ART**](https://github.com/ARM-DOE/pyart) | Weather radar data processing (ARM) | ![GitHub Stars](https://img.shields.io/github/stars/ARM-DOE/pyart?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/ARM-DOE/pyart?style=flat-square) |
| [**wradlib**](https://github.com/wradlib/wradlib) | Radar data retrieval & analysis | ![GitHub Stars](https://img.shields.io/github/stars/wradlib/wradlib?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/wradlib/wradlib?style=flat-square) |
| [**ACT**](https://github.com/ARM-DOE/ACT) | ARM Atmospheric data Toolkit | ![GitHub Stars](https://img.shields.io/github/stars/ARM-DOE/ACT?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/ARM-DOE/ACT?style=flat-square) |

#### 🎨 Visualization & Mapping

| Tool | Function | ⭐ Stars | 📅 Last Update |
|:-----|:-----|:-------:|:----------:|
| [**Cartopy**](https://github.com/SciTools/cartopy) | Map projection & geographic plotting | ![GitHub Stars](https://img.shields.io/github/stars/SciTools/cartopy?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/SciTools/cartopy?style=flat-square) |
| [**proplot**](https://github.com/proplot-dev/proplot) | Publication-quality scientific plotting | ![GitHub Stars](https://img.shields.io/github/stars/proplot-dev/proplot?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/proplot-dev/proplot?style=flat-square) |
| [**geoviews**](https://github.com/holoviz/geoviews) | Interactive geographic visualization | ![GitHub Stars](https://img.shields.io/github/stars/holoviz/geoviews?style=flat-square&logo=github) | ![Last Commit](https://img.shields.io/github/last-commit/holoviz/geoviews?style=flat-square) |

## Contributing

<div align="center">

All forms of contribution are welcome and appreciated! See [**CONTRIBUTING_EN.md**](CONTRIBUTING_EN.md) for detailed guidelines.

> 💡 **Where to contribute**: To add or fix **data sources, access notes and other guide content**, open an Issue / PR in [this repo](https://github.com/wait4xx/open-earth-data-guide); to improve the **`meteo` CLI, download adapters and backends**, head over to [Open Earth Data Kit](https://github.com/wait4xx/open-earth-data-kit).

<br/>

[![Report Issues](https://img.shields.io/badge/Report_Issues-Issues-e05d44?style=for-the-badge&logo=github)](https://github.com/wait4xx/open-earth-data-guide/issues)
[![Add Resources](https://img.shields.io/badge/Add_Resources-Pull_Request-2962ff?style=for-the-badge&logo=github)](https://github.com/wait4xx/open-earth-data-guide/pulls)
[![Share Use Cases](https://img.shields.io/badge/Share_Use_Cases-Discussions-9CF?style=for-the-badge&logo=github)](https://github.com/wait4xx/open-earth-data-guide/discussions)

<br/>

**📋 Submission Checklist**

`✓ Valid links`　`✓ Clear descriptions`　`✓ Consistent format`　`✓ Note license`

</div>

---

## License

<div align="center">

![License: MIT](https://img.shields.io/github/license/wait4xx/open-earth-data-guide?style=for-the-badge&logo=github)

This repository is open-sourced under the **MIT License**, which applies to the **guide content and download scripts** in this repo.

</div>

> ⚠️ **Important distinction**: The MIT license covers only this repository's own content and code; the third-party data sources linked in the list (ERA5, NOAA, CMEMS, etc.) **each have their own independent terms and licenses**. Please review and comply with the respective data provider's terms before using the data. This repository holds no ownership of any data.

---

## Acknowledgements

<div align="center">

Thanks to the following data-providing institutions and to every developer who has contributed to this project ✨

<br/>

![CMA](https://img.shields.io/badge/CMA-China_Meteorological_Admin.-blue?style=flat-square)
![NOAA](https://img.shields.io/badge/NOAA-USA-blue?style=flat-square)
![ECMWF](https://img.shields.io/badge/ECMWF-Europe-orange?style=flat-square)
![NASA](https://img.shields.io/badge/NASA-USA-red?style=flat-square)
![ESA](https://img.shields.io/badge/ESA-Europe-purple?style=flat-square)
![NCEI](https://img.shields.io/badge/NCEI-NOAA-00CED1?style=flat-square)
![DWD](https://img.shields.io/badge/DWD-Germany-9CF?style=flat-square)
![Met Office](https://img.shields.io/badge/Met_Office-UK-00BFFF?style=flat-square)
![JMA](https://img.shields.io/badge/JMA-Japan-9CF?style=flat-square)
![Copernicus](https://img.shields.io/badge/Copernicus-EU-003399?style=flat-square)

<br/>

![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=flat-square&logo=googlecloud&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-FF9900?style=flat-square&logo=amazonaws&logoColor=white)

</div>

---

<div align="center">

<h3>💖 Support This Project</h3>

If this repository helps you, please Star, Fork, or share it with your peers!

<br/>

[![GitHub Stars](https://img.shields.io/github/stars/wait4xx/open-earth-data-guide?style=for-the-badge&logo=github)](https://github.com/wait4xx/open-earth-data-guide/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/wait4xx/open-earth-data-guide?style=for-the-badge&logo=github)](https://github.com/wait4xx/open-earth-data-guide/network/members)
[![GitHub Watchers](https://img.shields.io/github/watchers/wait4xx/open-earth-data-guide?style=for-the-badge&logo=github)](https://github.com/wait4xx/open-earth-data-guide/watchers)
[![Discussions](https://img.shields.io/badge/Discussions-share_use_cases-9CF?style=for-the-badge&logo=github)](https://github.com/wait4xx/open-earth-data-guide/discussions)

</div>

---

<div align="center">

<h3>📈 Star History</h3>

<a href="https://star-history.com/#wait4xx/open-earth-data-guide&Date">
<img src="https://api.star-history.com/svg?repos=wait4xx/open-earth-data-guide&type=Date" alt="Star History" width="600">
</a>

</div>

---

<div align="center">

<sub>🔄 Data links and availability may change over time · If you find a broken link or want to recommend a new resource, let us know via <a href="https://github.com/wait4xx/open-earth-data-guide/issues">Issues</a></sub>

<br/><br/>

<sub><b>Made with ❤️ for the meteorology community</b> · Data availability is subject to each provider</sub>

</div>
