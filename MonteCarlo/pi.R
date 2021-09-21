muchos = 100000
interior = 0

for (r in 1:muchos) {
    x = runif(1, -1, 1)
    y = runif(1, -1, 1)
    d = sqrt(x*x + y*y)
    if (d < 1) {
        interior = interior + 1
    }
}

tasa = interior / muchos
pi = 4 * tasa
print(pi)
