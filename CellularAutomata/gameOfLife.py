import numpy as np # hay que instalar numpy a parte con pip3 o algo similar
from random import random
import matplotlib.cm as cm
import matplotlib.pyplot as plt
 
dim = 10
num = dim**2
valores = [round(random()) for i in range(num)]
actual = np.reshape(valores, (dim, dim))
fig = plt.figure()
plt.imshow(actual, interpolation='nearest', cmap=cm.Greys)
plt.savefig('p2p.png')
 
def paso(pos):
    fila = (pos - 1) // dim
    columna = (pos - 1) % dim
    vecindad = actual[(fila - 1):(fila + 2), (columna - 1):(columna + 2)]
    return 1 * (np.sum(vecindad) - actual[fila, columna] == 3)
 
import multiprocessing
if __name__ == "__main__":
    for iteracion in range(9):
        valores = None
        with multiprocessing.Pool() as pool: # rehacer para ver cambios en actual
            valores = pool.map(paso, range(num))
        if np.sum(valores) == 0:
            print('Ya no queda nadie vivo.')
            break;
        actual = np.reshape(valores, (dim, dim))
        fig = plt.figure()
        plt.imshow(actual, interpolation='nearest', cmap=cm.Greys)
        fig.suptitle('Paso {:d}'.format(iteracion + 1))
        plt.savefig('p2_t{:d}_p.png'.format(iteracion))
