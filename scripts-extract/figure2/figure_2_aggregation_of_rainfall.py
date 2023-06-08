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
	time = []
	time_end = []
	print(nans)

	row = 0
	column = 0 
	column_old = 0
	for i in range(0,len(nans)-1):

		if nans[i] == True and nans[i+1] == True:
			data_agg[row,column] = data[i]
			column +=1
		elif nans[i] == True and nans[i+1] == False:

			data_agg[row,column] = data[i]
			column = 0
			row +=1
			time_end.append(i)
		elif nans[i] == False and nans[i+1] == True:
			time.append(i)

		

	return(data_agg,time,time_end)

data_to_save = np.zeros((1,125))
data_loc = '../../intermediate-data/figure2/'
rain_windows = np.loadtxt(data_loc+'rain_bool_12hour_window.csv',delimiter=',')
rain_windows = np.where(rain_windows==1,1,np.nan)


data_location = '/Users/aaronalexander/Google Drive/My Drive/dissertation_chapter1_data/raw_outputs_from_cheyenne/three_season_permeable_pavement_var_depth/'
#data_location = '/Volumes/Untitled/Integragting_LID_into_LSM/milwaukee/share_correct/'
data_directory_list = sorted([i for i in os.listdir(data_location) if 'permeable' in i])
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
print(delll)
print(data_directory_list[0])

data_rain_2 = data_standard.RAINRATE[:,0,0]
print(data_rain_2)


data_aggrigate = np.zeros((1000,delll[1]-delll[0]+1))
data_aggrigate = np.where(data_aggrigate==0,np.nan,np.nan)


## organize the rainfall
data_aggrigate_n,data_times_start,data_time_end = organize_rainfall(rain_windows,data_rain_2.values,data_aggrigate)

	## event based rainfall form the rain bools
data_aggrigate_things = np.nansum(data_aggrigate,axis=1)

data_aggrigate_things = np.where(data_aggrigate_things == 0,np.nan,data_aggrigate_things)
data_aggrigate_things = data_aggrigate_things[~np.isnan(data_aggrigate_things)]

	

data_to_save[0,:] = data_aggrigate_things[:]


np.savetxt('../../intermediate-data/figure2/RAINFALL_12hour_EVENT_WINDOW.csv',data_to_save,delimiter=',')


# plt.boxplot(data_aggrigate_things,whis=(1,99))
# plt.show()






