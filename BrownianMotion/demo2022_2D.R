pos = c(0, 0) # dos-dimensional
dur = 1000
mayor = 0
regresos = 0
cat('Caminata de', dur, 'pasos', '\n')
for (paso in 1:dur) {
    eje = 0
    if (runif(1) < 0.5) {
        eje = 1 # horizontal
    } else {
        eje = 2 # vertical
    }
    if (runif(1) < 0.5) {
        pos[eje] = pos[eje] + 1
    } else {
        pos[eje] = pos[eje] - 1
    }
    if (all(pos == 0)) { # si ambos son ceros
        regresos = regresos + 1 # regreso al origen
    }
    manhattan = sum(abs(pos)) # suma de los valores absolutos
    mayor = max(mayor, manhattan)
}
cat('Fueron', regresos, 'regresos', '\n')
cat('La mayor distancia (Manhattan) era de', mayor, '\n')
