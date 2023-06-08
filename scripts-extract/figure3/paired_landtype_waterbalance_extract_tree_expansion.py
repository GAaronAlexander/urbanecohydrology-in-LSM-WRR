import xarray as xr
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
import matplotlib.patches as patches
import matplotlib.lines as lines
import os as os

save_loc = '../../intermediate-data/figure3/extract_data_tree_expansion/'

data_file_name = '201804010000.LDASOUT_DOMAIN1'
data_location = '/Volumes/Untitled/Integragting_LID_into_LSM/three_season_long_simulations_correct/three_season_share_tree_additional_clayloam/'
#data_location = '/Volumes/Untitled/Integragting_LID_into_LSM/milwaukee/share_correct/'
data_directory_list = sorted([i for i in os.listdir(data_location) if 'sharetree' in i])
print(data_directory_list)

d = pd.date_range(start='2018-03-31 18:00:00',end='2020-10-31 18:00:00', freq='5T')

drop_me = pd.date_range(start='2018-03-31 18:00:00',end='2018-04-30 18:00:00', freq='5T')
analysis_range = pd.date_range(start='2018-03-31 18:00:00',end='2018-10-31 18:00:00', freq='5T')


data_stan = xr.open_dataset(data_location+data_directory_list[0]+'/'+data_file_name)


data_stan = data_stan.assign_coords(Time=d)

SFC_RUNOFF_STAN = data_stan.SFCRNOFF.sel(Time='2018-10-31 18:00:00') - data_stan.SFCRNOFF.sel(Time='2018-04-30 18:00:00')

runoff_info = np.zeros((70,1))

# create a figure
figure, ax1 = plt.subplots(nrows=1,ncols=1,figsize=(20,10))

#create loop over the percentage

data_extracted = np.zeros((8,71))

for i, file in zip(range(0,71),data_directory_list):

	bottom_loop = 0


	Percentage_over_pavement_tree = i/2/100
	percentage_over_yard = 50/100
	percentage_pavement = (50-i/2)/100
	print(percentage_pavement)

	print(percentage_over_yard)

	data_loop = xr.open_dataset(data_location+data_directory_list[i]+'/'+data_file_name)
	data_loop = data_loop.assign_coords(Time=d)


	data_loop = data_loop.sel(Time=analysis_range)
	

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
	SOIL_M_norm = data_loop.SOIL_M[0,0,0]*100 + data_loop.SOIL_M[0,0,1]*400 + data_loop.SOIL_M[0,0,2]*600 + data_loop.SOIL_M[0,0,3]*1000
	SOIL_M_norm = data_loop.SOIL_M[-1,0,0]*100 + data_loop.SOIL_M[-1,0,1]*400 + data_loop.SOIL_M[-1,0,2]*600 + data_loop.SOIL_M[-1,0,3]*1000 - SOIL_M_norm

	# amount of rain
	
	data_extracted[0,i] = rain_amount[0]
	# surface runoff from pavement
	if i == 0:
		data_extracted[1,i] = SFC_RUNOFF_STAN[0,0]*percentage_pavement
	else:
		data_extracted[1,i] = SFC_RUNOFF_STAN[0,0]*percentage_pavement
	# surface runoff from tree
	data_extracted[2,i] = SFC_RUNOFF[0,0]*Percentage_over_pavement_tree
	# percentage over yard
	data_extracted[3,i] = SFC_RUNOFF[0,1]*percentage_over_yard

	# ET from yard
	data_extracted[4,i] = ETRAN[0,1]*percentage_over_yard
	# ET from tree
	data_extracted[5,i] = ETRAN[0,0]*Percentage_over_pavement_tree

	# normal soil moisture
	data_extracted[6,i] = SOIL_M_norm[1]*percentage_over_yard
	# underground runoff
	data_extracted[7,i] = UNDER_RUNOFF[0,1]*percentage_over_yard


np.savetxt(save_loc + '/extracted_data_2018.csv',data_extracted,delimiter=',')


