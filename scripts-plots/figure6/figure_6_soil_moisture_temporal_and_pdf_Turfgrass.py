import xarray as xr
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
import matplotlib.patches as patches
import matplotlib.lines as lines
import seaborn as sns
from sklearn.neighbors import KernelDensity

data_loc = '/Users/aaronalexander/Google Drive/My Drive/dissertation_chapter1_data/raw_outputs_from_cheyenne/three_season_turgrass_with_disconnect/'
save_loc = './'

dates = pd.date_range(start='2018-04-01 00:05:00',end='2020-11-01 00:00:00', freq='5T')
data_standard = xr.open_dataset(data_loc+'/turf_grass_three_season/201804010000.LDASOUT_DOMAIN1')
data_dis_50 = xr.open_dataset(data_loc+'turfgrass_with_some_disconnect_30/201804010000.LDASOUT_DOMAIN1')
data_dis_100 = xr.open_dataset(data_loc+'/turfgrass_with_some_disconnect_60/201804010000.LDASOUT_DOMAIN1')

soil_m_standard = data_standard.SOIL_M[1:,0,0]*100/2000 + data_standard.SOIL_M[1:,0,1]*400/2000 + data_standard.SOIL_M[1:,0,2]*600/2000 + data_standard.SOIL_M[1:,0,3]*1000/2000
soil_m_dis_50 = data_dis_50.SOIL_M[1:,0,0]*100/2000 + data_dis_50.SOIL_M[1:,0,1]*400/2000 + data_dis_50.SOIL_M[1:,0,2]*600/2000 + data_dis_50.SOIL_M[1:,0,3]*1000/2000
soil_m_dis_100 = data_dis_100.SOIL_M[1:,0,0]*100/2000 + data_dis_100.SOIL_M[1:,0,1]*400/2000 + data_dis_100.SOIL_M[1:,0,2]*600/2000 + data_dis_100.SOIL_M[1:,0,3]*1000/2000




figure, (ax1,ax2) = plt.subplots(nrows=1,ncols=2,figsize=(45,12),gridspec_kw={'width_ratios': [3.2, 1],'height_ratios':[1]})

ax1.plot(soil_m_standard.Time,soil_m_standard[:,1],color='k',linewidth=7.0)
ax1.plot(soil_m_dis_50.Time,soil_m_dis_50[:,1],color='#B084BB',linewidth=7.0)
ax1.plot(soil_m_dis_100.Time,soil_m_dis_100[:,1],color='#6F3D7D',linewidth=7.0)


ax1.fill_betweenx([0,1],pd.to_datetime('20180501'),pd.to_datetime('20181101'),color='#DED2B7',alpha=0.3)
ax1.fill_betweenx([0,1],pd.to_datetime('20190501'),pd.to_datetime('20191101'),color='#DED2B7',alpha=0.3)
ax1.fill_betweenx([0,1],pd.to_datetime('20200501'),pd.to_datetime('20201101'),color='#DED2B7',alpha=0.3)


ax1.grid(which='major',axis='both',linestyle='--',color='k',linewidth=1.5)
ax1.set_ylim([0.2,0.5])
ax1.set_xlim([pd.to_datetime('20180501'),pd.to_datetime('20201101')])

ax1.set_xlabel('Time',fontsize=55)
ax1.tick_params(axis='both', which='major', labelsize=45)
ax1.set_ylabel(r'Soil Moisture [m$^3$ m$^{-3}$]',fontsize=55)

plt.tight_layout()




## create pdf of soil moisture 

date_drop1 = pd.date_range(start='2018-11-01 00:05:00',end='2019-04-30 23:55:00', freq='5T')

soil_m_standard = soil_m_standard.drop_sel(Time=date_drop1)
soil_m_dis_50 = soil_m_dis_50.drop_sel(Time=date_drop1)
soil_m_dis_100 = soil_m_dis_100.drop_sel(Time=date_drop1)

date_drop2 = pd.date_range(start='2019-11-01 00:05:00',end='2020-04-30 23:55:00', freq='5T')

soil_m_standard = soil_m_standard.drop_sel(Time=date_drop2)
soil_m_dis_50 = soil_m_dis_50.drop_sel(Time=date_drop2)
soil_m_dis_100 = soil_m_dis_100.drop_sel(Time=date_drop2)


soil_m_standard = soil_m_standard.dropna('Time')
soil_m_dis_50 = soil_m_dis_50.dropna('Time')
soil_m_dis_100  = soil_m_dis_100.dropna('Time')


X_plot = np.linspace(0.15, .6, 401)[:, np.newaxis]

kde = KernelDensity(kernel="gaussian", bandwidth=0.005).fit(soil_m_standard[:,1].values.reshape(-1,1))
log_dens = kde.score_samples(X_plot.reshape(-1,1))
CDF_stan = np.exp(log_dens)*(X_plot[1] - X_plot[0])



plt.plot(X_plot,CDF_stan,color='k',linewidth=7)

# kde = KernelDensity(kernel="gaussian", bandwidth=0.005).fit(soil_m_plotwise[:,1].values.reshape(-1,1))
# log_dens = kde.score_samples(X_plot.reshape(-1,1))
# # sns.displot(data=[soil_m_standard[:,1].values,soil_m_plotwise[:,1].values],kind="kde")

# plt.plot(X_plot,np.exp(log_dens),color='#179C30',linewidth=5.0)

kde_50 = KernelDensity(kernel="gaussian", bandwidth=0.005).fit(soil_m_dis_50[:,1].values.reshape(-1,1))
log_dens_50 = kde_50.score_samples(X_plot.reshape(-1,1))

CDF_50 = np.exp(log_dens_50)*(X_plot[1] - X_plot[0])

plt.plot(X_plot,CDF_50,color='#B084BB',linewidth=7.0)

## plotwise 35% tree
kde_100 = KernelDensity(kernel="gaussian", bandwidth=0.01).fit(soil_m_dis_100[:,1].values.reshape(-1,1))
log_dens_100 = kde_100.score_samples(X_plot.reshape(-1,1))
CDF_100 = np.exp(log_dens_100)*(X_plot[1] - X_plot[0])
ax2.plot(X_plot,CDF_100,color='#6F3D7D',linewidth=7.0)

ax2.grid(which='major',axis='both',linestyle='--',color='k',linewidth=1.5)
ax2.set_xlabel(r'Soil Moisture [m$^3$ m$^{-3}$]',fontsize=55)
ax2.tick_params(axis='both', which='major', labelsize=45)
ax2.set_ylabel(r'Probability',fontsize=55)

ax2.set_xlim([0.2,0.53])
#ax2.set_ylim([-0.01,0.03])

ax2.set_yticks([0,0.01,0.02,0.03])
ax2.set_yticklabels([0,0.01,0.02,0.03])

ax2.set_xticks([0.20,0.30,0.40,0.50])
ax2.set_xticklabels([0.20,0.30,0.40,0.50])

plt.tight_layout()

plt.tight_layout()
plt.savefig(save_loc+'soil_moisture_turfgrass_PDF.png',dpi=300)
# plt.show()
