import xarray as xr
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
import matplotlib.patches as patches
import matplotlib.lines as lines
import os as os

data_location = '../../intermediate-data/figure4/permeable_pavement/'
data = np.loadtxt(data_location+'permeable_pav_2018.csv',delimiter=',')
data2 = np.loadtxt(data_location+'permeable_pav_2019.csv',delimiter=',')
data3 = np.loadtxt(data_location+'permeable_pav_2020.csv',delimiter=',')

data = (data+data2+data3)/3
print(data[0,0])
## runoff
print("Runnoff standard")
x = data[1,0].round(1) + data[2,0].round(1) 
print(x)
print("Runnoff middle")
y = data[1,10].round(1) + data[2,10].round(1)
print(y)
print("Runnoff extreme")
z = data[1,5].round(1) + data[2,5].round(1) 
print(z)

dd = data[1,:] + data[2,:]

print('Percentage Diff Middle')
print((y - x)/data[0,0] * 100)

print('Percentage Diff extreme')
print((z - x)/data[0,0] * 100)

## ET
print("ET standard")
x = data[3,0].round(1) + data[4,0].round(1) 
print(x)
print("ET middle")
y = data[3,25].round(1) + data[4,25].round(1) 
print(y)
print("ET extreme")
z = data[3,50].round(1) + data[4,50].round(1) 
print(z)

print('Percentage Diff Middle')
print((y - x)/data[0,0] * 100)

print('Percentage Diff extreme')
print((z - x)/data[0,0] * 100)

## Deep Drainage
print("DD standard")
x = data[6,0].round(1) 
print(x)
print("DD middle")
y = data[6,25].round(1)
print(y)
print("DD extreme")
z = data[6,50].round(1) 
print(z)

print('Percentage Diff Middle')
print((y - x)/data[0,0] * 100)
dd
print('Percentage Diff extreme')
print((z - x)/data[0,0] * 100)

## Soil Moisture
print("SM standard")
x = data[5,0].round(1) 
print(x)
print("SM middle")
y = data[5,25].round(1) 
print(y)
print("SM extreme")
z = data[5,50].round(1) 
print(z)

print('Percentage Diff Middle')
print((y - x)/data[0,0] * 100)

print('Percentage Diff extreme')
print((z - x)/data[0,0] * 100)