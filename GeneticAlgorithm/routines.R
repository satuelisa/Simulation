library(testit)
 
knapsack <- function(cap, peso, valor) {
    n <- length(peso)
    pt <- sum(peso) # deben ser enteros en este caso
    assert(n == length(valor))
    vt <- sum(valor) # pueden ser lo que sea
    if (pt < cap) { # cabe todo
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
 
al.azar <- function(cuantos) {
    return(round(runif(cuantos)))
}
 
normalizar <- function(data) {
    menor <- min(data)
    mayor <- max(data)
    rango <- mayor - menor
    data <- data - menor # > 0
    return(data / rango) # entre 0 y 1
}
 
generador.pesos <- function(cuantos, min, max) {
    return(sort(round(normalizar(rnorm(cuantos)) * (max - min) + min)))
}
 
generador.valores <- function(pesos, min, max) {
    n <- length(pesos)
    valores <- double()
    for (i in 1:n) {
        media <- pesos[i]
        desv <- runif(1)
        valores <- c(valores, rnorm(1, media, desv))
    }
    valores <- normalizar(valores) * (max - min) + min
    return(valores)
}
 
n <- 20
pesos <- generador.pesos(n, 15, 80)
valores <- generador.valores(pesos, 10, 500)
capacidad <- round(sum(pesos) * 0.65)
print(pesos)
print(valores)
print(knapsack(capacidad, pesos, valores))
for (i in 1:10) {
    intento <- al.azar(n)
    print(paste(factible(intento, pesos, capacidad), objetivo(intento, valores)))
}
