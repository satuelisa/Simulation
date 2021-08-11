from timeit import timeit
from sys import getsizeof
import numpy as np


n = 2**12
M = np.random.rand(n, n)
print(n)
B = getsizeof(M)
kB = B / 2**10
MB = kB / 2**10
GB = MB / 2**10
print(B, kB, MB, GB)
rep = 3

def tem():
    Q = M @ M

print(timeit('tem()', 'from __main__ import tem', number = rep))

