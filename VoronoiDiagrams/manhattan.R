suppressMessages(library(doParallel))

experimento = function(k) {
    n <-  40
    zona <- matrix(rep(0, n * n), nrow = n, ncol = n)
    x <- rep(0, k) # ocupamos almacenar las coordenadas x de las semillas
    y <- rep(0, k) # igual como las coordenadas y de las semillas
    for (semilla in 1:k) {
        while (TRUE) { # hasta que hallamos una posicion vacia para la semilla
            fila <- sample(1:n, 1)
            columna <- sample(1:n, 1)
            if (zona[fila, columna] == 0) {
                zona[fila, columna] = semilla
                x[semilla] <- columna
                y[semilla] <- fila
                break
            }
        }
    }
    celda <-  function(pos) {
        fila <- floor((pos - 1) / n) + 1
        columna <- ((pos - 1) %% n) + 1
        if (zona[fila, columna] > 0) { # es una semilla
            return(zona[fila, columna])
        } else {
            cercano <- NULL # sin valor por el momento
            menor <- n * sqrt(2) # mayor posible para comenzar la busqueda
            for (semilla in 1:k) {
                dx <- columna - x[semilla]
                dy <- fila - y[semilla]
                dist <- sqrt(dx^2 + dy^2)
                if (dist < menor) {
                    cercano <- semilla
                    menor <- dist
                }
            }
            return(cercano)
        }
    }
    celdas <- sapply(1:(n * n), celda)
    voronoi <- matrix(celdas, nrow = n, ncol = n, byrow=TRUE)
    inicio <- function() {
        direccion <- sample(1:4, 1)
        xg <- NULL
        yg <- NULL
        if (direccion == 1) { # horiz izq -> der
            xg <- 1
            yg <- sample(1:n, 1)
        } else if (direccion == 2) { # vertical abajo -> arriba
            xg <- sample(1:n, 1)
            yg <- 1
        } else if (direccion == 3) { # horiz der -> izq
            xg <- n
            yg <- sample(1:n, 1)
        } else { # vertical arriba -> abajo
            xg <- sample(1:n, 1)
            yg <- n
        }
        return(c(xg, yg))
    }
    vp <- data.frame(numeric(), numeric()) # posiciones de posibles vecinos
    for (dx in -1:1) {
        for (dy in -1:1) {
            if (dx != 0 | dy != 0) { # descartar la posicion misma
                vp <- rbind(vp, c(dx, dy))
            }
        }
    }
    names(vp) <- c("dx", "dy")
    vc <- dim(vp)[1]
    distancia <- function(replica) {
        prob <- 1 # interno a la celda (inicial)
        dificil <- 0.99 # bajada al interior
        grieta <- voronoi # marcamos la grieta en una copia
        i <- inicio() # posicion inicial al azar
        xg <- i[1]
        yg <- i[2]
        mayor = 0
        while (TRUE) { # hasta que la propagacion termine
            grieta[yg, xg] <- 0 # usamos el cero para marcar la grieta
            actual = min(n - yg, n - xg, xg - 1, yg - 1) # las cuatro distancias de los lados
                                        #                    %%%%%%  ++++++  ======  @@@@@@
                                        #        ----------
                                        #        |   %    |
                                        #        |===*++++|   xg (h), yg (v)
                                        #        |   @    |
                                        #        |   @    |    n por n
                                        #        ----------
            mayor = max(mayor, actual) # recordar el mayor de los minimos
            frontera <- numeric()
            interior <- numeric()
            for (v in 1:vc) {
                vecino <- vp[v,]
                xs <- xg + vecino$dx # columna del vecino potencial
                ys <- yg + vecino$dy # fila del vecino potencial
                if (xs > 0 & xs <= n & ys > 0 & ys <= n) { # no sale de la zona
                    if (grieta[ys, xs] > 0) { # aun no hay grieta ahi
                        if (voronoi[yg, xg] == voronoi[ys, xs]) {
                            interior <- c(interior, v)
                        } else { # frontera
                            frontera <- c(frontera, v)
                        }
                    }
                }
            }
            elegido <- 0
            if (length(frontera) > 0) { # siempre tomamos frontera cuando haya
                if (length(frontera) > 1) {
                    elegido <- sample(frontera, 1)
                } else {
                    elegido <- frontera # sample sirve con un solo elemento
                }
                prob <- 1 # estamos nuevamente en la frontera
            } else if (length(interior) > 0) { # no hubo frontera para propagar
                if (runif(1) < prob) { # intentamos en el interior
                    if (length(interior) > 1) {
                        elegido <- sample(interior, 1)
                    } else {
                        elegido <- interior
                    }
                    prob <- dificil * prob # mas dificil a la siguiente
                }
            }
            if (elegido > 0) { # si se va a propagar
                vecino <- vp[elegido,]
                xg <- xg + vecino$dx
                yg <- yg + vecino$dy
            } else {
                break # ya no se propaga
            }
        }
        return(mayor)
    }
    manhattan <- sapply(1:30, distancia)
    return(manhattan)
}

d1 = experimento(20)
d2 = experimento(30)
d3 = experimento(40)
png('manhattan.png')
boxplot(d1, d2, d2, names = c("k = 20", "k = 30", "k = 40"))
dev.off()
