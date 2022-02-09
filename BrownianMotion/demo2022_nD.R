dim = 5 # cuantas dimensiones
pos = rep(0, 5)
dur = 1000
mayor = 0
regresos = 0
cat('Caminata de', dur, 'pasos', '\n')
for (paso in 1:dur) {
    # elegir eje
    eje = round(runif(1, 1, dim)) 
    if (runif(1) < 0.5) { # subir en ese eje
        pos[eje] = pos[eje] + 1
    } else { # bajar en ese eje
        pos[eje] = pos[eje] - 1
    }
    if (all(pos == 0)) { # si todos son ceros
        regresos = regresos + 1 # regreso al origen
    }
    manhattan = sum(abs(pos)) # suma de los valores absolutos
    mayor = max(mayor, manhattan)
}
cat('Fueron', regresos, 'regresos', '\n')
cat('La mayor distancia (Manhattan) era de', mayor, '\n')
