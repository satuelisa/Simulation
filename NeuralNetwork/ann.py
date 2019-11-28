from random import randint
from math import floor, log
import pandas as pd
import numpy as np
 
modelos = pd.read_csv('digits.txt', sep=' ', header = None)
modelos = modelos.replace({'n': 0.995, 'g': 0.92, 'b': 0.002})
r, c = 5, 3
dim = r * c
 
tasa = 0.15
tranqui = 0.99
tope = 9
k = tope + 1 # incl. cero
contadores = np.zeros((k, k + 1), dtype = int)
n = floor(log(k-1, 2)) + 1
neuronas = np.random.rand(n, dim) # perceptrones
  
for t in range(5000): # entrenamiento
    d = randint(0, tope)
    pixeles = 1 * (np.random.rand(dim) < modelos.iloc[d])
    correcto = '{0:04b}'.format(d)
    for i in range(n):
        w = neuronas[i, :]
        deseada = int(correcto[i]) # 0 o 1
        resultado = sum(w * pixeles) >= 0
        if deseada != resultado: 
            ajuste = tasa * (1 * deseada - 1 * resultado)
            tasa = tranqui * tasa 
            neuronas[i, :] = w + ajuste * pixeles
 
for t in range(300): # prueba
    d = randint(0, tope)
    pixeles = 1 * (np.random.rand(dim) < modelos.iloc[d])
    correcto = '{0:04b}'.format(d)
    salida = ''
    for i in range(n):
        salida += '1' if sum(neuronas[i, :] * pixeles) >= 0 else '0'
    r = min(int(salida, 2), k)
    contadores[d, r] += 1
c = pd.DataFrame(contadores)
c.columns = [str(i) for i in range(k)] + ['NA']
c.index = [str(i) for i in range(k)]
print(c)
