from math import ceil, sqrt
def primo(n):
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(ceil(sqrt(n))), 2):
        if n % i == 0:
            return False
    return True
 
from scipy.stats import describe # instalar con pip3
from random import shuffle
import multiprocessing
from time import time
if __name__ == "__main__":
    desde = 1000
    hasta = 3000
    original = [x for x in range(desde, hasta + 1)]
    invertido = original[::-1]
    aleatorio = original.copy()
    replicas = 10
    tiempos = {"ot": [], "it": [], "at": []}
    with multiprocessing.Pool() as pool:
        for r in range(replicas):
            t = time()
            pool.map(primo, original)
            tiempos["ot"].append(time() - t)
            t = time()
            pool.map(primo, invertido)
            tiempos["it"].append(time() - t)
            shuffle(aleatorio)
            t = time()
            pool.map(primo, aleatorio)
            tiempos["at"].append(time() - t)
    for tipo in tiempos:
        print(describe(tiempos[tipo]))
