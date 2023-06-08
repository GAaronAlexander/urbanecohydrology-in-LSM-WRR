import xarray as xr
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
import matplotlib.patches as patches
import matplotlib.lines as lines
import os as os

save_loc = '../../intermediate-data/figure4/permeable_pavement/'

data_file_name = '201804010000.LDASOUT_DOMAIN1'
data_location = '/Volumes/Untitled/Integragting_LID_into_LSM/three_season_long_simulations_correct/three_season_permeable_pavement_var_depth/'
#data_location = '/Volumes/Untitled/Integragting_LID_into_LSM/milwaukee/share_correct/'
data_directory_list = sorted([i for i in os.listdir(data_location) if 'permeable' in i])


d = pd.date_range(start='2018-03-31 18:00:00',end='2020-10-31 18:00:00', freq='5T')
# print(data_directory_list)
# dd
drop_me = pd.date_range(start='2018-03-31 18:00:00',end='2018-04-30 18:00:00', freq='5T')
analysis_range = pd.date_range(start='2018-03-31 18:00:00',end='2018-10-31 18:00:00', freq='5T')


data_standard = xr.open_dataset(data_location+data_directory_list[0]+'/'+data_file_name)
data_standard = data_standard.assign_coords(Time=d)
data_standard = data_standard.sel(Time=analysis_range)


SFC_RUNOFF_stan = data_standard.SFCRNOFF.sel(Time=analysis_range[-1]) - data_standard.SFCRNOFF.sel(Time='2018-04-30 18:00:00')

#create loop over the percentage

data_extracted = np.zeros((8,51))


for i, file in enumerate(data_directory_list):
	print(i)



	Percentage_permeable = (i)/100
	print(Percentage_permeable)
	percentage_pavement = (100-i)/100


	data_loop = xr.open_dataset(data_location+data_directory_list[i]+'/'+data_file_name)
	data_loop = data_loop.assign_coords(Time=d)
	data_loop = data_loop.sel(Time=analysis_range)


	
	# data_loop.SOIL_M[:,0,0,1].plot()
	# data_loop.SOIL_M[:,0,1,1].plot()
	# data_loop.SOIL_M[:,0,2,1].plot()
	# data_loop.SOIL_M[:,0,3,1].plot()

	##first create runoff layer

	SFC_RUNOFF = data_loop.SFCRNOFF.sel(Time=analysis_range[-1]) - data_loop.SFCRNOFF.sel(Time='2018-04-30 18:00:00')
	
	UNDER_RUNOFF = data_loop.UGDRNOFF.sel(Time=analysis_range[-1]) - data_loop.UGDRNOFF.sel(Time='2018-04-30 18:00:00')
	
	data_loop = data_loop.drop_sel(Time=drop_me)


	## calculte the rain amount 
	rain_amount = data_loop.RAINRATE[1:,0,:].sum(axis=0).values
	rain_amount = np.append(rain_amount,[rain_amount[0],rain_amount[0]],axis=0)
	print(rain_amount)
	




	# calculate Transpiration & evaporation & canopy
	ETRAN = data_loop.ETRAN * 300 + data_loop.EDIR * 300 +  data_loop.ECAN * 300

	ECAN = data_loop.ECAN * 300
	EDIR = data_loop.EDIR * 300
	ET = data_loop.ETRAN * 300

	ET = ET[1:].sum(axis=0).values

	ETRAN = ETRAN[1:].sum(axis=0).values
	
	



	# calculate the SURFACE RUNON

	RUN_ON = data_loop.RUNONSFXY[1:]*300
	RUN_ON = RUN_ON.sum(axis=0).values


	## calculate the Soil Moisture Storage:
	SOIL_M_norm = data_loop.SOIL_M_PER_PAVEMENT[0,0,0]*100 + data_loop.SOIL_M_PER_PAVEMENT[0,0,1]*400 + data_loop.SOIL_M_PER_PAVEMENT[0,0,2]*600 + data_loop.SOIL_M_PER_PAVEMENT[0,0,3]*1000
	SOIL_M_norm = data_loop.SOIL_M_PER_PAVEMENT[-1,0,0]*100 + data_loop.SOIL_M_PER_PAVEMENT[-1,0,1]*400 + data_loop.SOIL_M_PER_PAVEMENT[-1,0,2]*600 + data_loop.SOIL_M_PER_PAVEMENT[-1,0,3]*1000 - SOIL_M_norm

	

	# amount of rain
	
	data_extracted[0,i] = rain_amount[0]
	# surface runoff from pavement

	data_extracted[1,i] = SFC_RUNOFF[0,0]*percentage_pavement
	
	# percentage over yard
	data_extracted[2,i] = SFC_RUNOFF[0,1]*Percentage_permeable

	# ET from yard
	data_extracted[3,i] = ETRAN[0,0]*percentage_pavement
	# ET from tree
	data_extracted[4,i] = ETRAN[0,1]*Percentage_permeable

	# normal soil moisture
	data_extracted[5,i] = SOIL_M_norm[1]*Percentage_permeable
	# underground runoff
	data_extracted[6,i] = UNDER_RUNOFF[0,1]*Percentage_permeable

np.savetxt('./permeable_pav_2018.csv',data_extracted,delimiter=',')

