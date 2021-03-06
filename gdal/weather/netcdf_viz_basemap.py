from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

nc_file = 'F:\\GIS_DATA\\weather\\2019030600_003.nc'
ds = Dataset(nc_file, mode='r')

# print(fh.variables)

# get variable value
lons = ds.variables['longitude'][:]
lats = ds.variables['latitude'][:]
tmax = ds.variables['TMAX_2maboveground'][:]
tmax_units = ds.variables['TMAX_2maboveground'].units

# lon, lat mean
lon_0 = lons.min()
lon_1 = lons.max()
lat_0 = lats.min()
lat_1 = lats.max()

# lat 0-60, lon 70-140
# m = Basemap(lat_0 = lat_0, lon_0 = lon_0)
m = Basemap(llcrnrlon=lon_0, llcrnrlat=lat_0, urcrnrlon=lon_1, urcrnrlat=lat_1)
lon, lat = np.meshgrid(lons, lats)
xi, yi = m(lon, lat)

# plot data
cs = m.pcolor(xi, yi, np.squeeze(tmax))

# grid lines
m.drawparallels(np.arange(-90., 91., 20.), labels=[1,0,0,0], fontsize=10)
m.drawmeridians(np.arange(-180., 181., 40.), labels=[0,0,0,1], fontsize=10)

m.drawcoastlines()
m.drawstates()
m.drawcountries()

# Add Colorbar
cbar = m.colorbar(cs, location='bottom', pad="10%")
cbar.set_label(tmax_units)

# Add Title
plt.title('Maximum Temperature')

plt.show()
ds.close()
