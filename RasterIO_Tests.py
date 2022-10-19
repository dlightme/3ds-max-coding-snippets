# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 08:29:22 2022

@author: w.haak
"""

import rasterio
from rasterio.plot import show

def main():
    fp = r'C:\Users\w.haak\Downloads\GIS\LIDAR\P_12150\DSM_TQ1580_P_12150_20201204_20210221.tif'
    img = rasterio.open(fp)
    show(img)


if __name__ == "__main__":
    main()