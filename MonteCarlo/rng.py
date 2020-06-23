inicio = -6.0
final = -inicio
paso = 0.25
X = [inicio]
while X[-1] + paso <= final:
    X.append(X[-1] + paso)
 
from math import exp, pi
def f(x):
    return 1 / (exp(x) + exp(-x))
 
def g(x):
    return (2 / pi) * f(x) # ineficiente, pero claro
 
Y = [g(x) for x in X]
  
from GeneralRandom import GeneralRandom 
import numpy as np
generador = GeneralRandom(np.asarray(X), np.asarray(Y))
muestra = generador.random(50000)[0]
 
from matplotlib import rc
import matplotlib.pyplot as plt
 
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.hist(muestra, bins = X, normed = True, align = 'right')
plt.plot(X, Y)
plt.title('Histograma de $g(x)$ comparado con $g(x)$')
plt.xlabel(r'$x$')
plt.ylabel(r'$\frac{2}{\pi} (\exp(x) + \exp(-x))^{-1}$')
plt.savefig('p5pm.png')
plt.show() # opcional
plt.close()
