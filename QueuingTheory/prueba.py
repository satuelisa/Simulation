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
 
import multiprocessing
from time import time
from scipy.stats import describe # instalar con pip3
 
if __name__ == "__main__":
    d = 100
    h = 200
    replicas = 5
    tiempos = []
    with multiprocessing.Pool() as pool:
        for r in range(replicas):
            antes = time()
            primos = pool.map(primo, range(d, h + 1))
            despues = time()
            tiempos.append(despues - antes)    
    print(describe(tiempos))
