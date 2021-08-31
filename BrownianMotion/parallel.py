from random import random, randint
from distance import ed_orig, md_orig
 
def experimento(dim, eucl):
    pos = [0] * dim
    mayor = 0
    for t in range(50): 
        cambiar = randint(0, dim - 1)
        cambio = 1 if random() < 0.5 else -1
        pos[cambiar] += cambio
        d = ed_orig(pos) if eucl else md_orig(pos)
        mayor = d if d > mayor else mayor
    return (eucl, dim, mayor)
 
import multiprocessing
if __name__ == "__main__":
    parametros = [(d, True) for d in range(1, 9)]
    parametros += [(d, False) for d in range(1, 9)]
    with multiprocessing.Pool() as pool:
        results = pool.starmap_async(experimento, parametros)
        print(results.get())
