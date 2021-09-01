import numpy as np # instalar numpy con pip
from random import random
import matplotlib.cm as cm
import matplotlib.pyplot as plt

dim = 100
num = dim**2
p = 0.25
valores = [1 * (random() < p) for i in range(num)]
actual = np.reshape(valores, (dim, dim))

def mapeo(pos):
    fila = pos // dim
    columna = pos % dim
    return actual[fila, columna]

assert all([mapeo(x) == valores[x]  for x in range(num)])

def paso(pos):
    fila = pos // dim
    columna = pos % dim
    vecindad = actual[max(0, fila - 1):min(dim, fila + 2),
                      max(0, columna - 1):min(dim, columna + 2)]
    return 1 * (np.sum(vecindad) - actual[fila, columna] == 3)

dur = 100
lim = 9
seq = 0

if __name__ == "__main__":
    fig = plt.figure()
    plt.imshow(actual, interpolation='nearest', cmap=cm.Greys)
    fig.suptitle('Estado inicial')
    plt.savefig('p2_t0_p.png')
    plt.close()
    for iteracion in range(dur):
        valores = [paso(x) for x in range(num)]
        vivos = sum(valores)
        print(iteracion, vivos)
        if vivos == 0:
            break; # nadie vivo
        actual = np.reshape(valores, (dim, dim))
        if dur - iteracion < 9:  
            fig = plt.figure()
            plt.imshow(actual, interpolation='nearest', cmap=cm.Greys)
            fig.suptitle('Paso {:d}'.format(iteracion + 1))
            plt.savefig('p2_t{:d}_p.png'.format(seq))
            seq += 1
            plt.close()
# para crear un GIF, se puede usar ImageMagick con
# convert -delay 100 -size 300x300 -loop 0 p2_t*.png p2p.gif
