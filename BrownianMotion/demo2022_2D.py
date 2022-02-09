from random import random
from math import fabs, sqrt

pos = [ 0, 0 ] # dos dimensiones
dur = 1000
mayor = 0
regresos = 0
print('Caminata de', dur, 'pasos')
for paso in range(dur):
    # elegir eje (vertical o horizontal)
    eje = 0 if random() < 0.5 else 1 
    if random() < 0.5:
        pos[eje] += 1
    else:
        pos[eje] -= 1
    if all([ p == 0 for p in pos ]): # si ambos son ceros
        regresos += 1 # regreso al origen
    # raiz de la suma de los cuardados de las coordenadas
    euclideana = sqrt(sum([ p**2 for p in pos ]))
    mayor = max(mayor, euclideana)
print('Fueron', regresos, 'regresos')
print('La mayor distancia era de', mayor)
