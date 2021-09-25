from math import sqrt, pi, fabs
import matplotlib.pyplot as plt
from random import random
import pandas as pd
data = []

def rng():
    return 2 * random() - 1

for n in [100, 1000, 10000, 100000]:
    for replica in range(15):
        est = 4 * (sum([sqrt(rng()**2 + rng()**2) < 1 for i in range(n)]) / n)
        data.append([n, fabs(est - pi)])

datos = pd.DataFrame(data, columns = ['Sample size', 'Error'])
plot = datos.boxplot('Error', by = 'Sample size')
plt.show()
