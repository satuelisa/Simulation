# -*- coding: utf-8 -* # para incluir acentos
import numpy as np
import seaborn as sns
from random import randint
 
k = 1000
n = 100000
orig = np.random.normal(size = k)
cumulos = orig - min(orig)
cumulos += 1 # ahora el menor vale uno
cumulos = cumulos / sum(cumulos) # ahora suman a uno
cumulos *= n # ahora suman a n, pero son valores decimales
cumulos = np.round(cumulos).astype(int) # ahora son enteros
diferencia = n - sum(cumulos) # por cuanto le hemos fallado
cambio = 1 if diferencia > 0 else -1
while diferencia != 0:
    p = randint(0, k - 1)
    if cambio > 0 or (cambio < 0 and cumulos[p] > 0): # sin vaciar
        cumulos[p] += cambio
        diferencia -= cambio
assert sum(cumulos) == n
 
import matplotlib.pyplot as plt
from scipy.stats import shapiro
from statsmodels.graphics.gofplots import qqplot
 
plt.figure(figsize=(12, 12), dpi=300)
 
plt.subplot(221)
sns.distplot(orig, hist=True, kde=True, color = 'darkblue', hist_kws={'edgecolor':'black'}, kde_kws={'linewidth': 4})
plt.title('Datos generados originales')
plt.xlabel('Tamaño de cúmulos')
plt.ylabel('Probabilidad')
 
print(shapiro(orig))
ax = plt.subplot(222)
qqplot(orig, line = '45', ax = ax)
ax.set_title('Gráfico de cuantil-cuantil')
ax.set_xlabel('Cuantiles teóricas')
ax.set_ylabel('Cuantiles de la muestra')
 
plt.subplot(223)
sns.distplot(cumulos, hist=True, kde=True, color = 'darkblue', hist_kws={'edgecolor':'black'}, kde_kws={'linewidth': 4})
plt.title('Cúmulos resultantes')
plt.xlabel('Tamaño de cúmulos')
plt.ylabel('Probabilidad')
 
print(shapiro(cumulos))
ax = plt.subplot(224)
qqplot(cumulos, line = '45', ax = ax, fit = True)
ax.set_title('Gráfico de cuantil-cuantil')
ax.set_xlabel('Cuantiles teóricas')
ax.set_ylabel('Cuantiles de la muestra')
 
plt.savefig('p8p_norm.png') 
plt.close()
