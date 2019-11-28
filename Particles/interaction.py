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
colores = [(niveles[i], 0, niveles[-(i + 1)]) for i in range(len(niveles))]
 
import matplotlib.pyplot as plt
import matplotlib.colorbar as colorbar
from matplotlib.colors import LinearSegmentedColormap
 
palette = LinearSegmentedColormap.from_list('tonos', colores, N = len(colores))
 
from math import fabs, sqrt, floor, log
eps = 0.001
def fuerza(i):
    pi = p.iloc[i]
    xi = pi.x
    yi = pi.y
    ci = pi.c
    fx, fy = 0, 0
    for j in range(n):
        pj = p.iloc[j]
        cj = pj.c
        dire = (-1)**(1 + (ci * cj < 0))
        dx = xi - pj.x
        dy = yi - pj.y
        factor = dire * fabs(ci - cj) / (sqrt(dx**2 + dy**2) + eps)
        fx -= dx * factor
        fy -= dy * factor
    return (fx, fy)
 
from os import popen
popen('rm -f p9p_t*.png') # borramos anteriores en el caso que lo hayamos corrido
tmax = 100
digitos = floor(log(tmax, 10)) + 1
fig, ax = plt.subplots(figsize=(6, 5), ncols=1)
pos = plt.scatter(p.x, p.y, c = p.g, s = 70, marker = 's', cmap = palette)
fig.colorbar(pos, ax=ax)
plt.title('Estado inicial')
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(-0.1, 1.1)
plt.ylim(-0.1, 1.1)
fig.savefig('p9p_t0.png')
plt.close()
 
def actualiza(pos, fuerza, de):
    return max(min(pos + de * fuerza, 1), 0)
 
import multiprocessing
from itertools import repeat
 
if __name__ == "__main__":
    for t in range(tmax):
        with multiprocessing.Pool() as pool: # rehacer para que vea cambios en p
            f = pool.map(fuerza, range(n))
            delta = 0.02 / max([max(fabs(fx), fabs(fy)) for (fx, fy) in f])
            p['x'] = pool.starmap(actualiza, zip(p.x, [v[0] for v in f], repeat(delta)))
            p['y'] = pool.starmap(actualiza, zip(p.y, [v[1] for v in f], repeat(delta)))
            fig, ax = plt.subplots(figsize=(6, 5), ncols=1)
            pos = plt.scatter(p.x, p.y, c = p.g, s = 70, marker = 's', cmap = palette)
            fig.colorbar(pos, ax=ax)
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.xlim(-0.1, 1.1)
            plt.ylim(-0.1, 1.1)            
            plt.title('Paso {:d}'.format(t + 1))
            fig.savefig('p9p_t' + format(t + 1, '0{:d}'.format(digitos)) + '.png')
            plt.close()
popen('convert -delay 50 -size 300x300 p9p_t*.png -loop 0 p9p.gif') # requiere ImageMagick
