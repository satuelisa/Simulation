library(testit)

knapsack <- function(cap, peso, valor) {
    n <- length(peso)
    pt <- sum(peso)
    assert(n == length(valor))
    vt <- sum(valor)
    if (pt < cap) {
        return(vt)
    } else {
        filas <- cap + 1
        cols <- n + 1
        tabla <- matrix(rep(-Inf, filas * cols),
                       nrow = filas, ncol = cols)
        for (fila in 1:filas) {
            tabla[fila, 1] <- 0
        }
        rownames(tabla) <- 0:cap
        colnames(tabla) <- c(0, valor)
        for (objeto in 1:n) {
            for (acum in 1:(cap+1)) {
                anterior <- acum - peso[objeto]
                tabla[acum, objeto + 1] <- tabla[acum, objeto]
                if (anterior > 0) {
                    tabla[acum, objeto + 1] <- max(tabla[acum, objeto], tabla[anterior, objeto] + valor[objeto])
                }
            }
        }
        return(max(tabla))
    }
}

factible <- function(seleccion, pesos, capacidad) {
    return(sum(seleccion * pesos) <= capacidad)
}

objetivo <- function(seleccion, valores) {
    return(sum(seleccion * valores))
}

n = 15
low = 1
high = 150
# ordenados de menor a mayor
peso <- sort(round(runif(n, low, high)))
low = 120
high = 100000
valor <- round(runif(n, low, high))
total = sum(peso)
capacidad = round(0.6 * total)
optimo = knapsack(capacidad, peso, valor)
tam = 50 # cuantas soluciones
# generar selecciones al azar
pobl <- matrix(round(runif(tam * n)), nrow = tam, ncol = n)
for (fila in 1:tam) {
    s = pobl[fila,]
    if (factible(s, peso, capacidad)) {
        obtenido = objetivo(s, valor)
        cat(obtenido, optimo - obtenido, "\n")
    }
}


