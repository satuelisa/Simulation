# -*- coding: utf-8 -*-
 
from random import getrandbits, randint
import matplotlib.pyplot as plt # instalar con pip3
from math import sqrt, fabs
import multiprocessing # instalar con pip3
 
def experimento(dim, dur, eucl):
    pos = [0] * dim
    mayor = 0
    delta = getrandbits(dur)
    for t in range(dur):
        pos[randint(0, dim - 1)] += 1 if delta % 2 == 0 else -1
        delta >>= 1
    mayor = max(mayor, sqrt(sum([p**2 for p in pos])) if eucl else sum([fabs(p) for p in pos]))
    return mayor
 
if __name__ == "__main__":
    dimension = [d for d in range(1, 9)] # de uno a ocho
    duracion = 200
    replicas = 100
    results = None
    p = [(d, duracion, True) for d in dimension]
    p += [(d, duracion, False) for d in dimension]
    param = p * replicas
    with multiprocessing.Pool() as pool:
        results = pool.starmap(experimento, param)
    eucl = [[] for d in dimension]
    manh = [[] for d in dimension]
    for p in param:
        value = results.pop(0)
        d = p[0] - 1
        if p[2]: # euclideana
         eucl[d].append(value)
        else: # manhattan
            manh[d].append(value)
    fig, ax = plt.subplots()
    ax.boxplot(eucl)
    ax.set_xlabel('Dimensión')
    ax.set_ylabel('Distancia máxima')
    ax.set_title('Euclideana')
    plt.savefig('p1ep.png')
    plt.close()
    fig, ax = plt.subplots()
    ax.boxplot(manh)
    ax.set_xlabel('Dimensión')
    ax.set_ylabel('Distancia máxima')
    ax.set_title('Manhattan')
    plt.savefig('p1mp.png')
    plt.close()
