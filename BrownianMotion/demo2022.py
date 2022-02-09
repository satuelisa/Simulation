from random import random
from math import fabs

pos = 0
dur = 1000
mayor = 0
regresos = 0
print('Caminata de', dur, 'pasos')
for paso in range(dur):
    if random() < 0.5:
        pos += 1
    else:
        pos -= 1
    if pos == 0:
        regresos +=1 # regreso al origen
    mayor = max(mayor, int(fabs(pos)))
print('Fueron', regresos, 'regresos')
print('La mayor distancia era de', mayor)
