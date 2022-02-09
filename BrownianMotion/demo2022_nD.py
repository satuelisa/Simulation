from random import random, randint
from math import fabs, sqrt

dim = 7 # cuantas dimensiones
pos = [ 0 ] * dim
dur = 1000
mayor = 0
regresos = 0
print('Caminata de', dur, 'pasos en', dim, 'dimensiones')
for paso in range(dur):
    eje = randint(0, dim - 1) # elegir eje (van 0, 1, ..., dim - 1)
    if random() < 0.5:
        pos[eje] += 1
    else:
        pos[eje] -= 1
    if all([ p == 0 for p in pos ]): # si todos son ceros
        regresos += 1 # regreso al origen
    # raiz de la suma de los cuardados de las coordenadas
    euclideana = sqrt(sum([ p**2 for p in pos ]))
    mayor = max(mayor, euclideana)
print('Fueron', regresos, 'regresos')
print('La mayor distancia era de', mayor)
