from random import randint, random
from math import fabs
import pandas as pd
data = []
largos = [100, 1000, 10000]

for dimension in range(2, 6):
    for duracion in largos:
    	for replica in range(5):
            pos = [0] * dimension
            mayor = 0
            for t in range(duracion):
                cambiar = randint(0, dimension - 1)
                cambio = 1
                if random() < 0.5:
                    cambio = -1
                pos[cambiar] += cambio
                d = sum([fabs(p) for p in pos])
                if d > mayor:
                    mayor = d
            resultado = [dimension, duracion, replica, mayor]
            data.append(resultado)

datos = pd.DataFrame(data, columns = ['Dim', 'Dur', 'Rep', 'Dist'])

print('INICIO')
print(datos.head())
print('FINAL')
print(datos.tail())
