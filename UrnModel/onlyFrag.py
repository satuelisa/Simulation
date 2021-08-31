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
 
from math import exp, floor, log
 
def rotura(x, c, d):
    return 1 / (1 + exp((c - x) / d))
 
def union(x, c):
    return exp(-x / c)
 
from random import random
 
def romperse(tam, cuantos):
    res = []
    for cumulo in range(cuantos):
        if random() < rotura(tam, c, d):
            primera = randint(1, tam - 1)
            segunda = tam - primera
            res += [primera, segunda]
        else:
            res.append(tam) # no rompió
    return res
 
import matplotlib.pyplot as plt
 
duracion = 10
digitos = floor(log(duracion, 10)) + 1
xmax = None
 
for paso in range(duracion):
    (tams, freqs) = np.unique(cumulos, return_counts = True)
    cumulos = []
    assert len(tams) == len(freqs)
    for i in range(len(tams)):
        cumulos += romperse(tams[i], freqs[i]) 
    if xmax is None:
        xmax = 1.05 * max(cumulos)
 
    plt.hist(cumulos, align = 'right', density = True)
    plt.title('Estado inicial')
    plt.xlabel('Tamaño')
    plt.ylabel('Frecuencia relativa')
    plt.xlim(0, xmax)
    plt.ylim(0, 0.05)
    plt.title('Paso {:d} con pura rotura'.format(paso + 1))
    plt.savefig('p8p_t' + format(paso, '0{:d}'.format(digitos)) + '.png')
    plt.close()
