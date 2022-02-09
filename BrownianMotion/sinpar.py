# -*- coding: utf-8 -*-

from random import random, randint
from math import fabs, sqrt
from random import getrandbits, randint
import matplotlib.pyplot as plt # instalar con pip3

dur = 200
replicas = 100
results = [] # almacen de dimensiones
for dim in range(1, 9): # de uno a ocho
    mayores = [] # almacen de replicas
    for rep in range(replicas):
        pos = [0] * dim # origen
        mayor = 0
        for paso in range(dur):
            eje = randint(0, dim - 1) # elegir eje (van 0, 1, ..., dim - 1)
            if random() < 0.5:
                pos[eje] += 1
            else:
                pos[eje] -= 1
            mayor = max(mayor, sqrt(sum([ p**2 for p in pos ])))
        mayores.append(mayor) # replica terminada
    results.append(mayores) # dimension procesada
fig, ax = plt.subplots()
ax.boxplot(results) 
ax.set_xlabel('Dimensión')
ax.set_ylabel('Distancia máxima')
ax.set_title('Distancia Euclideana')
plt.savefig('figuraPy.png') # mandar a un archivoa
plt.close()
