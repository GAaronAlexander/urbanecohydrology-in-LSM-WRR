import xarray as xr
import numpy as np
import os 
import pandas as pd
import matplotlib.pyplot as plt

'''
generates a binary 1, 0 for rainfall for aggregation of our runoff. Only need once because rainfall is not changing!
'''
def create_rain_bool(rain_data):
	l = rain_data
	l = np.where(l >0.0, True, False)

	## code curtosy of Dan Wright for help!
	Threshold = 288 #5 minute time steps and 12 hours
	timecounter=100000000   # think of this as the time since last rain, assuming no storm to kick things off

	for i in range(0,len(l)):           # for loop felt easier than a while loop
	    if l[i]:  	                    # it is raining
	        timecounter=0               # if there is rain, then make sure your "time since last rain" tracker is set to zero...
	    else:                           #its not raining
	        if timecounter<Threshold:       
	            l[i]=True 
	       		
	   	         # if  time since last rain less than the threshold, define that time step as belonging to the prior storm
	        timecounter=timecounter+1  
	        print(timecounter)     # if there is no rain, your time since last rain should be counting up
	# new_bool = np.asarray(new_bool)
	# new_bool_rain = np.where(new_bool == 1, True, False)

	l = np.where(l==True,1,np.nan)


	return(l)


save_loc = '../intermediate-data/figure2/'

data_file_name = '201804010000.LDASOUT_DOMAIN1'
data_location = '/Volumes/Untitled/Integragting_LID_into_LSM/three_season_long_simulations/'


d = pd.date_range(start='2018-03-31 18:00:00',end='2020-10-31 18:00:00', freq='5T')
drop1 = pd.date_range(start='2018-04-30 18:00:00',end='2018-10-31 18:00:00', freq='5T')
drop2 = pd.date_range(start='2019-04-30 18:00:00',end='2019-10-31 18:00:00', freq='5T')
drop3 = pd.date_range(start='2020-04-30 18:00:00',end='2020-10-31 18:00:00', freq='5T')

drop1 = drop1.append(drop2)
drop1 = drop1.append(drop3)


data_turf = xr.open_dataset(data_location+'201804010000.LDASOUT_DOMAIN1')
data_turf = data_turf.assign_coords(Time=d)
data_turf = data_turf.sel(Time=drop1)

data_turf_rain = data_turf.RAINRATE[:,0,0]
rain_happning = create_rain_bool(data_turf_rain)


np.savetxt(save_loc+'rain_bool_12hour_window.csv',rain_happning,delimiter=',')
