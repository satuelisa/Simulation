import seaborn as sns
from math import sqrt
from PIL import Image, ImageColor
from random import randint, choice
 
n, k, semillas = 80, 30, []
for s in range(k):
    while True:
        x, y = randint(0, n - 1), randint(0, n - 1)
        if (x, y) not in semillas:
            semillas.append((x, y))
            break
 
def celda(pos):
    if pos in semillas:
        return semillas.index(pos)
    x, y = pos % n, pos // n
    cercano = None
    menor = n * sqrt(2)
    for i in range(k):
        (xs, ys) = semillas[i]
        dx, dy = x - xs, y - ys
        dist = sqrt(dx**2 + dy**2)
        if dist < menor:
            cercano, menor = i, dist
    return cercano
 
def inicio():
    direccion = randint(0, 3)
    if direccion == 0: # vertical abajo -> arriba
        return (0, randint(0, n - 1))
    elif direccion == 1: # izq. -> der
        return (randint(0, n - 1), 0)
    elif direccion == 2: # der. -> izq.
        return (randint(0, n - 1), n - 1)
    else:
        return (n - 1, randint(0, n - 1))
 
celdas = [celda(i) for i in range(n * n)]
voronoi = Image.new('RGB', (n, n))
vor = voronoi.load()
c = sns.color_palette("Set3", k).as_hex()
for i in range(n * n):
    vor[i % n, i // n] = ImageColor.getrgb(c[celdas.pop(0)])
limite, vecinos = n, []
for dx in range(-1, 2):
    for dy in range(-1, 2):
        if dx != 0 or dy != 0:
            vecinos.append((dx, dy))
 
def propaga(replica):
    prob, dificil = 0.9, 0.8
    grieta = voronoi.copy()
    g = grieta.load()
    (x, y) = inicio()
    largo = 0
    negro = (0, 0, 0)
    while True:
        g[x, y] = negro
        largo += 1
        frontera, interior = [], []
        for v in vecinos:
            (dx, dy) = v
            vx, vy = x + dx, y + dy
            if vx >= 0 and vx < n and vy >= 0 and vy < n: # existe
               if g[vx, vy] != negro: # no tiene grieta por el momento
                   if vor[vx, vy] == vor[x, y]: # misma celda
                       interior.append(v)
                   else:
                       frontera.append(v)
        elegido = None
        if len(frontera) > 0:
            elegido = choice(frontera)
            prob = 1
        elif len(interior) > 0:
            elegido = choice(interior)
            prob *= dificil
        if elegido is not None:
            (dx, dy) = elegido
            x, y = x + dx, y + dy
        else:
            break # ya no se propaga
    if largo >= limite:
        visual = grieta.resize((10 * n,10 * n))
        visual.save("p4pg_{:d}.png".format(replica))
    return largo
 
for r in range(10): # pruebas sin paralelismo
    propaga(r)

