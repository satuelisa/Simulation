poli <- function(maxdeg, varcount, termcount) {
    f <- data.frame(variable=integer(),
                    coef=integer(),
                    degree=integer())
    for (t in 1:termcount) {
        var <- sample(1:varcount, 1)
        deg <- sample(0:maxdeg, 1)
        f <-  rbind(f, c(var, runif(1), deg))
    }
    names(f) <- c("variable", "coef", "degree")
    return(f)
}

eval <- function(pol, vars) {
    value <- 0.0
    terms = dim(pol)[1]
    for (t in 1:terms) {
        term <- pol[t,]
        aport = term$coef * vars[term$variable]^term$degree
        value <-  value + aport
    }
    return(value)
}

vc <- 4
md <- 3
tc <- 5
k <- 2 # cuantas funciones objetivo
obj <- list()
for (i in 1:k) {
    obj[[i]] <- poli(md, vc, tc)
}
minim <- (runif(k) > 0.5) # <- NUEVA
n <- 250 # cuantas soluciones aleatorias
sol <- matrix(runif(vc * n), nrow=n, ncol=vc)
val <- matrix(rep(NA, k * n), nrow=n, ncol=k)
for (i in 1:n) { # evaluamos las soluciones
    for (j in 1:k) { # para todos los objetivos
        val[i, j] <- eval(obj[[j]], sol[i,])
    }
}
# minimizar f = maximizar -f
mejor1 <- which.max((1 + (-2 * minim[1])) * val[,1])
mejor2 <- which.max((1 + (-2 * minim[2])) * val[,2])
cual <- c("max", "min") # FALSE (0) -> 1, TRUE (1) -> 2
xl <- paste("Primer objetivo (", cual[minim[1] + 1], ")", sep="")
yl <- paste("Segundo objetivo (", cual[minim[2] + 1], ")", sep="")
png("p11_init.png")
plot(val[,1], val[,2], xlab=xl, ylab=yl, main="Ejemplo bidimensional")
graphics.off()
png("p11_mejores.png")
plot(val[,1], val[,2], xlab=paste(xl, "mejor con cuadro azul"),
     ylab=paste(yl,"mejor con bolita naranja"),
     main="Ejemplo bidimensional")
# mejor con cuadro azul para el primer objetivo
points(val[mejor1, 1], val[mejor1, 2], col="blue", pch=15, cex=1.5)
# mejor con bola naranja para el segundo objetivo
points(val[mejor2, 1], val[mejor2, 2], col="orange", pch=16, cex=1.5)
graphics.off()
