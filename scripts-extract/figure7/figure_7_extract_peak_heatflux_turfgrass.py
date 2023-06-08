import xarray as xr
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import rcParams
import os
import scipy.stats as stats
from matplotlib.dates import DateFormatter



data_file_name = '201804010000.LDASOUT_DOMAIN1'
data_location = '/Volumes/Untitled/Integragting_LID_into_LSM/three_season_long_simulations_correct/three_season_turgrass_with_disconnect/'
#data_location = '/Volumes/Untitled/Integragting_LID_into_LSM/milwaukee/share_correct/'
data_directory_list = sorted([i for i in os.listdir(data_location) if 'disconnect' in i])
print(data_directory_list)

save_loc = '../../intermediate-data/figure7/extract_data_turfgrass/'

##define things for dropping our analysis
d = pd.date_range(start='2018-03-31 18:00:00',end='2020-10-31 18:00:00', freq='5T')
drop1 = pd.date_range(start='2018-04-30 18:00:00',end='2018-10-31 18:00:00', freq='5T')
drop2 = pd.date_range(start='2019-04-30 18:00:00',end='2019-10-31 18:00:00', freq='5T')
drop3 = pd.date_range(start='2020-04-30 18:00:00',end='2020-10-31 18:00:00', freq='5T')

drop1 = drop1.append(drop2)
drop1 = drop1.append(drop3)

data_extracted_HFX = np.ones((6,61))
data_extracted_LH = np.ones((6,61))

data_stan = xr.open_dataset(data_location+data_directory_list[0]+'/201804010000.LDASOUT_DOMAIN1')
data_stan = data_stan.assign_coords(Time=d)
data_stan = data_stan.sel(Time=drop1)

for i,n in enumerate(data_directory_list):

	Percentage_turfgrass = (70)/100
	percentage_pavement = (((60-i))/2)/100
	percentage_pavement_dis = (i/2)/100

	data_loop = xr.open_dataset(data_location+n+'/201804010000.LDASOUT_DOMAIN1')
	print(i)

	
	data_loop = data_loop.assign_coords(Time=d)

	data_loop = data_loop.sel(Time=drop1)
	

	index = pd.date_range(start='00:00:00',end='23:55:00',freq='5T')

	HFX_data_loop = data_stan.HFX.isel(west_east=0)* percentage_pavement  + data_loop.HFX.isel(west_east=1)*Percentage_turfgrass + data_loop.HFX.isel(west_east=0)*percentage_pavement_dis
	LH_data_loop = data_stan.LH.isel(west_east=0)* percentage_pavement  + data_loop.LH.isel(west_east=1)*Percentage_turfgrass + data_loop.LH.isel(west_east=0)*percentage_pavement_dis

	## resample the HFX data, get the max and min, and then fill in
	data_test = pd.DataFrame(HFX_data_loop.values,index=HFX_data_loop.Time)
	data_test_resample = data_test.groupby([data_test.index.hour, data_test.index.minute]).median()
	data_test_resample_max = np.max(data_test_resample.values)
	data_test_resample_min = np.min(data_test_resample.values)


	data_test_hist1 = data_test.groupby([data_test.index.hour, data_test.index.minute]).quantile(0.75)
	data_test_hist2 = data_test.groupby([data_test.index.hour, data_test.index.minute]).quantile(0.25)

	data_test_hist1_75quantile_max = data_test_hist1.values[np.argmax(data_test_resample.values)]
	data_test_hist1_75quantile_min = data_test_hist1.values[np.argmin(data_test_resample.values)]

	data_test_hist1_25quantile_max = data_test_hist2.values[np.argmax(data_test_resample.values)]
	data_test_hist1_25quantile_min = data_test_hist2.values[np.argmin(data_test_resample.values)]


	##load in data 
	data_extracted_HFX[0,i] = data_test_resample_max
	data_extracted_HFX[1,i] = data_test_hist1_75quantile_max
	data_extracted_HFX[2,i] = data_test_hist1_25quantile_max
	data_extracted_HFX[3,i] = data_test_resample_min
	data_extracted_HFX[4,i] = data_test_hist1_75quantile_min
	data_extracted_HFX[5,i] = data_test_hist1_25quantile_min


	## now do the exact same thing, but for LH

	## resample the HFX data, get the max and min, and then fill in
	data_test = pd.DataFrame(LH_data_loop.values,index=HFX_data_loop.Time)
	data_test_resample = data_test.groupby([data_test.index.hour, data_test.index.minute]).median()
	data_test_resample_max = np.max(data_test_resample.values)
	data_test_resample_min = np.min(data_test_resample.values)


	data_test_hist1 = data_test.groupby([data_test.index.hour, data_test.index.minute]).quantile(0.75)
	data_test_hist2 = data_test.groupby([data_test.index.hour, data_test.index.minute]).quantile(0.25)

	data_test_hist1_75quantile_max = data_test_hist1.values[np.argmax(data_test_resample.values)]
	data_test_hist1_75quantile_min = data_test_hist1.values[np.argmin(data_test_resample.values)]

	data_test_hist1_25quantile_max = data_test_hist2.values[np.argmax(data_test_resample.values)]
	data_test_hist1_25quantile_min = data_test_hist2.values[np.argmin(data_test_resample.values)]


	##load in data 
	data_extracted_LH[0,i] = data_test_resample_max
	data_extracted_LH[1,i] = data_test_hist1_75quantile_max
	data_extracted_LH[2,i] = data_test_hist1_25quantile_max
	data_extracted_LH[3,i] = data_test_resample_min
	data_extracted_LH[4,i] = data_test_hist1_75quantile_min
	data_extracted_LH[5,i] = data_test_hist1_25quantile_min

np.savetxt(save_loc+'HFX_extracted_max_min_turfgrass.csv',data_extracted_HFX,delimiter=',')
np.savetxt(save_loc+'LH_extracted_max_min_turfgrass.csv',data_extracted_LH,delimiter=',')
