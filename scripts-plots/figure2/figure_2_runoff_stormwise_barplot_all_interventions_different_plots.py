import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

'''
This is currently set up to sort the storms
and then create a dual bar plot and percentage difference

Created by G. Aaron Alexander
'''
data_shift=np.loadtxt('../../intermediate-data/figure2/three_season_tree_shifttree_siltloam_12hourwindow.csv',delimiter=',')
data_share=np.loadtxt('../../intermediate-data/figure2/three_season_tree_sharetree_siltloam_12hourwindow.csv',delimiter=',')
data_turf= np.loadtxt('../../intermediate-data/figure2/three_season_turfgrass_12hourwindow.csv',delimiter=',') 
data_pavement = np.loadtxt('../../intermediate-data/figure2t/three_season_permeable_pavement_12hourwindow.csv',delimiter=',') 

data_rainfall = np.loadtxt('../../intermediate-data/figure2/RAINFALL_12hour_EVENT_WINDOW.csv',delimiter=',')

# indicies = np.argsort(data_rainfall,axis=0)
# print(np.linspace(0,124,125))
# print(data_pavement[-1,indicies[::-1]][0])
# dd

#share tree
typical = data_share[0,:]
reduced = data_share[-1,:]


indicies = np.argsort(data_rainfall,axis=0)
rain_sorted = np.take_along_axis(data_rainfall,indicies,axis=0)
print(rain_sorted.shape)

typical_sorted = np.take_along_axis(typical,indicies,axis=0)

reduced_sorted = np.take_along_axis(reduced,indicies,axis=0)


percentage_diff_share = 100*(typical_sorted-reduced_sorted)/typical_sorted 
x = np.argmin(percentage_diff_share)
print(percentage_diff_share)
print(x,rain_sorted[x])

difference_typical_min_reduced_share= typical_sorted - reduced_sorted

# shift tree
typical2 = data_shift[0,:]
reduced2 = data_shift[-1,:]

typical_sorted2 = np.take_along_axis(typical2,indicies,axis=0)

reduced_sorted2 = np.take_along_axis(reduced2,indicies,axis=0)

percentage_diff_shift = 100*(typical_sorted2-reduced_sorted2)/typical_sorted2 
x = np.argmin(percentage_diff_shift)
print(x,rain_sorted[x])


difference_typical_min_reduced_shift = typical_sorted2 - reduced_sorted2

# turf grass 
typical3 = data_turf[0,:]
reduced3 = data_turf[-1,:]


typical_sorted3 = np.take_along_axis(typical3,indicies,axis=0)

reduced_sorted3 = np.take_along_axis(reduced3,indicies,axis=0)

percentage_diff_turf = 100*(typical_sorted3-reduced_sorted3)/typical_sorted3 
x = np.argmin(percentage_diff_turf)
print(x,rain_sorted[x])

difference_typical_min_reduced_turf = typical_sorted3 - reduced_sorted3


# pavement 
typical4 = data_pavement[0,:]
reduced4 = data_pavement[26,:]

typical_sorted4 = np.take_along_axis(typical4,indicies,axis=0)
reduced_sorted4 = np.take_along_axis(reduced4,indicies,axis=0)


percentage_diff_pavement = 100*(typical_sorted4-reduced_sorted4)/typical_sorted4

x = np.argmin(percentage_diff_pavement)
print(percentage_diff_pavement)
print(124-x,rain_sorted[x])

# xxxxx
difference_typical_min_reduced_pavement = typical_sorted4 - reduced_sorted4 

#Difference plot
figure, (ax1,ax3,ax4,ax5,ax2) = plt.subplots(nrows=5,ncols=1,figsize=(30,34),sharex=True,gridspec_kw={'height_ratios': [1, 1, 1,1, 1.7]})


ax2.plot(np.linspace(0,124,125),percentage_diff_share[::-1],linewidth=4,linestyle='--',marker='o',dash_capstyle='round',markersize=18,color='#0C65C4',zorder=1000,label='"Extra" Tree Canopy')
ax2.plot(np.linspace(0,124,125),percentage_diff_shift[::-1],linewidth=4,linestyle='--',marker='^',dash_capstyle='round',markersize=18,color='#26A33A',zorder=1000,label='"Shifting" Tree Canopy')
ax2.plot(np.linspace(0,124,125),percentage_diff_turf[::-1],linewidth=4,linestyle='--',marker='d',dash_capstyle='round',markersize=18,color='#6F3D7D',zorder=1002,label='Downspout Disconnect')
ax2.plot(np.linspace(0,124,125),percentage_diff_pavement[::-1],linewidth=4,linestyle='--',marker='$X$',dash_capstyle='round',markersize=15,color='#8C5F32',zorder=1000,label='Permeable Pavement')


ax2.legend(frameon=False,fontsize=40,loc='right',bbox_to_anchor=(0.999, 0.59))
ax2.plot([-5,130],[0,0],linewidth=4,color='k',zorder=1)

# 


ax2.set_xticks([0,11.5,29,80])

ax2.set_yticks([0,20,40,60,80,100])

ax2.set_yticklabels([0,20,40,60,80,100],fontsize=50)

# ax1.set_xlim([-2.5,125])
ax2.set_xlim([-2.5,125])
ax2.set_ylim([0,101])
# ax1.set_ylim([-70,17])
ax2.grid(visible=True,which='major',axis='both',linewidth=1,linestyle='--',color='#A3A3A3')

ax2.set_ylabel('Reduction \nin Runoff [%]',fontsize=60)



ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)

# expansion
ax1.bar(np.linspace(-0.5,124,125),-1*reduced_sorted[::-1],width=.75,edgecolor='k',color='#0C65C4',alpha=1,label='Runoff Complete Downspout Discconect Scenario',zorder=10)
ax1.bar(np.linspace(-0.5,124,125),difference_typical_min_reduced_share[::-1],width=0.75,edgecolor='k',color='#767A79',alpha=1,label='Extra Runoff from Typical',zorder=10)

ax1.set_yticks([-75,-50, -25, 0, 15 ])
ax1.set_yticklabels([75,50, 25, 0, 15],fontsize=50)
ax1.set_xticks([])

ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.spines['bottom'].set_visible(False)

ax1.set_xlim([-2.5,125])
ax1.set_ylim([-70,17])
ax1.plot([-5,130],[0,0],linewidth=1,color='k',zorder=1)

#shift 
ax3.bar(np.linspace(-0.5,124,125),-1*reduced_sorted2[::-1],width=.75,edgecolor='k',color='#26A33A',alpha=1,label='Runoff Complete Downspout Discconect Scenario',zorder=10)
ax3.bar(np.linspace(-0.5,124,125),difference_typical_min_reduced_shift[::-1],width=0.75,edgecolor='k',color='#767A79',alpha=1,label='Extra Runoff from Typical',zorder=10)

ax3.set_yticks([-75,-50, -25, 0, 15 ])
ax3.set_yticklabels([75,50, 25, 0, 15],fontsize=50)
ax3.set_xticks([])

ax3.spines['right'].set_visible(False)
ax3.spines['top'].set_visible(False)
ax3.spines['bottom'].set_visible(False)

ax3.set_xlim([-2.5,125])
ax3.set_ylim([-70,17])
ax3.plot([-5,130],[0,0],linewidth=1,color='k',zorder=1)


# turf
ax4.bar(np.linspace(-0.5,124,125),-1*reduced_sorted3[::-1],width=.75,edgecolor='k',color='#6F3D7D',alpha=1,label='Runoff Complete Downspout Discconect Scenario',zorder=10)
ax4.bar(np.linspace(-0.5,124,125),difference_typical_min_reduced_turf[::-1],width=0.75,edgecolor='k',color='#767A79',alpha=1,label='Extra Runoff from Typical',zorder=10)

ax4.set_yticks([-30,-15, 0, 15 ,30])
ax4.set_yticklabels([30,15, 0, 15,30],fontsize=50)
ax4.set_xticks([])

ax4.spines['right'].set_visible(False)
ax4.spines['top'].set_visible(False)
ax4.spines['bottom'].set_visible(False)

ax4.set_xlim([-2.5,125])
ax4.set_ylim([-32,32])
ax4.plot([-5,130],[0,0],linewidth=1,color='k',zorder=1)

# permeable 
ax5.bar(np.linspace(-0.5,124,125),-1*reduced_sorted4[::-1],width=.75,edgecolor='k',color='#8C5F32',alpha=1,label='Runoff Complete Downspout Discconect Scenario',zorder=10)
ax5.bar(np.linspace(-0.5,124,125),difference_typical_min_reduced_pavement[::-1],width=0.75,edgecolor='k',color='#767A79',alpha=1,label='Extra Runoff from Typical',zorder=10)

ax5.set_yticks([-60, -30 , 0, 30,  60 ])
ax5.set_yticklabels([60, 30, 0,30,60 ],fontsize=50)
ax5.set_xticks([])

ax5.spines['right'].set_visible(False)
ax5.spines['top'].set_visible(False)
ax5.spines['bottom'].set_visible(False)

ax5.set_xlim([-2.5,125])
ax5.set_ylim([-75,75])
ax5.plot([-5,130],[0,0],linewidth=1,color='k',zorder=1)

ax2.set_xticks([1,11.5,29,56,80])
ax2.set_xticklabels([130,50,25,10,5],fontsize=55)
plt.tight_layout()
plt.savefig('./all_storm_labels_var_depth_small_4Jun2023.png',dpi=600)

plt.close()









