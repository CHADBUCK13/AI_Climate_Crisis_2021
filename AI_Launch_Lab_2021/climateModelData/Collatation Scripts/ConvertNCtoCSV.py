import netCDF4 as nc
from netCDF4 import num2date
import numpy as np
import os
import pandas as pd
 
#Manual change based on import NC file data
dataName = 'rsds'

#Open netCDF4 file
f = nc.Dataset(r'')

for var in f.variables:
    print(var)

#Extract variable
variable = f.variables[dataName]
 
#Get variable dimensions and names
time_dim, lat_dim, lon_dim = variable.get_dims()
time_var = f.variables[time_dim.name]
times = num2date(time_var[:], time_var.units)
latitudes = f.variables[lat_dim.name][:]
longitudes = f.variables[lon_dim.name][:]
 
#Read dataframe to CSV based on dataname
output_dir = './'
filename = os.path.join(output_dir, dataName +'.csv')
print(f'Writing data in tabular form to {filename} (this may take some time)...')
times_grid, latitudes_grid, longitudes_grid = [
    x.flatten() for x in np.meshgrid(times, latitudes, longitudes, indexing='ij')]
df = pd.DataFrame({
    'time': [t.isoformat() for t in times_grid],
    'latitude': latitudes_grid,
    'longitude': longitudes_grid,
    dataName : variable[:].flatten()})
df.to_csv(filename, index=False)
print('Done')
