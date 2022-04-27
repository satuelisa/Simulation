def knapsack(peso_permitido, objetos):
    peso_total = sum([objeto[0] for objeto in objetos])
    valor_total = sum([objeto[1] for objeto in objetos])
    if peso_total < peso_permitido: # cabe todo
        return valor_total
    else:
        cantidad = len(objetos)
        V = dict()
        for w in range(peso_permitido + 1):
            V[(w, 0)] = 0
        for i in range(cantidad):
            (peso, valor) = objetos[i]
            for w in range(peso_permitido + 1):
                cand = V.get((w - peso, i), -float('inf')) + valor
                V[(w, i + 1)] = max(V[(w, i)], cand)
        return max(V.values())

from sys import argv
cuantos = int(argv[1])

from random import randint
peso = [ randint(1, 10 * cuantos) for x in range(cuantos) ]
peso.sort()
valor = [ randint(10, 100 * cuantos) for x in range(cuantos) ]
objetos = [(p, v) for (p, v) in zip(peso, valor)]
print(objetos[:5])
print(objetos[-5:])
capacidad = sum(peso) // 2
print(capacidad)
print(knapsack(capacidad, objetos))
