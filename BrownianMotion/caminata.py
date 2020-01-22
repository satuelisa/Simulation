from random import random, randint # pseudoaleatorios
 
def caminata(dim, dur, dist):
    pos = [0] * dim
    mayor = 0
    for t in range(dur):
        cambiar = randint(0, dim - 1)
        cambio = 1 if random() < 0.5 else -1
        pos[cambiar] += cambio
        d = dist(pos)
        if d > mayor:
            mayor = d
    return mayor
