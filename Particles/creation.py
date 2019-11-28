# -*- coding: utf-8 -*
import numpy as np
import pandas as pd
 
n = 50
x = np.random.normal(size = n)
y = np.random.normal(size = n)
c = np.random.normal(size = n)
xmax = max(x)
xmin = min(x)
x = (x - xmin) / (xmax - xmin) # de 0 a 1
ymax = max(y)
ymin = min(y)
y = (y - ymin) / (ymax - ymin) 
cmax = max(c)
cmin = min(c)
c = 2 * (c - cmin) / (cmax - cmin) - 1 # entre -1 y 1
g = np.round(5 * c).astype(int)
p = pd.DataFrame({'x': x, 'y': y, 'c': c, 'g': g})
paso = 256 // 10
niveles = [i/256 for i in range(0, 256, paso)]
print(len(niveles))
colores = [(niveles[i], 0, niveles[-(i + 1)]) for i in range(len(niveles))]
print(colores)
 
import matplotlib.pyplot as plt
import matplotlib.colorbar as colorbar
from matplotlib.colors import LinearSegmentedColormap
 
palette = LinearSegmentedColormap.from_list('tonos', colores, N = len(colores))
 
fig, ax = plt.subplots(figsize=(6, 5), ncols=1)
pos = plt.scatter(p.x, p.y, c = p.g, s = 77, cmap = palette)
fig.colorbar(pos, ax=ax)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Partículas generadas')
plt.savefig('p9pi.png')
plt.close()
