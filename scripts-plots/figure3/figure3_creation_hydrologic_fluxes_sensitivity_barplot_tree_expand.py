import xarray as xr
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
import matplotlib.patches as patches
import matplotlib.lines as lines
import os as os

'''
This creates a barplot that is relative to the tree over pavement flux volume. e.g. i = 10 is 5% more urban tree canopy. 
Data labels are added in adobe illustrator
'''

data_location = '../../intermediate-data/figure3/extract_data_tree_expansion/'
save_loc = './'
data = np.loadtxt(data_location+'extracted_data_2018.csv',delimiter=',')
data2 = np.loadtxt(data_location+'extracted_data_2019.csv',delimiter=',')
data3 = np.loadtxt(data_location+'extracted_data_2020.csv',delimiter=',')

data_growing_tree = (data+data2+data3)/3 # now season averages 


figure, ax1 = plt.subplots(nrows=1,ncols=1,figsize=(25,12))
# ax1.axis('off')
for i in range(0,71):

	plt.bar(i/2,data_growing_tree[6,i],width=0.995/2, zorder=100,bottom=0,color='#4F5D70',edgecolor='k')
	

	bottom_loop = 0
	
	plt.bar(i/2, data_growing_tree[1,i],width=0.995/2,color='#103138',zorder=10,edgecolor='k')
	bottom_loop += data_growing_tree[1,i]

	
	plt.bar(i/2, data_growing_tree[2,i],width=0.995/2,color='#2D679E',bottom=bottom_loop,zorder=10,edgecolor='k')
	bottom_loop += data_growing_tree[2,i]



	plt.bar(i/2, data_growing_tree[3,i],width=0.995/2,color='#35A0B8',bottom=bottom_loop,zorder=10,edgecolor='k')
	bottom_loop += data_growing_tree[3,i]
	
	plt.bar(i/2,data_growing_tree[4,i],width=0.995/2,color='#4FA635',zorder=10,bottom=bottom_loop,edgecolor='k')
	bottom_loop += data_growing_tree[4,i]
	
	plt.bar(i/2,data_growing_tree[5,i],width=0.995/2,color='#74916D',zorder=10,bottom=bottom_loop,edgecolor='k')
	bottom_loop += data_growing_tree[5,i]

	



	plt.bar(i/2, data_growing_tree[7,i],width=0.995/2,color='#8F6132',zorder=10,bottom=bottom_loop,edgecolor='k')
	bottom_loop += data_growing_tree[7,i]

	


ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.tick_params(width=2,length=15)
plt.plot([-1,72],[data_growing_tree[0,0],data_growing_tree[0,0]],color='k',linewidth=4,zorder=1000)
plt.plot([-1,72],[0,0],color='#BDBBBF',linewidth=4,zorder=50)

plt.xlim([-1,70.5/2])
plt.ylim([-95,860])

plt.xlabel('Tree Over Pavement (%)',fontsize=50)
plt.xticks(fontsize=40)
plt.yticks(fontsize=40)
plt.ylabel('Water Depth (mm)',fontsize=50)




plt.tight_layout()
# plt.show()
plt.savefig(save_loc+'average_tree_canopy_tree_expand_siltloam_largetext.png',dpi=400)
plt.close()
