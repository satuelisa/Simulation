from random import randint
desde = 1
hasta = 1000
menor = 15
mayor = 21
from time import time # traer libreria
for k in range(menor, mayor + 1):
    n = 2 ** k
    lista = [ randint(desde, hasta) for i in range(n) ]
    antes = time() # ver la hora
    lista.sort()
    despues = time() # volver ver la hora
    diferencia = despues - antes # segundos
    print('ordenar', n, 'elementos toma', diferencia, 'segundos')
print('bye')
