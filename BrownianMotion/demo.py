from random import random, randint

def paso(pos, dim):
    d = randint(0, dim - 1)
    pos[d] += -1 if random() < 0.5 else 1
    return pos

def experimento(largo, dim):
    pos = [0] * dim
    for t in range(largo):
        pos = paso(pos, dim)
        if all([p == 0 for p in pos]):
            return True
    return False

dim = 1
largo = 1000
total = 10000
regresos = 0
for replica in range(total):
    regresos += experimento(largo, dim)
print(regresos / total)
        
