import seaborn as sns 
from random import randint
from PIL import Image, ImageColor 
from math import sqrt

def celda(pos):
    y = pos // n
    x = pos % n
    if pos in semillas:
        return semillas.index(pos)
    cercano = None
    menor = n * sqrt(2)
    for i in range(k):
        (xs, ys) = semillas[i]
        dx = x - xs
        dy = y - ys
        dist = sqrt(dx**2 + dy**2)
        if dist < menor:
            cercano = i
            menor = dist
    return cercano

n = 100
k = 50
semillas = []
for s in range(k):
    while True:
        x = randint(0, n - 1)
        y = randint(0, n - 1)
        if (x, y) not in semillas:
            semillas.append((x, y))
            break
celdas = [celda(i) for i in range(n * n)]
zona = Image.new('RGB', (n, n))
p = zona.load()
c = sns.color_palette("Set3", k).as_hex()
for i in range(n * n):
    s = celdas.pop(0)
    p[i % n, i // n] = ImageColor.getrgb(c[s])
visual = zona.resize((10 * n,  10 * n))
visual.show()
visual.save("p4pc.png")
