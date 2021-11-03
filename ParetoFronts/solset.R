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
        nuevo = term$coef * vars[term$variable]^term$degree
        value <-  value + nuevo
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
n <- 500 # cuantas soluciones aleatorias
# n asignaciones aleatorias en renglones
sol <- matrix(runif(vc * n), nrow=n, ncol=vc)
# aqui entran las evaluaciones de las asignaciones
val <- matrix(rep(NA, k * n), nrow=n, ncol=k)
for (i in 1:n) { # evaluamos las soluciones
    for (j in 1:k) { # para todos los objetivos
        val[i, j] <- eval(obj[[j]], sol[i,])
    }
}

png("p11_init.png")
plot(val[,1], val[,2],
     xlab="Primer objetivo", ylab="Segundo objetivo",
     main="Ejemplo bidimensional")
graphics.off()
