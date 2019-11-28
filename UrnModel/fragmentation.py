# -*- coding: utf-8 -* # para incluir acentos
import numpy as np
from random import randint
 
k = 1000
n = 100000
orig = np.random.normal(size = k)
cumulos = orig - min(orig)
cumulos += 1 # ahora el menor vale uno
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
 
c = np.median(cumulos) # tamaño crítico de cúmulos
d = np.std(cumulos) / 4 # factor arbitrario para suavizar la curva
 
from math import exp
def sigmoid(x, c, d):
    return 1 / (1 + exp((c - x) / d))
 
vs = np.vectorize(sigmoid)
x = np.linspace(min(cumulos), max(cumulos), 70)
y = vs(x, c, d)
import matplotlib.pyplot as plt
 
plt.figure(figsize=(7, 7), dpi=300)
plt.scatter(x, y)
plt.axvline(x = c, color = 'red')
plt.xlabel('Tamaño')
plt.ylabel('Probabilidad de fragmentación')
plt.savefig('p8p_sigmoid.png', bbox_inches='tight') 
plt.close()
