k <- 1000
n <- 100000
eps <- 0.0000001
originales <- rnorm(k)
cumulos <- originales - min(originales)  + eps
cumulos <- round(n * cumulos / sum(cumulos))
cumulos <- round(cumulos)
diferencia <- n - sum(cumulos)
if (diferencia > 0) {
    for (i in 1:diferencia) {
        p <- sample(1:k, 1)
        cumulos[p] <- cumulos[p] + 1
    }
} else if (diferencia < 0) {
    for (i in 1:-diferencia) {
        p <- sample(1:k, 1)
        if (cumulos[p] > 1) {
            cumulos[p] <- cumulos[p] - 1
        }
    }
}
png("p8_norm.png")
par(mfrow = c(2, 2)) # juntamos graficas
plot(density(originales)) # lo generado que era normal
print(shapiro.test(originales))
qqnorm(originales)
qqline(originales, col = 2)
plot(density(cumulos)) # lo nuestro que hemos modificado
print(shapiro.test(cumulos))
qqnorm(cumulos)
qqline(cumulos, col = 2)
graphics.off()
