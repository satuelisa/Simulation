import pandas as pd 
import matplotlib.pyplot as plt
from math import floor, log, sqrt
from random import random, uniform
 
l = 1.5
n = 50
pi = 0.05
pr = 0.02 # prob. de recuperar
v = l / 30
r = 0.1
tmax = 100
digitos = floor(log(tmax, 10)) + 1
c = {'I': 'r', 'S': 'g', 'R': 'orange'}
m = {'I': 'o', 'S': 's', 'R': '2'}
 
agentes =  pd.DataFrame()
agentes['x'] = [uniform(0, l) for i in range(n)]
agentes['y'] = [uniform(0, l) for i in range(n)]
agentes['dx'] = [uniform(-v, v) for i in range(n)]
agentes['dy'] = [uniform(-v, v) for i in range(n)]
agentes['estado'] = ['S' if random() > pi else 'I' for i in range(n)]
epidemia = []
for tiempo in range(tmax):
    conteos = agentes.estado.value_counts()
    infectados = conteos.get('I', 0)
    epidemia.append(infectados)
    if infectados == 0:
        break
    contagios = [False for i in range(n)]
    for i in range(n): # contagios
        a1 = agentes.iloc[i]
        if a1.estado == 'I':
            for j in range(n):
                a2 = agentes.iloc[j]
                if a2.estado == 'S':
                    d = sqrt((a1.x - a2.x)**2 + (a1.y - a2.y)**2)
                    if d < r:
                        if random() < (r - d) / r:
                            contagios[j] = True
    for i in range(n): # movimientos
        a = agentes.iloc[i]
        if contagios[i]:
            agentes.at[i, 'estado'] = 'I'
        elif a.estado == 'I': # ya infectado
            if random() < pr:
                agentes.at[i, 'estado'] = 'R'
        x = a.x + a.dx
        y = a.y + a.dy
        x = x if x < l else x - l
        y = y if y < l else y - l
        x = x if x > 0 else x + l
        y = y if y > 0 else y + l
        agentes.at[i, 'x'] = x
        agentes.at[i, 'y'] = y
    fig = plt.figure()
    ax = plt.subplot(1, 1, 1)
    plt.xlim(0, l)
    plt.ylim(0, l)
    for e, d in agentes.groupby('estado'):
        if len(d) > 0:
            ax.scatter(d.x, d.y, c = c[e], marker = m[e])
    plt.xlabel('x')
    plt.xlabel('y')
    plt.title('Paso {:d}'.format(tiempo + 1))
    fig.savefig('p6p_t' + format(tiempo, '0{:d}'.format(digitos)) + '.png')
    plt.close()
plt.figure(figsize=(8, 3), dpi=300)
plt.plot(range(len(epidemia)), [100 * e / n for e in epidemia], 'bo')
plt.xlabel('Tiempo')
plt.ylabel('Porcentaje de infectados')
plt.savefig('p6pe.png', bbox_inches='tight')
plt.close()
