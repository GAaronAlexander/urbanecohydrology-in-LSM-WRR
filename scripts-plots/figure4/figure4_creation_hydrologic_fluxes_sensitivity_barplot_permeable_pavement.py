import xarray as xr
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
import matplotlib.patches as patches
import matplotlib.lines as lines
import os as os

data_location = '../../intermediate-data/figure4/permeable_pavement/'
save_location = './'


data = np.loadtxt(data_location+'permeable_pav_2020.csv',delimiter=',')
data2 = np.loadtxt(data_location+'permeable_pav_2019.csv',delimiter=',')
data3 = np.loadtxt(data_location+'permeable_pav_2018.csv',delimiter=',')

data = (data+data2+data3)/3

figure, ax1 = plt.subplots(nrows=1,ncols=1,figsize=(25,12))
# ax1.axis('off')
x = np.linspace(0,51,52)


for i in range(0,71):

	if i == 0:
		plt.bar(0,data[0,0],width=.995,color='#103138',zorder=10,edgecolor='k')
	else:
		if (i+20) > 70: 
			break 
		bottom_loop = 0

		plt.bar(x[i],data[5,i],width=.995,color='#4F5D70',zorder=10,bottom=0,edgecolor='k')
		if data[5,i] > 0:
			bottom_loop += data[5,i]
		
		
		# plt.bar(10+i, data_stan[1,0]*((i+10)*0.2)/100,width=0.995,color='#103138',zorder=10,edgecolor='k')
		# bottom_loop += data_stan[1,0]*((i+10)*0.2)/100

		# print((i)/100 * .3, (i)/100 * .7)
		# print((100-i)/100)

		plt.bar(x[i],data[1,i],width=.995,color='#103138',zorder=10,bottom=bottom_loop,edgecolor='k')
		bottom_loop += data[1,i]
		print(data[1])

		plt.bar(x[i], data[2,i],width=.995,color='#103138',bottom=bottom_loop,zorder=10,edgecolor='k')
		bottom_loop += data[2,i]



		plt.bar(x[i], data[3,i],width=.995,color='#4FA635',bottom=bottom_loop,zorder=10,edgecolor='k')
		bottom_loop += data[3,i]
		

		# # # plt.bar(i/2,data[6,i],width=0.495, zorder=100,bottom=bottom_loop,color='#4F5D70',edgecolor='k',alpha=0.3)
		# # # bottom_loop += data[6,i]


		plt.bar(x[i], data[6,i],width=.995,color='#8F6132',zorder=10,bottom=bottom_loop,edgecolor='k')
		bottom_loop += data[6,i]


ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.tick_params(width=2,length=15)
plt.plot([-1,101],[data[0,0],data[0,0]],color='k',linewidth=3,zorder=1000)
plt.plot([-1,101],[0,0],color='#BDBBBF',linewidth=4,zorder=50)
plt.xlim([-1,51])

plt.ylim([-50,860])

print(np.arange(90,31,10))


plt.xlabel('Permeable Pavement (%)',fontsize=50)
plt.xticks(fontsize=40)
plt.yticks(fontsize=40)
plt.ylabel('Water Depth (mm)',fontsize=50)
# ax1.legend(['Surface Runoff','Etran: Yard','Etran: Pavement','Soil Storage','Underground Runoff'])



plt.tight_layout()
# plt.show()
plt.savefig(save_location+'permeable_pavement_VAR_DEPTH_all_LARGETEXT.png',dpi=400)
plt.close()
