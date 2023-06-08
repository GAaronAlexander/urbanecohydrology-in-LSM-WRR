import xarray as xr
import numpy as np
import scipy as sci
import matplotlib.pyplot as plt 
import matplotlib.colors as colors
import pandas as pd
import matplotlib.patches as patches
import matplotlib.lines as lines
from cmcrameri import cm
import os as os
import seaborn as sns 


sns.set_style('ticks')


save_loc = '../../data/extract_data_share_tree/season_heatfluxes/'

data_file_name = '201804010000.LDASOUT_DOMAIN1'
data_location = '/Volumes/Untitled/Integragting_LID_into_LSM/three_season_long_simulations_correct/three_season_share_tree_additional/'
data_directory_list = sorted([i for i in os.listdir(data_location) if 'share_tree' in i])
ticks = np.linspace(0,70,71)
nums = np.linspace(0,35,71)

ticks_y = np.linspace(0,185,186)


# c = cm.rainbow(np.linspace(0, 1, 8))
print(data_directory_list)
new_data =  xr.open_dataset(data_location+data_directory_list[0]+'/'+data_file_name)
d = pd.date_range(start='2018-03-31 18:00:00',end='2020-10-31 18:00:00', freq='5T')
analysis_time = pd.date_range(start='2018-04-30 18:00:00',end='2018-10-31 18:00:00', freq='5T')

days = pd.date_range(start='2019-04-30',end='2019-10-31', freq='D')



new_data = new_data.assign_coords(Time=d)
new_data = new_data.sel(Time=analysis_time)

rain = new_data.RAINRATE[:,0,0]
rain = rain.resample(Time='D').sum()

rain_marker = rain.where(rain > 5,0)
rain_marker = rain_marker.where(rain_marker == 0,1)

thing = []
print(rain_marker[0].values)
for i in range(185):
	if rain_marker[int(i)].values == 1.0:
		thing.append(r'$\bigstar$')
	else:
		thing.append('')

heat_flux = (new_data.LH[:,0,0]*50/100 + new_data.LH[:,0,1]*50/100)*300 # now in j/m^2
sens_flux = (new_data.HFX[:,0,0]*50/100 + new_data.HFX[:,0,1]*50/100)*300 # now in j/m^2
grou_flux = (new_data.GRDFLX[:,0,0]*50/100 + new_data.GRDFLX[:,0,1]*50/100)*300 # now in j/m^2

heat_flux = pd.Series(data=heat_flux.values,index=analysis_time)


sens_flux= pd.Series(data=sens_flux.values,index=analysis_time)




heat_flux_day = heat_flux.resample('D').sum()
heat_flux_day = heat_flux_day*(1000)/(10**9) #now in Mjoules

sens_flux_day = sens_flux.resample('D').sum()
sens_flux_day = sens_flux_day*(1000)/(10**9) #now in Mjoules



data_final_LH = np.empty((185,71))
data_final_H = np.empty((185,71))
data_final_diff_LH = np.empty((185,71))
data_final_diff_H = np.empty((185,71))


data_final_LH[:,0] = heat_flux_day
data_final_H[:,0] = sens_flux_day
data_final_diff_LH[:,0] = heat_flux_day - heat_flux_day
data_final_diff_H[:,0] = sens_flux_day - sens_flux_day

for i in range(1,71):

# 	# create a figure
	print(i)
	print(data_directory_list[i])
	data_loop = xr.open_dataset(data_location+data_directory_list[i]+'/'+data_file_name)

	

	data = data_loop.assign_coords(Time=d)
	data = data.sel(Time=analysis_time)

	heat_flux_l = (data.LH[:,0,1]*50/100 + data.LH[:,0,0]*((i/2)/100) + new_data.LH[:,0,0]*((100-i)/2)/100)*300 # now in j/m^2
	sens_flux_l = (data.HFX[:,0,1]*50/100 + data.HFX[:,0,0]*((i/2)/100) + new_data.HFX[:,0,0]*((100-i)/2)/100)*300 # now in j/m^2

	heat_flux_l = pd.Series(data=heat_flux_l.values,index=analysis_time)


	sens_flux_l = pd.Series(data=sens_flux_l.values,index=analysis_time)
	

	heat_flux_day_l = heat_flux_l.resample('D').sum()
	heat_flux_day_l = heat_flux_day_l*(1000)/(10**9) #now in Gjoules

	sens_flux_day_l = sens_flux_l.resample('D').sum()
	sens_flux_day_l = sens_flux_day_l*(1000)/(10**9) #now in Gjoules

	data_final_LH[:,i] = heat_flux_day_l
	data_final_H[:,i] = sens_flux_day_l


	data_final_diff_LH[:,i] = (heat_flux_day_l - heat_flux_day)
	data_final_diff_H[:,i] = (sens_flux_day_l - sens_flux_day)
	
	
np.savetxt(save_loc+'extracted_H_data_2018_all.csv',data_final_H,delimiter=',')
np.savetxt(save_loc+'extracted_H_data_difference_2018_all.csv',data_final_diff_H,delimiter=',')

np.savetxt(save_loc+'extracted_LH_data_2018_all.csv',data_final_LH,delimiter=',')
np.savetxt(save_loc+'extracted_LH_data_difference_2018_all.csv',data_final_diff_LH,delimiter=',')
