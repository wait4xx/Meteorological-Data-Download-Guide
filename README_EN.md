# 🌤️ Public Meteorological Data Download Resources

**[中文](README.md)** | **[English](README_EN.md)**

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](CONTRIBUTING.md)
[![GitHub Stars](https://img.shields.io/github/stars/wait4xx/Meteorological-Data-Download-Guide.svg?style=flat-square)](https://github.com/wait4xx/Meteorological-Data-Download-Guide)
[![GitHub Forks](https://img.shields.io/github/forks/wait4xx/Meteorological-Data-Download-Guide.svg?style=flat-square)](https://github.com/wait4xx/Meteorological-Data-Download-Guide)
[![Status](https://img.shields.io/badge/Status-Active-blue.svg?style=flat-square)](https://github.com/wait4xx/Meteorological-Data-Download-Guide)

> A curated collection of public meteorological data download sources, aimed at providing convenient data access for meteorological research, data analysis, and application development.

---

### 📢 Latest Updates
> **2026-05-21** · 📝 Added Planette ERA5 AWS S3 download script for ERA5 daily, weekly, and monthly mean data (`era5_planette_downloader.py`), supporting multi-variable concurrency, unit conversion, real-time progress
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

| Category | Status |
|:---------|:------:|
| Numerical Weather Prediction | ✅ |
| AI Model Forecasts | ✅ |
| Reanalysis Data | ✅ |
| Real-time Observations | 🔜 |
| Satellite Data | 🔜 |
| Radar Data | 🔜 |
| Climate Data | 🔜 |
| Marine Meteorology | 🔜 |
| Air Quality Data | 🔜 |
| Open Source Tools | 🔜 |

---

## 📚 Contents

| Data Types | Tools & Community |
|:----------:|:-----------------:|
| [NWP](#numerical-weather-prediction) · [AI Models](#ai-model-forecasts) · [Reanalysis](#climate--reanalysis) | [Contributing](#contributing) · [License](#license) |
| [Observations](#observation-data) · [Marine](#marine-meteorology) · [Air Quality](#air-quality-data) | [Open Source Tools](#open-source-tools) |
| [Satellite](#satellite-data) · [Radar](#radar-data) | [Acknowledgements](#acknowledgements) |


## Numerical Weather Prediction

### Real-time Forecasts

<details>
<summary><b>ECMWF</b> · European Centre for Medium-Range Weather Forecasts</summary>

---

**IFS** · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~144h(3h)_144~360h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-每日4次-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-官方-9CF?style=flat-square)

🔗 [ECMWF Open Data](https://data.ecmwf.int/forecasts/) · 📅 Last 4 days

---

**EFS** · Ensemble Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~144h(3h)_144~360h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-每日4次-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-官方-9CF?style=flat-square)

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
![Update](https://img.shields.io/badge/Update-每日4次-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-UCAR-800080?style=flat-square)

🔗 [GFS_UCAR](https://motherlode.ucar.edu/native/grid/NCEP/GFS/) · 📅 Last 3 months

---

**GFS** · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~120h(1h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-每日4次-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-OpeNDAP-00BFFF?style=flat-square)

🔗 [GFS_OpeNDAP](https://nomads.ncep.noaa.gov/dods/gfs_0p25_1hr/) · 📅 Last 10 days · 📝 [Python/xarray Example](./sources/download_from_opendap.py)

---

**GFS** · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~384h(3h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-每日4次-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-OpeNDAP-00BFFF?style=flat-square)

🔗 [GFS_OpeNDAP](https://nomads.ncep.noaa.gov/dods/gfs_0p25/) · 📅 Last 10 days · 📝 [Python/xarray Example](./sources/download_from_opendap.py)

---

**GFS** · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~120h(1h)_120~384h(3h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-每日4次-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-NOAA-00CED1?style=flat-square)

🔗 [GFS_NOAA](https://nomads.ncep.noaa.gov/pub/data/nccf/com/gfs/) · 📅 Last 10 days

---

**GFS** · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.5°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~384h(3h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-每日4次-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-OpeNDAP-00BFFF?style=flat-square)

🔗 [GFS_OpeNDAP](https://nomads.ncep.noaa.gov/dods/gfs_0p50/) · 📅 Last 10 days · 📝 [Python/xarray Example](./sources/download_from_opendap.py)

---

**GFS** · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-1°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~384h(3h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-每日4次-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-OpeNDAP-00BFFF?style=flat-square)

🔗 [GFS_OpeNDAP](https://nomads.ncep.noaa.gov/dods/gfs_1p00/) · 📅 Last 10 days · 📝 [Python/xarray Example](./sources/download_from_opendap.py)

---

**GEFS** · Ensemble Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~240h(3h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-每日4次-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-NOAA-00CED1?style=flat-square)

🔗 [GEFS_NOAA](https://nomads.ncep.noaa.gov/pub/data/nccf/com/gens/) · 📅 Last 4 days

---

**GEFS** · Ensemble Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.5°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~240h(3h)_240~840h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-每日4次-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-NOAA-00CED1?style=flat-square)

🔗 [GEFS_NOAA](https://nomads.ncep.noaa.gov/pub/data/nccf/com/gens/) · 📅 Last 4 days

</details>

<details>
<summary><b>DWD</b> · German Weather Service</summary>

---

**ICON** · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.125°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~144h(3h)_144~360h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-每日4次-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-官方-9CF?style=flat-square)

🔗 [ICON Open Data](https://opendata.dwd.de/weather/nwp/icon/grib/) · 📅 Last 4 runs

</details>

<details>
<summary><b>JMA</b> · Japan Meteorological Agency (Account registration required)</summary>

---

**GSM** · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°/0.5°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~144h(3h)_144~360h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-每日4次-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-官方-9CF?style=flat-square)

🔗 [JMA GSM](https://www.wis-jma.go.jp/cms/gsm/download.html) · 📅 Last 5 days

</details>


### Historical Forecasts

<details>
<summary><b>ECMWF</b> · European Centre for Medium-Range Weather Forecasts</summary>

---

**IFS (HRES ~ Surface)** · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.1°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~12h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-每日4次-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-UCAR-800080?style=flat-square)

🔗 [IFS_UCAR](https://gdex.ucar.edu/datasets/d113001/dataaccess/#) · 📅 From Jan 1, 2016 to present

---

**IFS** · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°/0.4°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~144h(3h)_144~360h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-每日4次-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-Google-4285F4?style=flat-square)
![VPN](https://img.shields.io/badge/VPN-√-3126F0?style=flat-square)

🔗 [🪜 ECMWF_GOOGLE](https://console.cloud.google.com/storage/browser/ecmwf-open-data) · 📅 From Jul 12, 2023 to present (with delay)

---

**IFS** · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°/0.4°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~144h(3h)_144~360h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-每日4次-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://ecmwf-forecasts.s3.amazonaws.com/) · 📅 From Mar 18, 2023 to present · ⚠️ Requires awscli or complete URL

---

**EFS** · Ensemble Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°/0.4°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~144h(3h)_144~360h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-每日4次-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-Google-4285F4?style=flat-square)
![VPN](https://img.shields.io/badge/VPN-√-3126F0?style=flat-square)

🔗 [🪜 ECMWF_GOOGLE](https://console.cloud.google.com/storage/browser/ecmwf-open-data) · 📅 From Jul 12, 2023 to present (with delay)

---

**EFS** · Ensemble Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°/0.4°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~144h(3h)_144~360h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-每日4次-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://ecmwf-forecasts.s3.amazonaws.com/) · 📅 From Mar 18, 2023 to present · ⚠️ Requires awscli or complete URL

</details>

<details>
<summary><b>NCEP</b> · Global Forecast System (USA)</summary>

---

**GFS** · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°/0.5°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~240h(3h)_240~384h(12h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-每日4次-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-UCAR-800080?style=flat-square)

🔗 [GFS_UCAR](https://gdex.ucar.edu/datasets/d084001/dataaccess/) · 📅 From Jan 15, 2015 to present (discontinued in 2026)

---

**GFS** · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°/0.5°/1°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~384h(3h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-每日4次-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-gfs-bdp-pds.s3.amazonaws.com/index.html) · 📅 From Jan 1, 2021 to present · 🔍 Search `gfs`

---

**GFS** · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°/0.5°/1°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~384h(3h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-每日4次-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-Google-4285F4?style=flat-square)
![VPN](https://img.shields.io/badge/VPN-√-3126F0?style=flat-square)

🔗 [🪜 GFS_GOOGLE](https://console.cloud.google.com/storage/browser/global-forecast-system) · 📅 From Jan 1, 2021 to present · 🔍 Search `gfs`

---

**GEFS** · Ensemble Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°/0.5°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~384h(6h)_0~240h(3h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-每日4次-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-gefs-pds.s3.amazonaws.com/index.html) · 📅 From Jan 1, 2017 to present

---

**GEFS** · Ensemble Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°/0.5°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~240h(3h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-每日4次-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-Google-4285F4?style=flat-square)
![VPN](https://img.shields.io/badge/VPN-√-3126F0?style=flat-square)

🔗 [🪜 GFS_GOOGLE](https://console.cloud.google.com/storage/browser/gfs-ensemble-forecast-system) · 📅 From Sep 25, 2020 to present

</details>

## AI Model Forecasts

### Real-time Data

<details>
<summary><b>ECMWF</b> · European Centre for Medium-Range Weather Forecasts</summary>

---

**AIFS** · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~360h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-每日4次-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-官方-9CF?style=flat-square)

🔗 [ECMWF Open Data](https://data.ecmwf.int/forecasts/) · 📅 Last 4 days

---

**AIEFS** · Ensemble Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~360h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-每日4次-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-官方-9CF?style=flat-square)

🔗 [ECMWF Open Data](https://data.ecmwf.int/forecasts/) · 📅 Last 4 days

</details>

<details>
<summary><b>NCEP</b> · Global Forecast System (USA)</summary>

---

**AIGFS** · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°/0.5°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~360h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-每日4次-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-NOAA-00CED1?style=flat-square)

🔗 [AIGFS_NOAA](https://nomads.ncep.noaa.gov/pub/data/nccf/com/aigfs/) · 📅 Last 2 days

---

**AIGEFS** · Ensemble Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°/0.5°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~360h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-每日4次-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-NOAA-00CED1?style=flat-square)

🔗 [AIGEFS_NOAA](https://nomads.ncep.noaa.gov/pub/data/nccf/com/aigefs/) · 📅 Last 2 days

</details>

<details>
<summary><b>AI Model Collection</b> · Aurora / FourCastNet / GraphCast / PANGU</summary>

---

**Aurora** · Microsoft · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.5°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~240h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-每日2次-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) · 📝 [Data Guide](./docs/noaa-oar-mlwp-data.txt)

---

**FourCastNet** · NVIDIA · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.5°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~240h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-每日2次-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) · 📝 [Data Guide](./docs/noaa-oar-mlwp-data.txt)

---

**GraphCast** · Google / DeepMind · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.5°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~240h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-每日2次-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) · 📝 [Data Guide](./docs/noaa-oar-mlwp-data.txt)

---

**PANGU** · Huawei · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.5°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~240h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-每日2次-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) · 📝 [Data Guide](./docs/noaa-oar-mlwp-data.txt)

</details>

### Historical Data

<details>
<summary><b>ECMWF</b> · European Centre for Medium-Range Weather Forecasts</summary>

---

**AIFS** · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~360h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-每日4次-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://ecmwf-forecasts.s3.amazonaws.com/) · 📅 From Feb 29, 2024 to present · ⚠️ Requires awscli or complete URL

---

**AIEFS** · Ensemble Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~360h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-每日4次-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://ecmwf-forecasts.s3.amazonaws.com/) · ⚠️ Requires awscli or complete URL

</details>

<details>
<summary><b>AI Model Collection</b> · Aurora / FourCastNet / GraphCast / PANGU</summary>

---

**Aurora** · Microsoft · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.5°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~240h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-每日2次-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) · 📅 From Jan 23, 2025 to present · 📝 [Data Guide](./docs/noaa-oar-mlwp-data.txt)

---

**FourCastNet** · NVIDIA · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.5°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~240h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-每日2次-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) · 📅 From Sep 30, 2020 to present · 📝 [Data Guide](./docs/noaa-oar-mlwp-data.txt)

---

**GraphCast** · Google / DeepMind · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.5°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~240h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-每日2次-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) · 📅 From Sep 30, 2020 to present · 📝 [Data Guide](./docs/noaa-oar-mlwp-data.txt)

---

**PANGU** · Huawei · Deterministic Forecast

![Resolution](https://img.shields.io/badge/Resolution-0.5°-blue?style=flat-square)
![Range](https://img.shields.io/badge/Range-0~240h(6h)-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-每日2次-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://noaa-oar-mlwp-data.s3.amazonaws.com/index.html) · 📅 From Sep 30, 2020 to present · 📝 [Data Guide](./docs/noaa-oar-mlwp-data.txt)

</details>

## Climate & Reanalysis

### Reanalysis Datasets

<details>
<summary><b>ERA5-land</b> · ECMWF Surface Reanalysis</summary>

***Without VPN, downloading via AWS + IDM multi-threaded is recommended for the fastest speed***

---

**ERA5-land (hourly)**

![Resolution](https://img.shields.io/badge/Resolution-0.1°-blue?style=flat-square)
![Temporal](https://img.shields.io/badge/Temporal-hourly-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1950年至今-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-CDS-00CED1?style=flat-square)

🔗 [ERA5-land](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-land?tab=download)

---

**ERA5-land (hourly)**

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Temporal](https://img.shields.io/badge/Temporal-hourly-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1940年至今-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://nsf-ncar-era5.s3.amazonaws.com/index.html#e5.oper.an.sfc/) · 📅 Data delayed 3-4 months · 📝 [Python multi-threaded download script](./sources/s3_downloader_multi.py)

<details>
<summary>📖 s3_downloader_multi.py Tutorial</summary>

---

**Script Overview**

`s3_downloader_multi.py` is an intelligent concurrent download script for AWS S3 ERA5 data. It leverages IDM or XDM for multi-task parallel downloading, supporting resume, byte-level verification, and automatic skipping of completed files.

**Dependencies**

```bash
pip install requests beautifulsoup4 lxml
```

Also requires one of the following download tools:
- **IDM** (Windows, recommended): [Internet Download Manager](https://www.internetdownloadmanager.com/)
- **XDM** (cross-platform): [Xtreme Download Manager](https://xtremedownloadmanager.com/)

**Configure Download Tool Path**

Open the script and modify the paths in the `Config` class:

```python
class Config:
    DOWNLOAD_TOOL = "idm"   # or "xdm"
    IDM_PATH = r"D:\Program Files (x86)\Internet Download Manager\IDMan.exe"
    XDM_PATH_LINUX  = "/opt/xdman/xdman"
    XDM_PATH_WINDOWS = r"C:\Program Files\XDM\xdman.exe"
```

---

**Command-line Mode (Recommended)**

```bash
python s3_downloader_multi.py -v <variables> -y <year_range> -o <output_dir> [options]
```

| Parameter | Description | Example |
|-----------|-------------|---------|
| `-v` | Variable name(s), comma-separated for multiple | `2t` / `2t,10u,10v` |
| `-y` | Year range, single year or interval | `2024` / `2020-2024` |
| `-m` | Month(s), comma-separated (default: all year) | `1,2,3` |
| `-o` | Local output directory | `./era5_data` |
| `-t` | Download tool, `idm` or `xdm` (default: `idm`) | `idm` |
| `-c` | Maximum concurrent downloads (default: 6) | `4` |
| `--dry-run` | Preview mode, no actual download | — |
| `--export` | Export file list as CSV/TXT | — |
| `--delay` | Data delay in months (default: 5) | `3` |

**Examples**

```bash
# Preview 2024 2m temperature data (no download)
python s3_downloader_multi.py -v 2t -y 2024 -o ./era5_data --dry-run --export

# Download 2023-2024 2m temperature + 10m wind, 6 concurrent threads
python s3_downloader_multi.py -v 2t,10u,10v -y 2023-2024 -o ./era5_data -c 6

# Download only Jun-Aug 2024 surface pressure
python s3_downloader_multi.py -v sp -y 2024 -m 6,7,8 -o ./era5_data
```

---

**Code Invocation Mode**

Modify `RUN_MODE` and `CODE_PARAMS` in the `Config` class at the top of the script, then run directly:

```python
class Config:
    RUN_MODE = "code"   # Switch to code mode
    CODE_PARAMS = {
        "variables":      ["2t", "10u"],   # Variable list
        "start_year":     2023,
        "end_year":       2024,
        "months":         [6, 7, 8],       # None means all year
        "output_dir":     "./era5_data",
        "dry_run":        False,
        "export_preview": True,
        "preview_file":   "preview_list.csv",
    }
```

---

**Supported Variables**

| Variable Code | Description |
|---------------|-------------|
| `2t` | 2m temperature |
| `2d` | 2m dewpoint temperature |
| `10u` | 10m zonal wind (u) |
| `10v` | 10m meridional wind (v) |
| `sp` | Surface pressure |
| `msl` | Mean sea level pressure |
| `tp` | Total precipitation |
| `skt` | Skin temperature |
| `sd` | Snow depth |
| `ssr` | Surface solar radiation |
| `str` | Surface thermal radiation |
| `...` | ... |

**Notes**

- Data is typically delayed by about **3-5 months**; the script automatically skips unpublished months
- Downloads are managed by IDM/XDM; the script checks local file sizes to determine completion
- Logs are automatically written to `download_log.txt` in the current directory
- Fully downloaded files (byte count >= expected * 99%) are automatically skipped; resume is supported

</details>

---

**ERA5-land (monthly)**

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Temporal](https://img.shields.io/badge/Temporal-monthly_mean-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1950年至今-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-CDS-00CED1?style=flat-square)

🔗 [ERA5-land (monthly)](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-land-monthly-means?tab=download)

---

**ERA5-land (daily/7-day/monthly/3-month)**

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Temporal](https://img.shields.io/badge/Temporal-hourly-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1940年至今-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://planette-era5.s3.amazonaws.com/index.html#era5/) · 📅 Data delayed 3-4 months · Data in zarr format · 📝 [Python Download Script](./sources/era5_planette_downloader.py)

<details>
<summary>📖 era5_planette_downloader.py Tutorial</summary>

---

**Overview**

`era5_planette_downloader.py` is a download script for AWS S3 Planette ERA5 data. It supports multi-variable concurrent download, automatic unit conversion, spatial/temporal subsetting, and real-time progress display.

**Dependencies**

```bash
pip install xarray icechunk s3fs numpy netcdf4 requests dask
```

**Usage**

```bash
python era5_planette_downloader.py -v <variable> -f <frequency> -o <output> [options]
```

| Option | Description | Example |
|--------|-------------|---------|
| `-v` | Variable name(s), supports multiple | `t2m` / `t2m tp slp` |
| `-f` | Time frequency | `day` / `7day` / `month` / `3month` |
| `-g` | Grid resolution (default: 0p25latx0p25lon) | `0p25latx0p25lon` |
| `-t` | Time range (YYYY-MM-DD) | `2020-01-01 2024-12-31` |
| `-r` | Spatial region (lon_min lon_max lat_min lat_max) | `70 140 15 55` |
| `-o` | Output file or directory (directory for multi-variable) | `./t2m.nc` / `./output/` |
| `--format` | Output format (default: netcdf4) | `netcdf4` / `zarr` |
| `--auto-name` | Auto-generate filenames | — |
| `--concurrent` | Download variables concurrently | — |
| `--workers` | Concurrent download threads (default: 4) | `8` |
| `--no-convert` | Disable unit conversion | — |
| `--no-compress` | Disable compression (faster export) | — |
| `--no-validate` | Skip data validation | — |
| `--list-variables` | List available S3 variables | — |
| `--list-tree` | Show variable data tree | — |

**Examples**

```bash
# List available variables
python era5_planette_downloader.py --list-variables

# Download monthly 2m temperature (2020-2024)
python era5_planette_downloader.py -v t2m -f month -t 2020-01-01 2024-12-31 -o ./t2m_monthly.nc

# Download and crop to a region
python era5_planette_downloader.py -v t2m -f month -t 2020-01-01 2020-12-31 -r 70 140 15 55 -o ./t2m_china.nc

# Multi-variable concurrent download with auto-naming
python era5_planette_downloader.py -v t2m tp slp -f month -t 2020-01-01 2024-12-31 -o ./output/ --auto-name --concurrent

# Export as Zarr
python era5_planette_downloader.py -v t2m -f day -o ./t2m.zarr --format zarr
```

**Supported Variables**

| Variable | Description | Unit Conversion |
|----------|-------------|-----------------|
| `t2m` | 2m Temperature | K → °C |
| `d2m` | 2m Dewpoint Temperature | K → °C |
| `sst` | Sea Surface Temperature | K → °C |
| `tp` | Total Precipitation | m → mm |
| `sp` | Surface Pressure | Pa → hPa |
| `msl` | Mean Sea Level Pressure | Pa → hPa |
| `slp` | Sea Level Pressure | Pa → hPa |
| `u10m` | 10m U-component Wind | m/s |
| `v10m` | 10m V-component Wind | m/s |
| `u850` | 850hPa U-component Wind | m/s |
| `v850` | 850hPa V-component Wind | m/s |
| `t850` | 850hPa Temperature | K → °C |
| `z500` | 500hPa Geopotential Height | m²/s² → dagpm |
| `r500` | 500hPa Relative Humidity | % |
| `...` | ... | |

**Notes**

- Data is in **Icechunk Zarr** format, accessed via the Icechunk library on S3 — different from direct GRIB/NetCDF downloads
- Download speed is affected by network latency and Icechunk protocol overhead — **larger datasets are more efficient**
- Output is standard **NetCDF4** or **Zarr** format, compatible with `xarray`

</details>

---

**ERA5 (hourly/monthly)**

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Temporal](https://img.shields.io/badge/Temporal-hourly/monthly-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1940年至今-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-Google-4285F4?style=flat-square)
![VPN](https://img.shields.io/badge/VPN-√-3126F0?style=flat-square)

🔗 [🪜 ERA5_GOOGLE](https://console.cloud.google.com/storage/browser/gcp-public-data-arco-era5/raw/ERA5GRIB/HRES)

</details>

<details>
<summary><b>ERA5-pressure</b> · ECMWF Pressure-level Reanalysis</summary>

***Without VPN, downloading via AWS + IDM multi-threaded is recommended for the fastest speed***

---

**ERA5-pressure (hourly)**

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Temporal](https://img.shields.io/badge/Temporal-hourly-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1940年至今-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-CDS-00CED1?style=flat-square)

🔗 [ERA5-pressure](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-pressure-levels?tab=download)

---

**ERA5-pressure (hourly)**

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Temporal](https://img.shields.io/badge/Temporal-hourly-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1940年至今-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://nsf-ncar-era5.s3.amazonaws.com/index.html#e5.oper.an.pl/) · 📅 Data delayed 3-4 months · 📝 [Python multi-threaded download script](./sources/s3_downloader_multi.py) (change `DATASET_PREFIX` to `e5.oper.an.pl`)

---

**ERA5-pressure (monthly)**

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Temporal](https://img.shields.io/badge/Temporal-monthly_mean-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1940年至今-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-CDS-00CED1?style=flat-square)

🔗 [ERA5-pressure (monthly)](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-pressure-levels-monthly-means?tab=download)

---

**ERA5-pressure (daily/7-day/monthly/3-month)**

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Temporal](https://img.shields.io/badge/Temporal-hourly-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1940年至今-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-AWS-FF9900?style=flat-square)

🔗 [AWS-S3](https://planette-era5.s3.amazonaws.com/index.html#era5/) · 📅 Data delayed 3-4 months · Data in zarr format · 📝 [Python Download Script](./sources/era5_planette_downloader.py)

---

**ERA5 (hourly/monthly)**

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Temporal](https://img.shields.io/badge/Temporal-hourly/monthly-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1940年至今-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-Google-4285F4?style=flat-square)
![VPN](https://img.shields.io/badge/VPN-√-3126F0?style=flat-square)

🔗 [🪜 ERA5_GOOGLE](https://console.cloud.google.com/storage/browser/gcp-public-data-arco-era5/raw/ERA5GRIB/HRES)

</details>


<details>
<summary><b>FNL</b> · NCEP Final Analysis</summary>

---

**FNL**

![Resolution](https://img.shields.io/badge/Resolution-0.25°-blue?style=flat-square)
![Temporal](https://img.shields.io/badge/Temporal-6_hourly-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-2015年至今-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-UCAR-800080?style=flat-square)

🔗 [FNL_UCAR](https://gdex.ucar.edu/datasets/d083003/dataaccess/#)

---

**FNL**

![Resolution](https://img.shields.io/badge/Resolution-1°-blue?style=flat-square)
![Temporal](https://img.shields.io/badge/Temporal-6_hourly-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1999年至今-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-UCAR-800080?style=flat-square)

🔗 [FNL_UCAR](https://gdex.ucar.edu/datasets/d083002/dataaccess/#)

</details>

<details>
<summary><b>JRA-3Q</b> · JMA Reanalysis</summary>

---

**DIAS**

![Resolution](https://img.shields.io/badge/Resolution-1.25°-blue?style=flat-square)
![Temporal](https://img.shields.io/badge/Temporal-hourly/monthly_mean-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1947年至今-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-DIAS-9CF?style=flat-square)

🔗 [JRA-3Q_DIAS](https://data.diasjp.net/dl/storages/filelist/dataset:645) · ⚠️ Login required

---

**UCAR (historical)**

![Resolution](https://img.shields.io/badge/Resolution-1.25°-blue?style=flat-square)
![Temporal](https://img.shields.io/badge/Temporal-hourly-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1947年至今-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-UCAR-800080?style=flat-square)

🔗 [JRA-3Q_UCAR](https://gdex.ucar.edu/datasets/d640000/dataaccess/#)

---

**UCAR (near-real)**

![Resolution](https://img.shields.io/badge/Resolution-1.25°-blue?style=flat-square)
![Temporal](https://img.shields.io/badge/Temporal-hourly-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-2023年至今-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-UCAR-800080?style=flat-square)

🔗 [JRA-3Q_UCAR](https://gdex.ucar.edu/datasets/d640001/dataaccess/#) · 🔄 Near real-time

---

**UCAR (monthly)**

![Resolution](https://img.shields.io/badge/Resolution-1.25°-blue?style=flat-square)
![Temporal](https://img.shields.io/badge/Temporal-monthly_mean-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1947年至今-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-UCAR-800080?style=flat-square)

🔗 [JRA-3Q_UCAR](https://gdex.ucar.edu/datasets/d640002/dataaccess/#)

</details>

<details>
<summary><b>MERRA-2</b> · NASA Reanalysis</summary>

![Resolution](https://img.shields.io/badge/Resolution-0.5°-blue?style=flat-square)
![Temporal](https://img.shields.io/badge/Temporal-hourly/monthly-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1980年至今-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-NASA-FF0000?style=flat-square)

🔗 [MERRA_GSFC](https://disc.gsfc.nasa.gov/datasets?project=MERRA-2) · [MERRA_FTP](https://goldsmr4.gesdisc.eosdis.nasa.gov/data/)

</details>

### Climate Datasets

<details>
<summary><b>CRU TS</b> · Gridded Observations</summary>

![Type](https://img.shields.io/badge/Type-格点化观测-blue?style=flat-square)
![Resolution](https://img.shields.io/badge/Resolution-0.5°-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1901~now-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-UEA-00BFFF?style=flat-square)

🔗 [UEA](https://crudata.uea.ac.uk/cru/data/hrg/)

</details>

<details>
<summary><b>GPCC</b> · Precipitation Dataset</summary>

![Type](https://img.shields.io/badge/Type-降水-blue?style=flat-square)
![Resolution](https://img.shields.io/badge/Resolution-0.25°~2.5°-green?style=flat-square)
![Period](https://img.shields.io/badge/Period-1891~now-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-DWD-00BFFF?style=flat-square)

🔗 [DWD](https://www.dwd.de/EN/ourservices/gpcc/gpcc.html)

</details>


## Observation Data

### Surface Observations

<details>
<summary><b>ASOS/AWOS</b> · Global Airport Observations</summary>

![Coverage](https://img.shields.io/badge/Coverage-全球机场-blue?style=flat-square)
![Elements](https://img.shields.io/badge/Elements-多要素-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-实时-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-NOAA-00CED1?style=flat-square)

🔗 [NOAA](https://www.ncei.noaa.gov/maps/hourly/)

</details>

<details>
<summary><b>SYNOP</b> · Global Surface Observations</summary>

![Coverage](https://img.shields.io/badge/Coverage-全球-blue?style=flat-square)
![Elements](https://img.shields.io/badge/Elements-基本气象要素-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-3/6小时-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-OGIMET-00BFFF?style=flat-square)

🔗 [OGIMET](https://www.ogimet.com/)

</details>

<details>
<summary><b>MADIS</b> · North American Multi-source Data</summary>

![Coverage](https://img.shields.io/badge/Coverage-北美-blue?style=flat-square)
![Elements](https://img.shields.io/badge/Elements-多源数据-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-实时-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-NOAA-00CED1?style=flat-square)

🔗 [NOAA MADIS](https://madis.ncep.noaa.gov/)

</details>

### Upper-air Observations

<details>
<summary><b>IGRA</b> · Global Sounding</summary>

![Coverage](https://img.shields.io/badge/Coverage-全球-blue?style=flat-square)
![Levels](https://img.shields.io/badge/Levels-标准层-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-每日2次-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-NOAA-00CED1?style=flat-square)

🔗 [NOAA IGRA](https://www.ncei.noaa.gov/access/weather/igra/)

</details>

<details>
<summary><b>AMDAR</b> · Global Aircraft Observations</summary>

![Coverage](https://img.shields.io/badge/Coverage-全球航线-blue?style=flat-square)
![Levels](https://img.shields.io/badge/Levels-飞行层-green?style=flat-square)
![Update](https://img.shields.io/badge/Update-实时-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-WMO-9CF?style=flat-square)

🔗 [WMO AMDAR](https://amdar.wmo.int/)

</details>

### Automatic Weather Stations

<details>
<summary><b>MesoWest</b> · US Regional Station Network</summary>

![Scale](https://img.shields.io/badge/Scale-数千站-blue?style=flat-square)
![Region](https://img.shields.io/badge/Region-美国-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-MesoWest-00BFFF?style=flat-square)

🔗 [MesoWest](https://mesowest.utah.edu/)

</details>

<details>
<summary><b>Weather Underground</b> · Global Personal Stations</summary>

![Scale](https://img.shields.io/badge/Scale-全球个人站-blue?style=flat-square)
![Region](https://img.shields.io/badge/Region-全球-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-WUnderground-00BFFF?style=flat-square)

🔗 [WUnderground](https://www.wunderground.com/)

</details>

## Satellite Data

### Geostationary Satellites

<details>
<summary><b>Himawari-8/9</b> · JMA · Asia-Pacific</summary>

![Products](https://img.shields.io/badge/Products-云图/气溶胶-blue?style=flat-square)
![Coverage](https://img.shields.io/badge/Coverage-亚太-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-JAXA-9CF?style=flat-square)

🔗 [JAXA](https://www.eorc.jaxa.jp/ptree/)

</details>

<details>
<summary><b>GOES-16/18</b> · NOAA · Americas</summary>

![Products](https://img.shields.io/badge/Products-多通道图像-blue?style=flat-square)
![Coverage](https://img.shields.io/badge/Coverage-美洲-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-NOAA-00CED1?style=flat-square)

🔗 [NOAA GOES](https://www.noaa.gov/goes-16-and-goes-17-satellite-data)

</details>

<details>
<summary><b>FY-4A/4B</b> · CMA · Asia</summary>

![Products](https://img.shields.io/badge/Products-云图/降水-blue?style=flat-square)
![Coverage](https://img.shields.io/badge/Coverage-亚洲-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-NSMC-9CF?style=flat-square)

🔗 [NSMC](http://satellite.nsmc.org.cn/)

</details>

### Polar-orbiting Satellites

<details>
<summary><b>Suomi NPP</b> · NASA/NOAA</summary>

![Resolution](https://img.shields.io/badge/Resolution-750m-blue?style=flat-square)
![Products](https://img.shields.io/badge/Products-VIIRS数据-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-NASA-FF0000?style=flat-square)

🔗 [NASA LAADS](https://ladsweb.modaps.eosdis.nasa.gov/)

</details>

<details>
<summary><b>JPSS</b> · NOAA</summary>

![Resolution](https://img.shields.io/badge/Resolution-375m-blue?style=flat-square)
![Products](https://img.shields.io/badge/Products-多光谱数据-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-NOAA-00CED1?style=flat-square)

🔗 [NOAA CLASS](https://www.avl.class.noaa.gov/)

</details>

<details>
<summary><b>Sentinel-3</b> · ESA</summary>

![Resolution](https://img.shields.io/badge/Resolution-300m-blue?style=flat-square)
![Products](https://img.shields.io/badge/Products-海洋颜色-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-ESA-003399?style=flat-square)

🔗 [Copernicus](https://scihub.copernicus.eu/)

</details>

### Satellite Precipitation Products

<details>
<summary><b>GPM IMERG</b> · Global Precipitation</summary>

![Spatial](https://img.shields.io/badge/Spatial-0.1°-blue?style=flat-square)
![Temporal](https://img.shields.io/badge/Temporal-30分钟-green?style=flat-square)
![Coverage](https://img.shields.io/badge/Coverage-全球-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-NASA-FF0000?style=flat-square)

🔗 [NASA GES DISC](https://disc.gsfc.nasa.gov/)

</details>

<details>
<summary><b>CMORPH</b> · Global Precipitation</summary>

![Spatial](https://img.shields.io/badge/Spatial-0.25°-blue?style=flat-square)
![Temporal](https://img.shields.io/badge/Temporal-30分钟-green?style=flat-square)
![Coverage](https://img.shields.io/badge/Coverage-全球-orange?style=flat-square)
![Source](https://img.shields.io/badge/Source-NOAA-00CED1?style=flat-square)

🔗 [CPC](https://www.cpc.ncep.noaa.gov/products/janowiak/cmorph_description.html)

</details>

## Radar Data

### Weather Radar

<details>
<summary><b>NEXRAD</b> · US Weather Radar Network</summary>

![Coverage](https://img.shields.io/badge/Coverage-美国-blue?style=flat-square)
![Products](https://img.shields.io/badge/Products-基数据/产品-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-NOAA-00CED1?style=flat-square)

🔗 [NOAA NCEI](https://www.ncdc.noaa.gov/nexradinv/)

</details>

<details>
<summary><b>OPERA</b> · European Radar Network</summary>

![Coverage](https://img.shields.io/badge/Coverage-欧洲-blue?style=flat-square)
![Products](https://img.shields.io/badge/Products-合成产品-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-EUMETNET-9CF?style=flat-square)

🔗 [EUMETNET](https://www.eumetnet.eu/activities/observations-programme/current-activities/opera/)

</details>


## Marine Meteorology

### Ocean Observations

<details>
<summary><b>Argo</b> · Profiling Float Observations</summary>

![Platform](https://img.shields.io/badge/Platform-剖面浮标-blue?style=flat-square)
![Elements](https://img.shields.io/badge/Elements-温盐深-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-Argo-00BFFF?style=flat-square)

🔗 [Argo GDAC](https://argo.ucsd.edu/data/argo-data/)

</details>

<details>
<summary><b>TAO/TRITON</b> · Moored Buoy Array</summary>

![Platform](https://img.shields.io/badge/Platform-锚定浮标-blue?style=flat-square)
![Elements](https://img.shields.io/badge/Elements-海洋气象-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-NOAA-00CED1?style=flat-square)

🔗 [PMEL](https://www.pmel.noaa.gov/tao/)

</details>

### Ocean Models

<details>
<summary><b>HYCOM</b> · US Navy Ocean Model</summary>

![Resolution](https://img.shields.io/badge/Resolution-1/12°-blue?style=flat-square)
![Products](https://img.shields.io/badge/Products-海洋分析预报-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-HYCOM-00BFFF?style=flat-square)

🔗 [HYCOM](https://www.hycom.org/)

</details>

<details>
<summary><b>CMEMS</b> · EU Marine Monitoring and Forecasting</summary>

![Resolution](https://img.shields.io/badge/Resolution-多种-blue?style=flat-square)
![Products](https://img.shields.io/badge/Products-海洋监测预报-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-Copernicus-003399?style=flat-square)

🔗 [Copernicus Marine](https://marine.copernicus.eu/)

</details>

## Air Quality Data

### Air Quality Monitoring

<details>
<summary><b>AirNow</b> · US Air Quality</summary>

![Coverage](https://img.shields.io/badge/Coverage-美国-blue?style=flat-square)
![Pollutants](https://img.shields.io/badge/Pollutants-主要污染物-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-AirNow-00BFFF?style=flat-square)

🔗 [AirNow](https://www.airnow.gov/)

</details>

<details>
<summary><b>OpenAQ</b> · Global Air Quality</summary>

![Coverage](https://img.shields.io/badge/Coverage-全球-blue?style=flat-square)
![Pollutants](https://img.shields.io/badge/Pollutants-多种污染物-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-OpenAQ-00BFFF?style=flat-square)

🔗 [OpenAQ](https://openaq.org/)

</details>

### Air Quality Models

<details>
<summary><b>CAMS</b> · ECMWF Global Air Quality Forecast</summary>

![Resolution](https://img.shields.io/badge/Resolution-0.4°-blue?style=flat-square)
![Products](https://img.shields.io/badge/Products-全球空气质量预报-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-CAMS-00CED1?style=flat-square)

🔗 [CAMS](https://atmosphere.copernicus.eu/)

</details>

## Open Source Tools

### Data Download & Processing

<details>
<summary><b>Herbie</b> · Python · GFS/HRRR Data Download</summary>

![Language](https://img.shields.io/badge/Language-Python-blue?style=flat-square)
![Function](https://img.shields.io/badge/Function-GFS/HRRR数据下载-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-GitHub-9CF?style=flat-square)

🔗 [GitHub](https://github.com/blaylockbk/Herbie)

</details>

<details>
<summary><b>Siphon</b> · Python · Remote Data Access</summary>

![Language](https://img.shields.io/badge/Language-Python-blue?style=flat-square)
![Function](https://img.shields.io/badge/Function-远程数据访问-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-Unidata-9CF?style=flat-square)

🔗 [Unidata](https://github.com/Unidata/siphon)

</details>

<details>
<summary><b>cfgrib</b> · Python · GRIB File Processing</summary>

![Language](https://img.shields.io/badge/Language-Python-blue?style=flat-square)
![Function](https://img.shields.io/badge/Function-GRIB文件处理-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-ECMWF-00CED1?style=flat-square)

🔗 [ECMWF](https://github.com/ecmwf/cfgrib)

</details>

### Visualization & Analysis

<details>
<summary><b>MetPy</b> · Python · Meteorological Data Analysis & Visualization</summary>

![Language](https://img.shields.io/badge/Language-Python-blue?style=flat-square)
![Function](https://img.shields.io/badge/Function-气象数据分析可视化-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-Unidata-9CF?style=flat-square)

🔗 [Unidata](https://github.com/Unidata/MetPy)

</details>

<details>
<summary><b>Cartopy</b> · Python · Map Plotting</summary>

![Language](https://img.shields.io/badge/Language-Python-blue?style=flat-square)
![Function](https://img.shields.io/badge/Function-地图制图-green?style=flat-square)
![Source](https://img.shields.io/badge/Source-SciTools-9CF?style=flat-square)

🔗 [SciTools](https://github.com/SciTools/cartopy)

</details>

## Contributing

We welcome and appreciate all forms of contribution! Please refer to [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

### Ways to Contribute

| 🐛 Report Issues | 📦 Add Resources | 📝 Improve Docs | 💬 Share Use Cases |
|:----------------:|:----------------:|:---------------:|:-----------------:|
| Feedback via [Issues](https://github.com/wait4xx/Meteorological-Data-Download-Guide/issues) | Submit a Pull Request | Help improve or translate | Share in Discussions |

### Submission Guidelines

> ✓ Links must be valid and publicly accessible · ✓ Clear data descriptions · ✓ Follow existing category format · ✓ Note any license restrictions

## License

> ⚠️ Data sources listed in this repository may have their own terms of use and license agreements. Please review and comply with the respective data provider's policies before use.

## Acknowledgements

Thanks to all data provider organizations and developers who have contributed to this project!

<div align="center">

![CMA](https://img.shields.io/badge/CMA-China_Meteorological_Administration-blue?style=flat-square)
![NOAA](https://img.shields.io/badge/NOAA-National_Oceanic_and_Atmospheric_Administration-green?style=flat-square)
![ECMWF](https://img.shields.io/badge/ECMWF-European_Centre_for_Medium-Range_Weather_Forecasts-orange?style=flat-square)
![ESA](https://img.shields.io/badge/ESA-European_Space_Agency-purple?style=flat-square)
![NASA](https://img.shields.io/badge/NASA-National_Aeronautics_and_Space_Administration-red?style=flat-square)
![Google Cloud](https://img.shields.io/badge/Google-Cloud-4285F4?style=flat-square)
![AWS](https://img.shields.io/badge/AWS-Amazon-FF9900?style=flat-square)

</div>

---

> ⚠️ **Note**: Data links and availability may change over time. If you find broken links or want to recommend new resources, please let us know via [Issues](https://github.com/wait4xx/Meteorological-Data-Download-Guide/issues).

<div align="center">

**⭐ If this project is helpful to you, please give us a star!**

</div>
