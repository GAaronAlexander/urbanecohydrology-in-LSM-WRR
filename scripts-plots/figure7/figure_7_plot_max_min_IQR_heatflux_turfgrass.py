import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set_style('ticks')
data_hfx_siltloam = np.loadtxt('../../intermediate-data/figure7/extract_data_turfgrass/HFX_extracted_max_min_turfgrass.csv',delimiter=',')
data_lh_siltloam = np.loadtxt('../../intermediate-data/figure7/extract_data_turfgrass/LH_extracted_max_min_turfgrass.csv',delimiter=',')

print(data_lh_siltloam[0,0] - data_lh_siltloam[0,-1])

# data_hfx_clayloam = np.loadtxt('../data/extract_data_share_tree/season_max_min_heatfluxes/HFX_extracted_max_min_shifttree_clayloam.csv',delimiter=',')
# data_lh_clayloam = np.loadtxt('../data/extract_data_share_tree/season_max_min_heatfluxes/LH_extracted_max_min_shifttree_clayloam.csv',delimiter=',')

figure = plt.figure(figsize=(12,9))
ax1 = plt.subplot(111)

ax1.plot(np.linspace(0,60,61),data_hfx_siltloam[0,:],linewidth=4.0,color='#A31712',label='Sensible')
ax1.plot(np.linspace(0,60,61),data_lh_siltloam[0,:],linewidth=4.0,color='#1A41B8',label='Latent')

ax1.fill_between(np.linspace(0,60,61), data_hfx_siltloam[1,:],data_hfx_siltloam[2,:],alpha=0.3,color='#A31712')
ax1.fill_between(np.linspace(0,60,61), data_lh_siltloam[1,:],data_lh_siltloam[2,:],alpha=0.3,color='#1A41B8')



ax1.set_xlim([-1,61])
ax1.set_xticks([0,15,30,45,60])
ax1.set_xticklabels([0,25,50,75,100])
ax1.set_xlabel('Impervious Disconnection (%)',fontsize=40)
ax1.tick_params(axis='both', which='major', labelsize=30)

ax1.set_ylabel(r'Heat Flux [$W m^{-2}$]',fontsize=40)


ax1.set_ylim([-90,410])
ax1.grid(True,'major','both',color='#ADABA8',linestyle='--')
gridlines = ax1.yaxis.get_gridlines()
gridlines[1].set_color("k")
gridlines[1].set_linewidth(2.5)



ax1.grid(True,linestyle='--',linewidth=2.0)
plt.tight_layout()
plt.savefig('./peak_heatfluxes_and_IQR_turfgrass.png',dpi=500)
