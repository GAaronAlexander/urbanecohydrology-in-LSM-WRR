import xarray as xr
import numpy as np
import os 
import pandas as pd
from scipy.signal import savgol_filter
# yhat = savgol_filter(y, 51, 3) # window size 51, polynomial order 3
import matplotlib.pyplot as plt

def pir(x):
    # pad with np.nan
    x = np.append(np.nan, np.append(x, np.nan))
    # find where null
    w = np.where(np.isnan(x))[0]
    # diff to find length of stretch
    # argmax to find where largest stretch
    a = np.diff(w).argmax()
    # return original positions of boundary nulls
    return w[[a, a + 1]] + np.array([0, -2])

## this takes the rainfall segments, and organizes them to 
## to allow for you integration of the amount of rainfall. 
def organize_rainfall(x,data,data_agg):
	nans = ~np.isnan(x)
	print(nans)

	row = 0
	column = 0 

	for i in range(0,len(nans)-1):

		if nans[i] == True and nans[i+1] == True:
			data_agg[row,column] = data[i]
			column +=1
		elif nans[i] == True and nans[i+1] == False:

			data_agg[row,column] = data[i]
			column = 0
			row +=1

	return data_agg

data_to_save = np.zeros((71,125))
data_loc = '../data/precipitation_bools/'
rain_windows = np.loadtxt(data_loc+'rain_bool_12hour_window.csv',delimiter=',')
rain_windows = np.where(rain_windows==1,1,np.nan)


data_location = '/Volumes/Untitled/Integragting_LID_into_LSM/three_season_long_simulations_correct/three_season_share_tree_additional/'
#data_location = '/Volumes/Untitled/Integragting_LID_into_LSM/milwaukee/share_correct/'
data_directory_list = sorted([i for i in os.listdir(data_location) if 'share_tree' in i])
print(data_directory_list)

d = pd.date_range(start='2018-03-31 18:00:00',end='2020-10-31 18:00:00', freq='5T')
drop1 = pd.date_range(start='2018-04-30 18:00:00',end='2018-10-31 18:00:00', freq='5T')
drop2 = pd.date_range(start='2019-04-30 18:00:00',end='2019-10-31 18:00:00', freq='5T')
drop3 = pd.date_range(start='2020-04-30 18:00:00',end='2020-10-31 18:00:00', freq='5T')

drop1 = drop1.append(drop2)
drop1 = drop1.append(drop3)


data_standard = xr.open_dataset(data_location+data_directory_list[0]+'/201804010000.LDASOUT_DOMAIN1')
data_standard = data_standard.assign_coords(Time=d)
data_standard = data_standard.sel(Time=drop1)

delll = pir(rain_windows)



for i,ll in enumerate(data_directory_list):
	print(i)
	percentage_tree = (100/2)/100
	percentage_tree_over_pavement = (i/2)/100
	percentage_urban = ((100-i)/2)/100
	print(percentage_tree,percentage_tree_over_pavement,percentage_urban)

	
	data_loop = xr.open_dataset(data_location+ll+'/201804010000.LDASOUT_DOMAIN1')
	data_loop = data_loop.assign_coords(Time=d)
	data_loop = data_loop.sel(Time=drop1)

	data_standard_rain = data_standard.RUNSFXY[:,0,0]*rain_windows*300*percentage_urban + data_loop.RUNSFXY[:,0,0]*rain_windows*300*percentage_tree_over_pavement + data_loop.RUNSFXY[:,0,1]*rain_windows*300*percentage_tree
	
	
	data_aggrigate = np.zeros((1000,delll[1]-delll[0]+1))
	data_aggrigate = np.where(data_aggrigate==0,np.nan,np.nan)


	## organize the rainfall
	data_aggrigate_n = organize_rainfall(rain_windows,data_standard_rain.values,data_aggrigate)

	## event based rainfall form the rain bools
	data_aggrigate_things = np.nansum(data_aggrigate,axis=1)

	## drop the extra zeros~!
	data_aggrigate_things = np.where(data_aggrigate_things == 0,np.nan,data_aggrigate_things)
	data_aggrigate_things = data_aggrigate_things[~np.isnan(data_aggrigate_things)]

	

	# append the save
	data_to_save[i,:] = data_aggrigate_things[:]


np.savetxt('../intermediate-data/figure2/three_season_tree_sharetree_siltloam_12hourwindow_correct.csv',data_to_save,delimiter=',')


# plt.boxplot(data_aggrigate_things,whis=(1,99))
# plt.show()






