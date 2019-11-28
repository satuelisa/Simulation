f <- function(x) {
    return(cos(14.5*x - 0.3) + x * (x + 0.2) + 1.01)
}
low <- -3
high <- -low
x <- seq(low, high, 0.05)
y <- f(x)
tmax <- 100
digitos <- floor(log(tmax, 10)) + 1
curr <- runif(1, low, high)
best <- curr
step <- 0.3
for (tiempo in 1:tmax) {
    delta <- runif(1, 0, step)
    left <- curr - delta
    right <- curr + delta
    fl <- f(left)
    fr <- f(right)
    if (fl < fr) {
        curr <- left
    } else {
        curr <- right
    }
    if (f(curr) < f(best)) { # minimizamos
        best <- curr
    }
    tl <- paste(tiempo, "", sep="")
    while (nchar(tl) < digitos) {
        tl <- paste("0", tl, sep="")
    }
    salida <- paste("p7_t", tl, ".png", sep="")
    tiempo <- paste("Paso", tiempo)
    png(salida, width=500, height=400)
    plot(x, y, type="l")
    abline(v = best, col="green", lwd=2)
    points(curr, f(curr), pch=16, col="red")
    graphics.off()
}
