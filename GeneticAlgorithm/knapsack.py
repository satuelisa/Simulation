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
 
peso = [1, 2, 4, 5, 5, 8, 12] # ordenados de menor a mayor
valor = [3, 8, 24, 7, 10, 12, 30]
objetos = [(p, v) for (p, v) in zip(peso, valor)]
print(knapsack(40, objetos))
