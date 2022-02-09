pos = 0
dur = 1000
mayor = 0
regresos = 0
cat('Caminata de', dur, 'pasos', '\n')
for (paso in 1:dur) {
    if (runif(1) < 0.5) {
        pos = pos + 1
    } else {
        pos = pos - 1
    }
    if (pos == 0) {
        regresos = regresos + 1 # regreso al origen
    }
    mayor = max(mayor, abs(pos))
}
cat('Fueron', regresos, 'regresos', '\n')
cat('La mayor distancia era de', mayor, '\n')
