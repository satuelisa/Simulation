from random import random
n = 100
p = 0.7
celda = [1 * (random() < p) for x in range(n)]
m = 0
a = 0
for c in celda:
 if not c:
     if a > m:
         m = a
     a = 0
 else:
     a += 1
m = max(m, a)
print(m)
