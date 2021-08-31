from random import randint

def experimento(eID): # argumento dummy para map
    maximo = 0
    pobl = 1000
    anterior = None
    while pobl > 0:
        pobl -= randint(10, 100)
        if anterior is not None:
            dif = anterior - pobl
            if dif > maximo:
                maximo = dif
        anterior = pobl
    return maximo

from multiprocessing import Pool, cpu_count

if __name__ == '__main__':
    k = cpu_count() - 1
    print(Pool(k).map(experimento, [x for x in range(10)])) # replicas
