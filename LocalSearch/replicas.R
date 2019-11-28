f <- function(x) { # modificamos para que sea interesante
    return(5 * cos(14*x - 3) * sin(2*x^2 - 4 * x) + 2 * x^2 - 4 * x)
}
 
low <- -2
high <- 4
step <- 0.25
replicas <- 100
 
replica <- function(t) {
    curr <- runif(1, low, high)
    best <- curr
    for (tiempo in 1:t) {
        delta <- runif(1, 0, step)
        left <- curr - delta
        right <- curr + delta
        if (f(left) < f(right)) {
            curr <- left
        } else {
            curr <- right
        }
        if (f(curr) < f(best)) {
            best <- curr
        }
    }
    return(best)
}
 
suppressMessages(library(doParallel))
registerDoParallel(makeCluster(detectCores() - 1))
x <- seq(low, high, length.out=500)
y <- foreach(i = x, .combine=c) %dopar% f(i)
 
for (pot in 2:4) {
    tmax <- 10^pot
    resultados <- foreach(i = 1:replicas, .combine=c) %dopar% replica(tmax)
    png(paste("p7_", tmax, ".png", sep=""), width=700, height=300)
    plot(x, y, type="l", main=paste(tmax, "pasos"))
    valores <- f(resultados)
    points(resultados, valores, pch=16, col="red")
    mejor <- which.min(valores)
    abline(v = resultados[mejor], col="green", lwd=3)
    graphics.off()
}
stopImplicitCluster()
