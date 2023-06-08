# import xarray as xr
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
import matplotlib.patches as patches
import matplotlib.lines as lines
import os as os

data_location = '../../intermediate-data/figure3/extract_data_tree_shift/'
data = np.loadtxt(data_location+'tree_shift_2018.csv',delimiter=',')
data2 = np.loadtxt(data_location+'tree_shift_2019.csv',delimiter=',')
data3 = np.loadtxt(data_location+'tree_shift_2020.csv',delimiter=',')

data = (data+data2+data3)/3
## runoff
print("Runnoff standard")
x = data[3,0].round(1) + data[1,0].round(1) + data[2,0].round(1) 
print(x)
print("Runnoff middle")
y = data[3,20].round(1) + data[1,20].round(1) + data[2,20].round(1) 
print(y)
print("Runnoff extreme")
z = data[3,70].round(1) + data[1,70].round(1) + data[2,70].round(1) 
print(z)

# plt.plot(data[,:])
# plt.show()
print('Percentage Diff Middle')
print((y - x)/data[0,0] * 100)

print('Percentage Diff extreme')
print((z - x)/data[0,0] * 100)


## some speciation of the runoff
print('amount reduced by runoff on average from pavement')

runoff_total = data[3,0] + data[2,0] + data[1,0] 
runoff_pavement =  data[3,1:]+ data[2,1:] + data[1,1:]
print((100*(runoff_total - runoff_pavement)/data[0,0]))


## ET
print("ET standard")
x = data[4,0].round(1) + data[5,0].round(1) 
print(x)
print("ET middle")
y = data[4,20].round(1) + data[5,20].round(1) 
print(y)
print("ET extreme")
z = data[4,70].round(1) + data[5,70].round(1) 
print(z)

av = (x - (data[4,1:] + data[5,1:]))/data[0,0]

print(av,np.mean(av))

print(data[4,0] - data[4,70])

# ddd
print('percentage diff average')
print((av-x)/data[0,0] * 100)

print('Percentage Diff Middle')
print((y - x)/data[0,0] * 100)

print('Percentage Diff extreme')
print((z - x)/data[0,0] * 100)

print(np.argmax((data[4,:]+data[5,:])))
print(np.min((data[4,:]+data[5,:])))
# ddd

## Deep Drainage
print("DD standard")
x = data[7,0].round(1) 
print(x)
print("DD middle")
y = data[7,20].round(1)
print(y)
print("DD extreme")
z = data[7,70].round(1) 
print(z)

print('Percentage Diff Middle')
print((y - x)/data[0,0] * 100)

print('Percentage Diff extreme')
print((z - x)/data[0,0] * 100)

print(((data[7,1:]) - x)/data[0,0] * 100)


## Soil Moisture
print("SM standard")
x = data[6,0].round(1) 
print(x)
print("SM middle")
y = data[6,20].round(1) 
print(y)
print("SM extreme")
z = data[6,70].round(1) 
print(z)

print('Percentage Diff Middle')
print((y - x)/data[0,0] * 100)

print('Percentage Diff extreme')
print((z - x)/data[0,0] * 100)

print(np.mean(data[6,1:]) - x) 
print(((data[6,1:]) - x )/data[0,0] * 100)
print(np.argmin(data[6,:]))
print(np.min(data[6,:]))



