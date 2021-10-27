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

# si respeta la restriccion o no
factible <- function(seleccion, pesos, capacidad) {
    return(sum(seleccion * pesos) <= capacidad)
}

# calcular el valor total (lo que se maximiza)
objetivo <- function(seleccion, valores) {
    return(sum(seleccion * valores))
}

normalizar <- function(data) {
    menor <- min(data)
    mayor <- max(data)
    rango <- mayor - menor
    data <- data - menor # > 0
    return(data / rango) # entre 0 y 1
}

# pesos normalmente distribuidos
generador.pesos <- function(cuantos, min, max) {
    return(sort(round(normalizar(rnorm(cuantos)) * (max - min) + min)))
}

# valores que dependan del peso (ojo)
generador.valores <- function(pesos, min, max) {
    n <- length(pesos)
    valores <- double()
    for (i in 1:n) {
        media <- pesos[n]
        desv <- runif(1)
        valores <- c(valores, rnorm(1, media, desv)) # variar esta parte
    }
    valores <- normalizar(valores) * (max - min) + min
    return(valores)
}

# soluciones iniciales pseudoaleatorias
poblacion.inicial <- function(n, tam) {
    pobl <- matrix(round(runif(tam * n)), nrow = tam, ncol = n)
    return(as.data.frame(pobl))
}

# mutar la solucion sol
mutacion <- function(sol, n) {
    pos <- sample(1:n, 1) # posicion por cambiar
    mut <- sol # clon
    mut[pos] <- (!sol[pos]) * 1 # modificar el clon
    return(mut) # regresa el clon
}

# cruzamiento: dos soluciones x & y
reproduccion <- function(x, y, n) {
    pos <- sample(2:(n-1), 1) # donde cortar
    xy <- c(x[1:pos], y[(pos+1):n]) # cabeza de x con cola de y
    yx <- c(y[1:pos], x[(pos+1):n]) # cabeza de y con cola de x
    return(c(xy, yx)) # regresa los hijos en un solo vector
}

n <- 100 # cuantos objetos
pesos <- generador.pesos(n, 15, 80) # generar sus pesos
valores <- generador.valores(pesos, 10, 500) # generar valores DADO los pesos
capacidad <- round(sum(pesos) * 0.65) # capacidad 65% del peso total
optimo <- knapsack(capacidad, pesos, valores) # cuanto vale el optimo
print("optimo obtenido")
init <- 50 # cuantas soluciones
p <- poblacion.inicial(n, init) # iniciales al azar
tam <- dim(p)[1]
assert(tam == init)
pm <- 0.1 # probabilidad de mutacion
rep <- 10 # cantidad de cruzamientos
tmax <- 30 # iteraciones
for (iter in 1:tmax) { # iterar
    p$obj <- NULL
    p$fact <- NULL
    for (i in 1:tam) { # cada objeto puede mutarse con probabilidad pm
        if (runif(1) < pm) { # si es que hace
            p <- rbind(p, mutacion(p[i,], n)) # agregar clon en la poblacion
        }
    }
    for (i in 1:rep) { # una cantidad fija de reproducciones
        padres <- sample(1:tam, 2, replace=FALSE) # distintos
        hijos <- reproduccion(p[padres[1],], p[padres[2],], n)
        # agregar al final del dataframe
        p <- rbind(p, hijos[1:n]) # primer hijo (mitad)
        p <- rbind(p, hijos[(n+1):(2*n)]) # segundo hijo (mitad)
    }
    tam <- dim(p)[1] # cuantos son ahora
    obj <- double()
    fact <- integer()
     for (i in 1:tam) {
        obj <- c(obj, objetivo(p[i,], valores))
        fact <- c(fact, factible(p[i,], pesos, capacidad))
    }
    p <- cbind(p, obj) # columna de objetivo (n + 1)
    p <- cbind(p, fact) # columna de factibilidad (n + 2)
    # matanza
    mantener <- order(-p[, (n + 2)], -p[, (n + 1)])[1:init]
    p <- p[mantener,] # recortar a los primeros init
    tam <- dim(p)[1]
    assert(tam == init)
    factibles <- p[p$fact == TRUE,] # filtrar factibles
    mejor <- max(factibles$obj) # mayor objetivo entre factibles
    print(paste(mejor, (optimo - mejor) / optimo))
}
