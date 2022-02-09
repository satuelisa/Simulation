from random import random, randint
from math import fabs, sqrt

dim = 3 # cuantas dimensiones
dur = 5000
replicas = 30 # cuantas veces
mayores = []
regresos = []
print(replicas, 'caminatas de', dur, 'pasos en', dim, 'dimensiones')
for replica in range(replicas): 
    pos = [ 0 ] * dim
    mayor = 0
    re = 0
    for paso in range(dur):
        eje = randint(0, dim - 1) # elegir eje (van 0, 1, ..., dim - 1)
        if random() < 0.5:
            pos[eje] += 1
        else:
            pos[eje] -= 1
        if all([ p == 0 for p in pos ]): # si todos son ceros
            re += 1 # regreso al origen
        mayor = max(mayor, sqrt(sum([ p**2 for p in pos ])))
    regresos.append(re)
    mayores.append(mayor)
print('Regresos:')
print('Menor cantidad de regresos: ', min(regresos))
print('Mayor cantidad de regresos: ', max(regresos))
print('Cantidad de regresos en promedio: ', sum(regresos) / len(regresos))
print('Distancias maximales:')
print('Menor valor: ', min(mayores))
print('Mayor valor: ', max(mayores))
print('Promedio: ', sum(mayores) / len(mayores))


