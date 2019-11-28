import matplotlib.pyplot as plt
from random import uniform
from math import cos, sin
import numpy as np
 
def f(x): # ligeros cambios
    return 5 * cos(14*x - 3) * sin(2*x**2 - 4 * x) + 2 * x**2 - 4 * x
 
low = -2
high = 4
step =  0.25
replicas = 100
 
def replica(t):
    curr = uniform(low, high)
    best = curr
    for tiempo in range(t):
        delta = uniform(0, step)
        l = curr - delta
        r = curr + delta
        curr = l if f(l) < f(r) else r
        if f(curr) < f(best): 
            best = curr
    return best
 
x = np.arange(low, high, 0.05)
vf = np.vectorize(f)
y = vf(x)
 
import multiprocessing
from itertools import repeat
 
if __name__ == "__main__":
    with multiprocessing.Pool() as pool:
        for p in range(2, 5):
            r = pool.map(replica, repeat(10**p, replicas))
            q = vf(r)
            fig = plt.figure(figsize=(8, 3), dpi=300)
            plt.xlim(low, high)
            plt.ylim(-8, 20)
            ax = plt.subplot(1, 1, 1)
            ax.plot(x, vf(x))
            ax.axvline(x = r[np.argmin(q)], color = 'green')    
            ax.scatter(r, q, marker = 'o', color = 'red')
            plt.xlabel('x')
            plt.ylabel('f(x)')
            plt.title('{:d} pasos'.format(10**p))
            fig.savefig('p7p_{:d}.png'.format(p), bbox_inches='tight')
            plt.close()
