# coding=utf-8

import plotly
import plotly.plotly as py
from plotly.graph_objs import *
import numpy as np
from scipy.io import netcdf

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
# System.loadLibrary("mkl_rt")
m = Basemap(width=12000000, height=9000000, projection='lcc',
            resolution=None, lat_1=45., lat_2=55, lat_0=50, lon_0=-107.)
m.bluemarble()
plt.show()
