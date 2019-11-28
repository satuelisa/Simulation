import numpy as np
import pandas as pd
from random import randint, random
 
def poli(maxdeg, varcount, termcount):
    f = []
    for t in range(termcount):
        var = randint(0, varcount - 1)
        deg = randint(1, maxdeg)
        f.append({'var': var, 'coef': random(), 'deg': deg})
    return pd.DataFrame(f)
  
def evaluate(pol, var):
    return sum([t.coef * var[pol.at[i, 'var']]**t.deg for i, t in pol.iterrows()])
 
 
def domin_by(target, challenger):
    if np.any(challenger < target):
        return False
    return np.any(challenger > target)
 
vc = 4
md = 3
tc = 5
k = 2 # cuantas funciones objetivo
obj = [poli(md, vc, tc) for i in range(k)]
minim = np.random.rand(2) > 0.5
n = 250 # cuantas soluciones aleatorias
sol = np.random.rand(n, vc)
val = np.zeros((n, k))
for i in range(n): # evaluamos las soluciones
    for j in range(k):
        val[i, j] = evaluate(obj[j], sol[i])
sign = [1 + -2 * m for m in minim]
mejor1 = np.argmax(sign[0] * val[:, 0])
mejor2 = np.argmax(sign[1] * val[:, 1])
cual = {True: 'min', False: 'max'}
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6), dpi=300)        
plt.plot(val[:, 0], val[:, 1], 'o', fillStyle = 'none')
plt.xlabel('Primer objetivo')
plt.ylabel('Segundo objetivo')
plt.title('Ejemplo bidimensional')
plt.savefig('p11p_init.png', bbox_inches='tight')
plt.close()
fig = plt.figure(figsize=(8, 6), dpi=300)        
ax = plt.subplot(111)
ax.plot(val[:, 0], val[:, 1], 'o', color = 'k', fillStyle = 'none')
ax.plot(val[mejor1, 0], val[mejor1, 1], 's', color = 'blue') 
ax.plot(val[mejor2, 0], val[mejor2, 1], 'o', color = 'orange') 
plt.xlabel('Primer objetivo ({:s}) mejor con cuadro azul'.format(cual[minim[0]])) 
plt.ylabel('Segundo objetivo ({:s}) mejor con bolita naranja'.format(cual[minim[1]])) 
plt.title('Ejemplo bidimensional')
plt.savefig('p11p_mejores.png', bbox_inches='tight')
plt.close()
dom = []
for i in range(n):
    d = [domin_by(sign * val[i], sign * val[j]) for j in range(n)]
    dom.append(sum(d)) 
frente = val[[d == 0 for d in dom], :]
fig = plt.figure(figsize=(8, 6), dpi=300)        
ax = plt.subplot(111)
ax.plot(val[:, 0], val[:, 1], 'o', color = 'k', fillStyle = 'none')
# para opciones de colores, ver https://matplotlib.org/examples/color/named_colors.html
ax.plot(frente[:, 0], frente[:, 1], 'o', color = 'lime') 
plt.xlabel('Primer objetivo ({:s})'.format(cual[minim[0]])) 
plt.ylabel('Segundo objetivo ({:s})'.format(cual[minim[1]])) 
plt.title('Ejemplo bidimensional')
plt.savefig('p11p_frente.png', bbox_inches='tight')
plt.close()
# lo que resta fue adaptado de
# https://matplotlib.org/3.1.0/gallery/statistics/customized_violin.html
fig, ax = plt.subplots(nrows = 1, ncols = 1, figsize=(4, 12))
plt.ylabel('Frecuencia')
plt.title('Cantidad de soluciones dominantes')
parts = ax.violinplot(dom, showmeans=False, showmedians=False, showextrema=False)
for p in parts['bodies']:
    p.set_facecolor('orange')
    p.set_edgecolor('red')
    p.set_alpha(1)
# agregamos la caja con cuartiles y mediana encima del violin
d = sorted(dom)
m = np.median(d)
q1, m, q3 = np.percentile(d, [25, 50, 75])
ax.scatter(1, m, marker = '_', color = 'lime', s = 100, zorder = 3)
ax.vlines(1, q1, q3, color = 'blue', linestyle = '-', lw = 20)
 
# basemos el filtrado de datos anomales en 
# https://stackoverflow.com/questions/11686720/is-there-a-numpy-builtin-to-reject-outliers-from-a-list
def is_outlier(d, iqr = 0.5):
    p = (1 - iqr) / 2
    s = pd.Series(d)
    qlow, med, qhigh = s.quantile([p, 0.50, 1 - p])
    iqr = qhigh - qlow
    return ((s - med).abs() > iqr).values
 
out = is_outlier(d)
from itertools import compress
y = list(compress(d, out)) # anomales
x = [1] * len(y)
ax.scatter(x, y, marker = 'o', color = 'lime', s = 3, zorder = 3)
a = list(compress(d, ~np.array(out))) # no anomales
low, high = a[0], a[-1]
# agregamos el eje 
ax.vlines(1, low, high, color = 'lime', linestyle = '-', lw = 2)
# los bigotes del eje
ax.scatter([1, 1], [low, high], color = 'lime', marker = '_', s = 100, zorder = 3)
ax.get_xaxis().set_tick_params(direction = 'out')
ax.set_xticks([])
ax.set_xlabel('')
plt.subplots_adjust(bottom = 0.5, wspace = 0.02)
plt.savefig('p11p_violin.png', bbox_inches = 'tight')
plt.close()
