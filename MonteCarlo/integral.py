from math import exp, pi
import numpy as np
def g(x):
    return (2  / (pi * (exp(x) + exp(-x))))
 
vg = np.vectorize(g)
X = np.arange(-8, 8, 0.05) # ampliar y refinar
Y = vg(X) # mayor eficiencia
 
from GeneralRandom import GeneralRandom
generador = GeneralRandom(np.asarray(X), np.asarray(Y))
desde = 3
hasta = 7
pedazo = 50000
cuantos = 500
def parte(replica):
    V = generador.random(pedazo)[0]
    return ((V >= desde) & (V <= hasta)).sum() 
 
import multiprocessing
if __name__ == "__main__":
    with multiprocessing.Pool() as pool:
        montecarlo = pool.map(parte, range(cuantos))
        integral = sum(montecarlo) / (cuantos * pedazo)
        print((pi / 2) * integral)
