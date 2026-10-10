
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

COLOR = 'blue'
LINE_WIDTH = 1.5

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

x=c1["effort"]/1000
sec_x = c1["generation"]

y0 = M[0,:]
y1 = M[1,:]
y2 = M[2,:]
y3 = M[3,:]
y4 = M[4,:]
        
fig, (ax1, ax2) = plt.subplots(1,2, figsize=(12, 6))

#==============================FIRST GRAPH==================================================
ax1.plot(x, y0, label='1-Coev', markevery=25, marker='o', mec='black')
ax1.plot(x, y1, label='1-Coev-RS', markevery=25, marker='^', mec='black')
ax1.plot(x, y2, label='1-Evol-RS', markevery=25, marker='v', mec='black')
ax1.plot(x, y3, label='2-Coev', markevery=25, marker='*', mec='black')
ax1.plot(x, y4, label='2-Coev-RS', markevery=25, marker='s', mec='black')
ax1.set_ylabel('Odsetek wygranych gier [%]')
ax1.set_xlabel(r'Liczba rozegranych gier ($\times 1000$)')
ax_top = ax1.twiny()
ax_top.set_xlabel("Pokolenie")
ax1.set_xlim((0,500))
ax1.set_ylim((0.6,1))
ax1.set_xticks([0, 100, 200, 300, 400, 500])
ax_top.set_xticks([0,40,80,120,160,200])
ax1.grid(True, linestyle = 'dashed', color='#c3cbc4')
ax1.legend()
#==============================FIRST GRAPH==================================================


#==============================SECOND GRAPH==================================================
last_generation = [file.iloc[-1, 2:] * 100 for file in files]
x_labels = ['1-Coev', '1-Coev-RS', '1-Evol-RS', '2-Coev', '2-Coev-RS']
mean_props = dict(
    marker = 'o',
    markerfacecolor = COLOR,
    markeredgecolor = 'black'
)
whisher_props = dict(
    color = COLOR,
    linestyle = 'dashed',
    linewidth = LINE_WIDTH
)
box_props = dict(
    color = COLOR,
    linewidth = LINE_WIDTH
)


ax2.boxplot(last_generation, notch=True, showmeans=True, sym='b+', meanprops = mean_props, whiskerprops=whisher_props, boxprops = box_props)
ax2.grid(True, linestyle='dashed', color='#c3cbc4')
ax2.set_ylim((60,100))
ax2.yaxis.tick_right()
ax2.set_xticklabels(x_labels)
#==============================SECOND GRAPH==================================================

plt.savefig('KCK_plot.pdf')
plt.show()
plt.close()