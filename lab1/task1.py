
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

c1 = pd.read_csv('dane/1c.csv')
crs1 = pd.read_csv('dane/1crs.csv')
ers1 = pd.read_csv('dane/1ers.csv')
c2 = pd.read_csv('dane/2c.csv')
crs2 = pd.read_csv('dane/2crs.csv')

files = [c1, crs1, ers1, c2, crs2]
M = np.zeros((len(files), files[0].shape[0]))

for index, file in enumerate(files): 
    for i in range(file.shape[0]):
        M[index,i] = file.iloc[i,2:].mean()

y0 = M[0,:]
y1 = M[1,:]
y2 = M[2,:]
y3 = M[3,:]
y4 = M[4,:]
        
plt.plot(c1['effort'], y0, label='1-Coev')
plt.plot(c1['effort'], y1, label='1-Coev-RS')
plt.plot(c1['effort'], y2, label='1-Evol-RS')
plt.plot(c1['effort'], y3, label='2-Coev')
plt.plot(c1['effort'], y4, label='2-Coev-RS')
plt.ylabel('Odsetek wygranych gier')
plt.xlabel('Liczba rozegranych gier')
plt.margins(x=0)
plt.legend()

print(c1.head())
plt.show()