k <- 1000
n <- 100000
cumulos <- rnorm(k)
cumulos <- cumulos - min(cumulos) # ahora el menor vale cero
cumulos <- cumulos + 1 # ahora el menor vale uno
cumulos <- cumulos / sum(cumulos) # ahora suman a uno
cumulos <- n * cumulos # ahora suman a n, pero son valores decimales
cumulos <- round(cumulos) # ahora son enteros
diferencia <- n - sum(cumulos) # por cuanto le hemos fallado
if (diferencia > 0) { # faltan particulas
    for (i in 1:diferencia) {
        p <- sample(1:k, 1) # elegimos uno al azar
        cumulos[p] <- cumulos[p] + 1 # agregamos particula
    }
} else if (diferencia < 0) { # sobran particulas
    while (diferencia < 0) {
        p <- sample(1:k, 1) # elegimos uno al azar
        if (cumulos[p] > 1) { # sin vaciar
            cumulos[p] <- cumulos[p] - 1 # restamos particula
            diferencia <- diferencia + 1 
    }
    }
}
png("p8_init.png")
plot(hist(cumulos), main="Estado inicial",
     xlab="Tama\u{00f1}o de c\u{00fa}mulos", ylab="Frecuencia absoluta")
graphics.off()
