import xarray as xr
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import rcParams
import scipy.stats as stats
from matplotlib.dates import DateFormatter



rcParams['font.family'] = 'serif'
rcParams['font.sans-serif'] = ['Cooper Std']

sns.set_style('ticks')
# check_rn_input=pd.read_csv('/Users/aarona//My Drive/integrating_GSI_into_large_scale_LSM/Milwaukee_NLDAS2_HRLDAS_input_hrly.dat',sep=' ')

data_loc = '/Users/aaronalexander/Google Drive/My Drive/dissertation_chapter1_data/raw_outputs_from_cheyenne/'
save_loc = '../../prelim_results/diel_patterns/'


data_stan = xr.open_dataset(data_loc+'three_season_share_tree_additional/share_tree_additional_treecover_percentage_00/201804010000.LDASOUT_DOMAIN1')
data_plot = xr.open_dataset(data_loc+'three_season_shifting_tree/share_tree_shifting_treecover_percentage_70/201804010000.LDASOUT_DOMAIN1')
data_turf = xr.open_dataset(data_loc+'three_season_turgrass_with_disconnect/turf_grass_three_season/201804010000.LDASOUT_DOMAIN1')


d = pd.date_range(start='2018-03-31 18:00:00',end='2020-10-31 18:00:00', freq='5T')
data_stan = data_stan.assign_coords(Time=d)
data_plot = data_plot.assign_coords(Time=d)
data_turf = data_turf.assign_coords(Time=d)

drop1 = pd.date_range(start='2018-04-30 18:00:00',end='2018-10-31 18:00:00', freq='5T')
drop2 = pd.date_range(start='2019-04-30 18:00:00',end='2019-10-31 18:00:00', freq='5T')
drop3 = pd.date_range(start='2020-04-30 18:00:00',end='2020-10-31 18:00:00', freq='5T')
drop1 = drop1.append(drop2)
drop1 = drop1.append(drop3)


data_stan = data_stan.sel(Time=drop1)
data_plot = data_plot.sel(Time=drop1)
data_turf = data_turf.sel(Time=drop1)

index = pd.date_range(start='00:00:00',end='23:55:00',freq='5T')

#### create typical
fig = plt.figure(figsize=(12,9))
ax1 = plt.subplot(111)

## create first time series
HFX_data1 = data_stan.HFX.isel(west_east=0) * 0.5 +  data_stan.HFX.isel(west_east=1)* 0.5  
# + data_plot.HFX.isel(west_east=1) * 0.5


data_test = pd.DataFrame(HFX_data1.values,index=HFX_data1.Time)
data_test_resample = data_test.groupby([data_test.index.hour, data_test.index.minute]).median()


data_test_hist1 = data_test.groupby([data_test.index.hour, data_test.index.minute]).quantile(0.75)
data_test_hist2 = data_test.groupby([data_test.index.hour, data_test.index.minute]).quantile(0.25)


ax1.plot(index,data_test_resample.values,color='#A31712',linewidth=4,label='Sensible')
ax1.fill_between(index, data_test_hist1.values.flatten(),data_test_hist2.values.flatten(),alpha=0.3,color='#A31712')
print('Typical Sensible Heat Flux')
print(np.max(data_test_resample))
print(data_test_hist1.values[np.argmax(data_test_resample)] - data_test_hist2.values[np.argmax(data_test_resample)])


HFX_data1 = data_stan.LH.isel(west_east=0) * 0.5 +  data_stan.LH.isel(west_east=1)* 0.5 
# + data_plot.LH.isel(west_east=1) * 0.5


data_test = pd.DataFrame(HFX_data1.values,index=HFX_data1.Time)
data_test_resample = data_test.groupby([data_test.index.hour, data_test.index.minute]).median()


data_test_hist1 = data_test.groupby([data_test.index.hour, data_test.index.minute]).quantile(0.75)
data_test_hist2 = data_test.groupby([data_test.index.hour, data_test.index.minute]).quantile(0.25)


ax1.plot(index,data_test_resample.values,color='#1A41B8',linewidth=4,label='Latent')
ax1.fill_between(index, data_test_hist1.values.flatten(),data_test_hist2.values.flatten(),alpha=0.3,color='#1A41B8')
print('Typical Latent Heat Flux')
print(np.max(data_test_resample))
print(data_test_hist1.values[np.argmax(data_test_resample)] - data_test_hist2.values[np.argmax(data_test_resample)])


ax1.grid(True,'major','both',color='#ADABA8',linestyle='--')
gridlines = ax1.yaxis.get_gridlines()
gridlines[1].set_color("k")
gridlines[1].set_linewidth(2.5)

ax1.xaxis.set_major_formatter(DateFormatter('%H:%M'))
ax1.set_xlim([index[0],index[-1]])
ax1.set_ylim([-90,410])
ax1.set_xlabel('Time of Day',fontsize=40)
ax1.tick_params(axis='both', which='major', labelsize=30)

ax1.set_ylabel(r'Heat Flux [$W m^{-2}$]',fontsize=40)

# plt.legend(frameon=False,fontsize=30)
plt.tight_layout()

plt.savefig(save_loc+'typical_diel_heatflux_shiftingtree.png',dpi=500)
plt.close()
####

fig2 = plt.figure(figsize=(12,9))
ax2 = plt.subplot(111)

HFX_data1 = data_stan.HFX.isel(west_east=0) * 0.15 +  data_plot.HFX.isel(west_east=0)* 0.35  + data_plot.HFX.isel(west_east=1) * 0.15 + data_turf.HFX.isel(west_east=1) * 0.35


data_test = pd.DataFrame(HFX_data1.values,index=HFX_data1.Time)
data_test_resample = data_test.groupby([data_test.index.hour, data_test.index.minute]).median()


data_test_hist1 = data_test.groupby([data_test.index.hour, data_test.index.minute]).quantile(0.75)
data_test_hist2 = data_test.groupby([data_test.index.hour, data_test.index.minute]).quantile(0.25)



ax2.plot(index,data_test_resample.values,color='#A31712',linewidth=4,label='Sensible')
ax2.fill_between(index, data_test_hist1.values.flatten(),data_test_hist2.values.flatten(),alpha=0.3,color='#A31712')
print('Extreme Sensible Heat Flux')
print(np.max(data_test_resample))
print(data_test_hist1.values[np.argmax(data_test_resample)] - data_test_hist2.values[np.argmax(data_test_resample)])


HFX_data1 = data_stan.LH.isel(west_east=0) * 0.15 +  data_plot.LH.isel(west_east=0)* 0.35  +data_plot.LH.isel(west_east=1) * 0.15 + data_turf.LH.isel(west_east=1) * 0.35




data_test = pd.DataFrame(HFX_data1.values,index=HFX_data1.Time)
data_test_resample = data_test.groupby([data_test.index.hour, data_test.index.minute]).median()


data_test_hist1 = data_test.groupby([data_test.index.hour, data_test.index.minute]).quantile(0.75)
data_test_hist2 = data_test.groupby([data_test.index.hour, data_test.index.minute]).quantile(0.25)

data_saveme = pd.concat([data_test_resample,data_test_hist2,data_test_hist1],axis=1,keys=['median','25_percentile','75_percentile'])
data_saveme.to_csv('./LH_35_shift_tree.csv')

ax2.plot(index,data_test_resample.values,color='#1A41B8',linewidth=4,label='Latent')
ax2.fill_between(index, data_test_hist1.values.flatten(),data_test_hist2.values.flatten(),alpha=0.3,color='#1A41B8')
print('Extreme Latent Heat Flux')
print(np.max(data_test_resample))
print(data_test_hist1.values[np.argmax(data_test_resample)] - data_test_hist2.values[np.argmax(data_test_resample)])


ax2.grid(True,'major','both',color='#ADABA8',linestyle='--')
gridlines = ax2.yaxis.get_gridlines()
gridlines[1].set_color("k")
gridlines[1].set_linewidth(2.5)

ax2.xaxis.set_major_formatter(DateFormatter('%H:%M'))
ax2.set_xlim([index[0],index[-1]])
ax2.set_ylim([-90,410])
ax2.set_xlabel('Time of Day',fontsize=40)
ax2.tick_params(axis='both', which='major', labelsize=30)

ax2.set_ylabel(r'Heat Flux [$W m^{-2}$]',fontsize=40)

# plt.legend(frameon=False,fontsize=30)
plt.tight_layout()

plt.savefig(save_loc+'extreme_diel_heatflux_shifttree.png',dpi=500)

