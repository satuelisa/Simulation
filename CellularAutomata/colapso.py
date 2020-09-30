from random import randint

def experimento():
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

if __name__ == "__main__":
    for replica in range(10):
        print('mayor colapso', experimento())
