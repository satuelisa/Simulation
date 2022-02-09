dim = 5 # cuantas dimensiones
dur = 1000
replicas = 50
cat(replicas, 'caminatas de', dur, 'pasos en', dim, 'dimensiones', '\n')
dist = numeric() # lista sin nada
reg = numeric() # lista sin nada
for (r in 1:replicas) {
    pos = rep(0, 5)
    mayor = 0
    regresos = 0
    for (paso in 1:dur) {    
        eje = round(runif(1, 1, dim)) 
        if (runif(1) < 0.5) { # subir en ese eje
            pos[eje] = pos[eje] + 1
        } else { # bajar en ese eje
            pos[eje] = pos[eje] - 1
        }
        if (all(pos == 0)) { # si todos son ceros
            regresos = regresos + 1 # regreso al origen
        }
        mayor = max(mayor, sum(abs(pos))) # manhattan
    }
    dist = c(dist, mayor) # agregar la nueva mayor distancia
    reg = c(reg, regresos) # agregar el nuevo contador de regresos
}
print('Regresos')
summary(reg)
print('Mayores distancias (Manhattan)')
summary(dist)
