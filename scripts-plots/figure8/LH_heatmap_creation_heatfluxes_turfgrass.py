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


data_location = '../../data/turfgrass/heatmap_sensible_latent_heatfluxes/'
sav_loc = '../../prelim_results/turfgrass_results/flux_heatmaps/'

data_final_H = np.loadtxt(data_location+'extracted_H_data_2020_all.csv',delimiter=',')


data_final_H_sum = np.sum(data_final_H,axis=0)

data_final_diff_H = np.zeros_like(data_final_H)
for i in range(0,61):
	data_final_diff_H[:,i] = -1*data_final_H[:,0] + data_final_H[:,i]

# data_final_diff_H = np.loadtxt(data_location+'extracted_LH_data_difference_2018_all.csv',delimiter=',')

data_file_name = '201804010000.LDASOUT_DOMAIN1'
data_location2 = '/Users/aaronalexander/Google Drive/My Drive/dissertation_chapter1_data/raw_outputs_from_cheyenne/three_season_share_tree_additional/'
data_directory_list = sorted(os.listdir(data_location2))

ticks = np.linspace(0,60,61)
nums = np.linspace(0,100,61)
ticks_y = np.linspace(0,184,185)



print(data_directory_list)
new_data =  xr.open_dataset(data_location2+data_directory_list[2]+'/'+data_file_name)
d = pd.date_range(start='2018-03-31 18:00:00',end='2020-10-31 18:00:00', freq='5T')
analysis_time = pd.date_range(start='2020-04-30 18:00:00',end='2020-10-31 18:00:00', freq='5T')

drop_me = pd.date_range(start='2020-03-31 18:00:00',end='2020-04-30 18:00:00', freq='5T')
days = pd.date_range(start='2020-04-30',end='2020-10-31', freq='D')
days2 = pd.date_range(start='2020-04-30 13:00:00',end='2020-10-31 12:00:00', freq='D')

new_data = new_data.assign_coords(Time=d)
new_data = new_data.sel(Time=analysis_time)

rain = new_data.RAINRATE[:,0,0]
rain = rain.resample(Time='D').sum()




figure,axs = plt.subplots(nrows=1,ncols=3,figsize=(27,14),gridspec_kw={'width_ratios': [1.2, 9,9]},sharey=True)


## PRecipitation 
ax_bar = axs[0]

ax_bar.barh(ticks_y,rain,color='#AEC4CF',height=.9,edgecolor='k',alpha=1,zorder=100)
ax_bar.set_yticks([])
ax_bar.invert_yaxis()  # labels read top-to-bottom
ax_bar.invert_xaxis()  # labels read top-to-bottom
ax_bar.yaxis.set_tick_params(which='both', labelbottom=False,size=0)

ax2_bar = ax_bar.twinx()
ax2_bar.get_shared_y_axes().join(ax2_bar, ax_bar)
ax2_bar.set_yticks(ticks=ticks_y[::10])
ax2_bar.set_yticklabels(labels=days[::10].strftime('%m-%d'),fontsize=25)
ax2_bar.invert_yaxis() 


ax_bar.grid(which='major', color='k', linestyle='--', linewidth=2,axis='x')
ax_bar.set_xlabel('Precip\n[mm]',fontsize=35)
ax_bar.set_xticks(ticks=[0,25,50,75])
ax_bar.set_xticklabels(labels=['0','25','50','75'],fontsize=20)
ax2_bar.yaxis.set_tick_params(which='major',length=10,width=2)
ax2_bar.set_ylabel('Day',fontsize=35,labelpad=20)
ax_bar.xaxis.set_tick_params(which='major',length=10,width=2)

ax_bar.spines['left'].set_visible(False)
ax_bar.spines['top'].set_visible(False)
ax2_bar.spines['left'].set_visible(False)
ax2_bar.spines['top'].set_visible(False)
# ax2_bar2.set_ylim([days[0],days[-1]])
# ax_bar2.invert_yaxis()

## Plot for the heat maps First
ax1 = axs[1]
ax1.grid(which="minor", color="w", linestyle='-', linewidth=3,zorder=100)
x = ax1.imshow(data_final_H,vmin=-10,vmax=10,cmap=cm.roma,origin='upper',aspect='auto')

cax = plt.colorbar(x,extend='both',ax=ax1)
cax.ax.get_yaxis().labelpad =30
cax.ax.set_ylabel('Energy [GJ]', rotation=270,fontsize=35)
cax.ax.tick_params(axis='both', which='major', labelsize=25)


ax1.set_xticks(np.arange(-.5, 61, 1), minor=True)
ax1.xaxis.set_tick_params(which='minor',length=0)
ax1.set_yticks(np.arange(-.5, 185, 1), minor=True)
ax1.yaxis.set_tick_params(which='minor',length=0)


# Gridlines based on minor ticks
ax1.grid(which='minor', color='w', linestyle='-', linewidth=0.05)
ax1.xaxis.set_tick_params(labelleft=True)

ax1.set_xticks(ticks=ticks[::15])
# ax1.set_yticks(ticks=ticks_y[:-1:10])

ax1.set_xticklabels(labels=np.around(nums[::15],decimals=1),fontsize=25)
ax1.xaxis.set_tick_params(which='major', length=10,width=2)
ax1.yaxis.set_visible(False)

ax1.set_xlabel('Percentage Disconnect [%]',fontsize=35,labelpad=25)
ax1.yaxis.set_tick_params(which='both', length=0,width=0,labelbottom=True)


ax1_3 = ax1.twiny()
ax1_3.set_xticks(np.arange(-.5, 61, 1), minor=True)
ax1_3.xaxis.set_tick_params(which='minor',length=0)
# ax1_3.xaxis.set_tick_params(which='major',length=10)
ax1_3.tick_params(axis='x', which='major', pad=15)
ax1_3.set_xticks(ticks=ticks[::15])
ax1_3.set_xticklabels(labels=np.rint(data_final_H_sum[::15]),fontsize=20)
ax1_3.xaxis.set_tick_params(which='major',length=25)
ax1_3.set_xlabel('Total Seasonal Energy [GJ]',fontsize=35,labelpad=20)



## Percentage Differences
ax2 = axs[2]
x2 = ax2.imshow(data_final_diff_H,vmin=-6,vmax=6,cmap=cm.bam,origin='upper',aspect='auto')

cax2 = plt.colorbar(x2,extend='both',ax=ax2)
cax2.ax.get_yaxis().labelpad =40
cax2.ax.set_ylabel('Difference [GJ]', rotation=270,fontsize=35)
cax2.ax.tick_params(axis='both', which='major', labelsize=25)

ax2.set_xticks(np.arange(-.5, 61, 1), minor=True)
ax2.xaxis.set_tick_params(which='minor',length=0)
ax2.set_yticks(np.arange(-.5, 185, 1), minor=True)
ax2.yaxis.set_tick_params(which='minor',length=0)


# Gridlines based on minor ticks
ax2.grid(which='minor', color='w', linestyle='-', linewidth=0.05)


ax2.set_xticks(ticks=ticks[::15])
ax2.set_yticks(ticks=ticks_y[:-1:10])

ax2.set_xticklabels(labels=np.around(nums[::15],decimals=1),fontsize=25)
ax2.set_yticklabels(labels=days[:-1:10].strftime('%m-%d'),fontsize=25)

ax2.set_xlabel('Percentage Disconnect [%]',fontsize=35,labelpad=25)
# ax2.set_ylabel('Day',fontsize=35)
ax2.yaxis.set_tick_params(which='both', labelbottom=True)


plt.tight_layout()

plt.savefig(sav_loc+'Sensible_heat_flux_2020_LARGETEXT.png',dpi=500)
plt.close()