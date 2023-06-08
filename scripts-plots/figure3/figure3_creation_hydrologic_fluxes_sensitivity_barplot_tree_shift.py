import xarray as xr
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
import matplotlib.patches as patches
import matplotlib.lines as lines
import os as os

data_location = '../../intermediate-data/figure3/extract_data_tree_shift/'
save_loc = './'
data = np.loadtxt(data_location+'tree_shift_2018.csv',delimiter=',')
data2 = np.loadtxt(data_location+'tree_shift_2019.csv',delimiter=',')
data3 = np.loadtxt(data_location+'tree_shift_2020.csv',delimiter=',')

data = (data+data2+data3)/3
# plt.plot(data[1:,:].sum(axis=0) - data[0,:])
# plt.show()
# dd
figure, ax1 = plt.subplots(nrows=1,ncols=1,figsize=(25,12))
# ax1.axis('off')
for i in range(0,71):

	plt.bar(i/2,data[6,i],width=0.995/2, zorder=100,bottom=0,color='#4F5D70',edgecolor='k')
	
	bottom_loop = 0
	
	plt.bar(i/2, data[1,i],width=0.995/2,color='#103138',zorder=10,edgecolor='k')
	bottom_loop += data[1,i]

	
	plt.bar(i/2, data[2,i],width=0.995/2,color='#2D679E',bottom=bottom_loop,zorder=10,edgecolor='k')
	bottom_loop += data[2,i]



	plt.bar(i/2, data[3,i],width=0.995/2,color='#35A0B8',bottom=bottom_loop,zorder=10,edgecolor='k')
	bottom_loop += data[3,i]
	
	plt.bar(i/2,data[4,i],width=0.995/2,color='#4FA635',zorder=10,bottom=bottom_loop,edgecolor='k')
	bottom_loop += data[4,i]
	
	plt.bar(i/2,data[5,i],width=0.995/2,color='#74916D',zorder=10,bottom=bottom_loop,edgecolor='k')
	bottom_loop += data[5,i]

	


	plt.bar(i/2, data[7,i],width=0.995/2,color='#8F6132',zorder=10,bottom=bottom_loop,edgecolor='k')
	bottom_loop += data[7,i]



ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.tick_params(width=2,length=15)
plt.plot([-1,72],[data[0,0],data[0,0]],color='k',linewidth=4,zorder=1000)
plt.plot([-1,72],[0,0],color='#BDBBBF',linewidth=4,zorder=50)

plt.xlim([-1,70.5])
plt.ylim([-95,860])

plt.xlabel('Tree Over Pavement (%)',fontsize=50)
plt.xticks(fontsize=40)
plt.yticks(fontsize=40)
plt.ylabel('Water Depth (mm)',fontsize=50)
# ax1.legend(['Surface Runoff','Etran: Yard','Etran: Pavement','Soil Storage','Underground Runoff'])



plt.tight_layout()
# plt.show()
plt.savefig(save_loc+'average_tree_canopy_shift_tree_siltloam_largetext.png',dpi=400)
plt.close()
