from math import sin, cos, floor, log
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["figure.figsize"] = (20, 5)

def f(x):
    return(5 * cos(14*x - 3) * sin(2*x**2 - 4 * x) + 2 * x**2 - 4 * x)
 
low = -4
high = 7
xf = np.arange(low, high, 0.02)
vf = np.vectorize(f)
yf = vf(xf)

tmax = 500
digitos = floor(log(tmax, 10)) + 1

cuantos = 10
x = np.random.uniform(5.8, 6.2, cuantos) # un valor x PUNTOS ROJOS
menor = None # mejor RAYA VERDE
paso =  0.2 # lejos = local
heating = 1.1
rapido = False
inicio = 10
dibuja = inicio 
for tiempo in range(tmax):
    delta = np.random.uniform(0, paso, cuantos) # puntos rojos mueven
    xizq = x - delta # a la izq
    xder = x + delta # a la der
    fizq = vf(xizq) # altura a la izq
    fder = vf(xder) # altura a la der
    for i in range(cuantos):
        x[i] = xizq[i] if fizq[i] < fder[i] else xder[i] # se va al mas bajo
        if menor is None or f(x[i]) < f(menor):  # si este bajo de lo que habiamos visto
            menor = x[i] # movemos la RAYA VERDE AQUI
            paso *= heating
        if x[i] < low or x[i] > high:
             x[i] = np.random.uniform(low, high, 1)
    if tiempo == dibuja or tiempo <= inicio:
        if tiempo >= inicio:
            if rapido:
                dibuja *= 2
            else:
                dibuja += 20
        plt.xlim(low, high)
        plt.ylim(-10, 120)
        plt.plot(xf, yf) # funcion
        plt.axvline(x = menor, color = 'green') # RAYA VERDE
        plt.scatter(x, vf(x), marker = 'o', color = 'red') # PUNTO ROJO
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('Paso {:d}'.format(tiempo))
        plt.savefig('p7p_t' + format(tiempo, '0{:d}'.format(digitos)) + '.png')
        plt.close()
