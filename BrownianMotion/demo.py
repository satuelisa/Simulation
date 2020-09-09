from random import random, randint

def paso(pos, dim):
    d = randint(0, dim - 1)
    pos[d] += -1 if random() < 0.5 else 1
    return pos

dim = 50
largo = 1000000
pos = [0] * dim
for t in range(largo):
    pos = paso(pos, dim)
print(pos)
