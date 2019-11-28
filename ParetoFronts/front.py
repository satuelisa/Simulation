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
no_dom = []
for i in range(n):
    d = [domin_by(sign * val[i], sign * val[j]) for j in range(n)]
    no_dom.append(not np.any(d)) # si es cierto que ninguno es verdadero
frente = val[no_dom, :]
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
