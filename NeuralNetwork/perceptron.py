import numpy as np
tasa = 0.15 # tasa de aprendizaje
tranqui = 0.95 # se va bajando con ajustes hechos
dim = 2
w = np.random.rand(dim) # pesos del perceptron, al azar inicialmente
dibuja = True
  
if dibuja:
    xT = []
    yT = []
    xF = []
    yF = []
    xi = -1
    xf = 2
  
# contadores
tP = 0 # true positive (ambos son 1)
fP = 0 # da true aunque era false
tN = 0 # true negative (ambos son 0)
fN = 0 # da false aunque era true
tmax = 60 # pasos en total
 
from math import ceil, floor, log
entrenamiento = int(ceil(0.7 * tmax))
prueba = tmax - entrenamiento # probamos despues de entrenar
 
from os import popen
if dibuja:
    dl = floor(log(tmax, 10)) + 1
    popen('rm -f p12p_t*.png')
    import matplotlib.pyplot as plt    
 
from random import random
for t in range(tmax):
    entrada = np.random.rand(2)
    x, y = entrada[0], entrada[1]
    deseada = x > y # true si estamos debajo del diagonal 
    resultado = sum(w * entrada) >= 0 # producto interno y comparasion
    if t <= entrenamiento: # aprende durante entrenamiento
        if deseada != resultado:  # pero hubo un error en la salida
            ajuste = tasa * (1 * deseada - 1 * resultado)
            tasa = tranqui * tasa # ajustamos menos cada vez
            w = w + ajuste * entrada
            bien = False
        else:
            bien = True
        if dibuja:
            fase = "Fase de entrenamiento,"
            if deseada:
                xT.append(x)
                yT.append(y)
            else:
                xF.append(x)
                yF.append(y)
    else: # responde en la fase prueba
        if deseada == resultado:
            bien = True
            if deseada:
                tP += 1
            else:
                tN += 1
        else:
            bien = False
            if deseada: # resultado negativo (queriamos positivo)
                fN += 1 
            else: # resultado positivo (queriamos negativo)
                fP += 1
        if dibuja:
            fase = "Fase de prueba,"
    if dibuja:
        pendiente = -w[0] / w[1]
        fig = plt.figure(figsize = (7, 7), dpi = 300)        
        ax = plt.subplot(111)
        if len(xT) > 0:
            ax.plot(xT, yT, 's', color = 'gray')
        if len(xF) > 0:
            ax.plot(xF, yF, 'o', color = 'gray')        
        yi = pendiente * xi
        yf = pendiente * xf
        ax.plot([xi, xf], [yi, yf], 'b-', linewidth = 3)
        plt.xlim(-0.1, 1.1)
        plt.ylim(-0.1, 1.1)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('{:s} paso {:d}'.format(fase, t + 1))
        if bien:
            ax.plot([x], [y], marker = '^', color = 'lime', markersize = 15)
        else: # la deseada no fue correcta
            ax.plot([x], [y], marker = 'D', color = 'red', markersize = 15)
        plt.savefig('p12p_t' + format(t + 1, '0{:d}'.format(dl)) + '.png', bbox_inches='tight')
        plt.close()    
if dibuja:
    popen('convert -delay 50 -size 300x300 p12p_t*.png -loop 0 p12p.gif')
print('Bien')
print(tP, tN)
print('Mal')
print(fP, fN)
