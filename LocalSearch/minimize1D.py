from math import cos, floor, log
import matplotlib.pyplot as plt
from random import uniform
import numpy as np
 
def f(x):
    return cos(14.5*x - 0.3) + x * (x + 0.2) + 1.01
 
low = -3
high =  -low
x = np.arange(low, high, 0.05)
vf = np.vectorize(f)
y = vf(x)
tmax = 100
digitos = floor(log(tmax, 10)) + 1
curr = uniform(low, high)
best = curr
step =  0.3
for tiempo in range(tmax):
    delta = uniform(0, step)
    left = curr - delta
    right = curr + delta
    fl = f(left)
    fr = f(right)
    curr = left if fl < fr else right
    if f(curr) < f(best):  # minimizamos
        best = curr
    fig = plt.figure()
    plt.xlim(low, high)
    plt.ylim(-0.5, f(high))
    ax = plt.subplot(1, 1, 1)
    ax.plot(x, vf(x))
    ax.axvline(x = best, color = 'green')    
    ax.scatter(curr, f(curr), marker = 'o', color = 'red')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Paso {:d}'.format(tiempo + 1))
    fig.savefig('p7p_t' + format(tiempo, '0{:d}'.format(digitos)) + '.png')
    plt.close()
