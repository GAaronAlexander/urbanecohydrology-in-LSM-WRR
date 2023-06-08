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
from matplotlib.ticker import FormatStrFormatter


data_location = '../../data/extracted_data_shifting_canopy/season_heatflux_heatmap_shifting/'
sav_loc = '../../prelim_results/heatmap_sensitivity_correct/tree_shift/'

data_final_H = np.loadtxt(data_location+'extracted_HFX_data_2018_day_only.csv',delimiter=',')


data_final_H_sum = np.sum(data_final_H,axis=0)

data_final_diff_H = np.zeros_like(data_final_H)
for i in range(0,71):
	data_final_diff_H[:,i] = -1*data_final_H[:,0] + data_final_H[:,i]

# data_final_diff_H = np.loadtxt(data_location+'extracted_H_data_difference_2020_day_only.csv',delimiter=',')

data_file_name = '201804010000.LDASOUT_DOMAIN1'
data_location2 = '/Volumes/Untitled/Integragting_LID_into_LSM/three_season_long_simulations/three_season_long_extra_canopy/'
data_directory_list = sorted(os.listdir(data_location2))
ticks = np.linspace(0,70,71)
nums = np.linspace(0,35,71)

ticks_y = np.linspace(0,185,186)


# c = cm.rainbow(np.linspace(0, 1, 8))
print(data_directory_list)
new_data =  xr.open_dataset(data_location2+data_directory_list[0]+'/'+data_file_name)
d = pd.date_range(start='2018-03-31 18:00:00',end='2020-10-31 18:00:00', freq='5T')
analysis_time = pd.date_range(start='2020-04-30 18:00:00',end='2020-10-31 18:00:00', freq='5T')

drop_me = pd.date_range(start='2019-03-31 18:00:00',end='2019-04-30 18:00:00', freq='5T')
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
		# thing.append(r'$\bigstar$')
		thing.append('')
	else:
		thing.append('')

figure = plt.figure(figsize=(15,10))

ax1 = plt.subplot(121)
ax1.grid(which="minor", color="w", linestyle='-', linewidth=3,zorder=100)
x = plt.imshow(data_final_H,vmin=-10,vmax=10,cmap=cm.roma,origin='upper',aspect='auto')

cax = plt.colorbar(x,extend='both')
cax.ax.get_yaxis().labelpad = 15
cax.ax.set_ylabel('Energy [GJ]', rotation=270,fontsize=12)

ax1.set_xticks(np.arange(-.5, 71, 1), minor=True)
ax1.xaxis.set_tick_params(which='minor',length=0)
ax1.set_yticks(np.arange(-.5, 185, 1), minor=True)
ax1.yaxis.set_tick_params(which='minor',length=0)


# Gridlines based on minor ticks
ax1.grid(which='minor', color='w', linestyle='-', linewidth=0.05)


ax1.set_xticks(ticks=ticks[::10])
ax1.set_yticks(ticks=ticks_y[:-1:10])

ax1.set_xticklabels(labels=nums[::10],fontsize=12)
ax1.set_yticklabels(labels=days[:-1:10].strftime('%m-%d'),fontsize=12)

plt.xlabel('Percentage of Extra Tree over Pavement(%)',fontsize=16,labelpad=12)
plt.ylabel('Day',fontsize=16,labelpad=12)



ax1_2 = ax1.twinx()
ax1_2.set_yticks(np.arange(0.5, 185, 1), minor=True)
ax1_2.yaxis.set_tick_params(which='minor',length=0)
ax1_2.set_yticklabels(labels=thing,minor=True,fontsize=8)


ax1_2.set_yticklabels(labels='')
ax1_2.yaxis.set_tick_params(length=0)

ax1_3 = ax1.twiny()
ax1_3.set_xticks(np.arange(-.5, 71, 1), minor=True)
ax1_3.xaxis.set_tick_params(which='minor',length=0)
# ax1_3.xaxis.set_tick_params(which='major',length=10)
ax1_3.tick_params(axis='x', which='major', pad=15)
ax1_3.set_xticks(ticks=ticks[::10])
ax1_3.set_xticklabels(labels=np.rint(data_final_H_sum[::10]),fontsize=13)
ax1_3.xaxis.set_tick_params(which='major',length=10)
plt.xlabel('Total Seasonal Energy (GJ)',fontsize=16,labelpad=12)




ax2 = plt.subplot(122)
x = plt.imshow(data_final_diff_H,vmin=-6,vmax=6,cmap=cm.bam,origin='upper',aspect='auto')

cax = plt.colorbar(x,extend='both')
cax.ax.get_yaxis().labelpad = 15
cax.ax.set_ylabel('Difference [GJ]', rotation=270,fontsize=12)

ax2.set_xticks(np.arange(-.5, 71, 1), minor=True)
ax2.xaxis.set_tick_params(which='minor',length=0)
ax2.set_yticks(np.arange(-.5, 185, 1), minor=True)
ax2.yaxis.set_tick_params(which='minor',length=0)


# Gridlines based on minor ticks
ax2.grid(which='minor', color='w', linestyle='-', linewidth=0.05)


ax2.set_xticks(ticks=ticks[::10])
ax2.set_yticks(ticks=ticks_y[:-1:10])

ax2.set_xticklabels(labels=nums[::10],fontsize=12)
ax2.set_yticklabels(labels=days[:-1:10].strftime('%m-%d'),fontsize=12)

plt.xlabel('Percentage of Extra Tree over Pavement(%)',fontsize=16)
plt.ylabel('Day',fontsize=16)



ax2_2 = ax2.twinx()
ax2_2.set_yticks(np.arange(0.5, 185, 1), minor=True)
ax2_2.yaxis.set_tick_params(which='minor',length=0)
ax2_2.set_yticklabels(labels=thing,minor=True,fontsize=8)


ax2_2.set_yticklabels(labels='')
ax2_2.yaxis.set_tick_params(length=0)
plt.tight_layout()
plt.savefig(sav_loc+'Average_total_sensible_heat_flux_day_time.png',dpi=400)
plt.close()