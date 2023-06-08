import xarray as xr
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
import matplotlib.patches as patches
import matplotlib.lines as lines
import os as os

data_location = '../../intermediate-data/figure4/downspout_disconnect/'
data = np.loadtxt(data_location+'turfgrass_2018.csv',delimiter=',')
data2 = np.loadtxt(data_location+'turfgrass_2019.csv',delimiter=',')
data3 = np.loadtxt(data_location+'turfgrass_2020.csv',delimiter=',')

data = (data+data2+data3)/3
## runoff
print("Runnoff standard")
x = data[1,0].round(1) + data[2,0].round(1) 
print(x)
print("Runnoff middle")
y = data[1,30].round(1) + data[2,30].round(1)
print(y)
print("Runnoff extreme")
z = data[1,60].round(1) + data[2,60].round(1) 
print(z)

# print('Percentage Diff Middle')
# print((data[1,1:] + data[2,1:] - x)/data[0,0] * 100)

# dd

print('Percentage Diff extreme')
print((z - x)/data[0,0] * 100)



## ET
print("ET standard")
x = data[3,0].round(1) + data[4,0].round(1) 
print(x)
print("ET middle")
y = data[3,30].round(1) + data[4,30].round(1) 
print(y)
print("ET extreme")
z = data[3,60].round(1) + data[4,60].round(1) 
print(z)

print('Percentage Diff Middle')
print((y - x)/data[0,0] * 100)

print('Percentage Diff extreme')
print((z - x)/data[0,0] * 100)

print(data[3,0] - data[3,-1])

print((np.mean(data[3,1:] - data[3,0]))/data[0,0])


## Deep Drainage
print("DD standard")
x = data[6,0].round(1) 
print(x)
print("DD middle")
y = data[6,30].round(1)
print(y)
print("DD extreme")
z = data[6,60].round(1) 
print(z)

print('Percentage Diff Middle')
print((y - x)/data[0,0] * 100)

print('Percentage Diff extreme')
print((z - x)/data[0,0] * 100)

## Soil Moisture
print("SM standard")
x = data[5,0].round(1) 
print(x)
print("SM middle")
y = data[5,30].round(1) 
print(y)
print("SM extreme")
z = data[5,60].round(1) 
print(z)

print('Percentage Diff Middle')
print((y - x)/data[0,0] * 100)

print('Percentage Diff extreme')
print((z - x)/data[0,0] * 100)

print(data[5,0] - data[5,-1])

print((np.mean(data[5,1:] - data[5,0]))/data[0,0])
