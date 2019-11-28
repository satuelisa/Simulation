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
 
def unirse(tam, cuantos):
    res = []
    for cumulo in range(cuantos):
        if random() < union(tam, c):
            res.append(-tam) # marcamos con negativo los que quieren unirse
        else:
            res.append(tam)
    return res
 
from scipy.stats import itemfreq
from numpy.random import shuffle
import matplotlib.pyplot as plt
 
duracion = 10
digitos = floor(log(duracion, 10)) + 1
 
for paso in range(duracion):
    freq = itemfreq(cumulos)    
    l = freq.shape[0]
    cumulos = []    
    for i in range(l):
        urna = freq[i]
        cumulos += unirse(urna[0], urna[1])
    cumulos = np.asarray(cumulos)
    neg = cumulos < 0
    a = len(cumulos)
    juntarse = -1 * np.extract(neg, cumulos) # sacarlos y hacerlos positivos
    cumulos = np.extract(~neg, cumulos).tolist() # los demás en una lista
    assert a == len(juntarse) + len(cumulos)
    nt = len(juntarse)
    if nt > 0:
        if nt > 1:
            shuffle(juntarse) # orden aleatorio
            for i in range(nt // 2):
                cumulos.append(juntarse[2*i] + juntarse[2*i+1])
        if nt % 2 == 1: # fue una cantidad impar
            cumulos.append(juntarse[-1]) # el ultimo
    plt.hist(cumulos, align = 'right', normed = True)
    plt.xlabel('Tamaño')
    plt.ylabel('Frecuencia relativa')
    plt.ylim(0, 0.05)
    plt.title('Paso {:d} con pura unión'.format(paso + 1))
    plt.savefig('p8p_ut' + format(paso, '0{:d}'.format(digitos)) + '.png')
    plt.close()
