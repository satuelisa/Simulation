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
  
vc = 4
md = 3
tc = 5
k = 2 # cuantas funciones objetivo
obj = [poli(md, vc, tc) for i in range(k)]
n = 100 # cuantas soluciones aleatorias
sol = np.random.rand(n, vc)
val = np.zeros((n, k))
for i in range(n): # evaluamos las soluciones
    for j in range(k):
        val[i, j] = evaluate(obj[j], sol[i])
 
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6), dpi=300)        
plt.plot(val[:, 0], val[:, 1], 'o', fillStyle = 'none', color = 'k')
plt.xlabel('Primer objetivo')
plt.ylabel('Segundo objetivo')
plt.title('Ejemplo bidimensional')
plt.savefig('p11p_init.png', bbox_inches='tight')
plt.close()
