# -*- coding: utf-8 -* # para incluir acentos
import numpy as np
from random import randint
 
k = 1000
n = 100000
eps = 0.000001
cumulos = np.random.normal(size = k)
cumulos -= min(cumulos)
cumulos += eps # ahora el menor vale epsilon
cumulos = cumulos / sum(cumulos) # ahora suman a uno
cumulos *= n # ahora suman a n, pero son valores decimales
cumulos = np.round(cumulos).astype(int) # ahora son enteros
diferencia = n - sum(cumulos) # por cuanto le hemos fallado
cambio = 1 if diferencia > 0 else -1
while diferencia != 0:
    p = randint(0, k - 1)
    if cambio > 0 or (cambio < 0 and cumulos[p] > 0): # sin vaciar
        cumulos[p] += cambio
        diferencia -= cambio
assert sum(cumulos) == n
 
import matplotlib.pyplot as plt
  
plt.hist(cumulos, align = 'right')
plt.title('Estado inicial')
plt.xlabel('Tamaño de cúmulos')
plt.ylabel('Frecuencia absoluta')
plt.savefig('p8p_init.png', bbox_inches='tight') 
plt.close()
