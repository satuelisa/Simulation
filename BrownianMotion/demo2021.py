dim = 3
pos = [0] * dim
from random import random, randint
resultados = []
repeticiones = 100
for replica in range(repeticiones):
    nunca = True
    for paso in range(1000):
        cual = randint(0, dim - 1)
        pos[cual] = pos[cual] + 1 if random() < 0.5 else pos[cual] - 1
        if all([p == 0 for p in pos]):
            resultados.append(paso)
            nunca = False
            break
    if nunca:
        resultados.append(None)
cuantos = sum([r is None for r in resultados])
print(cuantos / repeticiones, 'no regresaron nunca')
if cuantos < repeticiones: # por lo menos uno ha regresado
    regresaron = sum([r if r is not None else 0 for r in resultados]) 
    print(regresaron / (repeticiones - cuantos), 'fue la tardanza en promedio')
        
    

