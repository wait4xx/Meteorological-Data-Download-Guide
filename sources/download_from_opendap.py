'''
Author: wait4x
Date: 2025-12-03 19:49:56
FilePath: \Meteorological-Data-Download-Guide\sources\download_from_opendap.py
'''

"""
从OPeNDAP下载数据
这只是一个简单示例，非完整的下载脚本，请根据自己的实际需求进行修改。
"""

import xarray as xr

if __name__ == "__main__":
    # OPeNDAP URL
    # 将该字段“/gfs_0p25_1hr/gfs20251125/gfs_0p25_1hr_00z”替换为数据集的URL
    url = "https://nomads.ncep.noaa.gov/dods/gfs_0p25_1hr/gfs20251125/gfs_0p25_1hr_00z"
    url = "https://nomads.ncep.noaa.gov/dods/gefs/gefs20251202/gep01_00z_pgrb2a"

    # 打开数据集（懒加载，不立即下载全部）
    ds = xr.open_dataset(url)
    print(ds)

    # 选择变量和区域（关键：先子集再下载）
    subset = ds['tmp2m'].sel(lat=slice(-10, 10), lon=slice(0, 30))

    # 将子集下载到内存并保存为本地 NetCDF
    subset.load().to_netcdf("local_data.nc")

    # 释放内存
    del ds, subset