pick.one <- function(x) {
    if (length(x) == 1) {
        return(x)
    } else {
        return(sample(x, 1))
    }
}
 
poli <- function(maxdeg, varcount, termcount) {
    f <- data.frame(variable=integer(), coef=integer(), degree=integer())
    for (t in 1:termcount) {
        var <- pick.one(1:varcount)
        deg <- pick.one(1:maxdeg)
        f <-  rbind(f, c(var, runif(1), deg))
    }
    names(f) <- c("variable", "coef", "degree")
    return(f)
}
 
eval <- function(pol, vars, terms) {
    value <- 0.0
    for (t in 1:terms) {
        term <- pol[t,]
        value <-  value + term$coef * vars[term$variable]^term$degree
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
n <- 100 # cuantas soluciones aleatorias
sol <- matrix(runif(vc * n), nrow=n, ncol=vc)
val <- matrix(rep(NA, k * n), nrow=n, ncol=k)
for (i in 1:n) { # evaluamos las soluciones
    for (j in 1:k) { # para todos los objetivos
        val[i, j] <- eval(obj[[j]], sol[i,], tc)
    }
}
png("p11_init.png")
plot(val[,1], val[,2], xlab="Primer objetivo", ylab="Segundo objetivo",
     main="Ejemplo bidimensional")
graphics.off()           
