l <- 1
n <- 50
pi <- 0.05
v <- l / 20
agentes <- data.frame(x = double(), y = double(),
                      dx = double(), dy = double(),
                      estado  = character())
for (i in 1:n) {
    e <- "S"
    if (runif(1) < pi) {
        e <- "I"
    }
    agentes <- rbind(agentes, data.frame(x = runif(1, 0, l),
                                         y = runif(1, 0, l),
                                         dx = runif(1, -v, v),
                                         dy = runif(1, -v, v),
                                         estado = e))
}
levels(agentes$estado) <- c(levels(agentes$estado), "R")
 
epidemia <- integer()
r <- 0.1
tmax <- 30
digitos <- floor(log(tmax, 10)) + 1
for (tiempo in 1:tmax) {
    infectados <- dim(agentes[agentes$estado == "I",])[1]
    epidemia <- c(epidemia, infectados)
    if (infectados == 0) {
        break
    }
    contagios <- rep(FALSE, n)
    for (i in 1:n) { # posibles contagios
        a1 <- agentes[i, ]
        if (a1$estado == "I") { # desde los infectados
            for (j in 1:n) {
                if (!contagios[j]) { # aun sin contagio
                    a2 <- agentes[j, ]
                    if (a2$estado == "S") { # hacia los susceptibles
                        dx <- a1$x - a2$x
                        dy <- a1$y - a2$y
                        d <- sqrt(dx^2 + dy^2)
                        if (d < r) { # umbral
                            p <- (r - d) / r
                            if (runif(1) < p) {
                                contagios[j] <- TRUE
                            }
                        }
                    }
                }
            }
        }
    }
    for (i in 1:n) { # movimientos
        a <- agentes[i, ]
        if (contagios[i]) {
            a$estado <- "I"
        }
        a$x <- a$x + a$dx
        a$y <- a$y + a$dy
        if (a$x > l) {
            a$x <- a$x - l
        }
        if (a$y > l) {
            a$y <- a$y - l
        }
        if (a$x < 0) {
            a$x <- a$x + l
        }
        if (a$y < 0) {
            a$y <- a$y + l
        }
        agentes[i, ] <- a
    }
    aS <- agentes[agentes$estado == "S",]
    aI <- agentes[agentes$estado == "I",]
    aR <- agentes[agentes$estado == "R",]
    tl <- paste(tiempo, "", sep="")
    while (nchar(tl) < digitos) {
        tl <- paste("0", tl, sep="")
    }
    salida <- paste("p6_t", tl, ".png", sep="")
    tiempo <- paste("Paso", tiempo)
    png(salida)
    plot(l, type="n", main=tiempo, xlim=c(0, l), ylim=c(0, l), xlab="x", ylab="y")
    if (dim(aS)[1] > 0) {
        points(aS$x, aS$y, pch=15, col="chartreuse3", bg="chartreuse3")
    }
    if (dim(aI)[1] > 0) {
        points(aI$x, aI$y, pch=16, col="firebrick2", bg="firebrick2")
    }
    if (dim(aR)[1] > 0) {
        points(aR$x, aR$y, pch=17, col="goldenrod", bg="goldenrod")
    }
    graphics.off()
}
cat(epidemia, "\n")
