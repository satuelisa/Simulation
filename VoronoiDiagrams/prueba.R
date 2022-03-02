n <-  5
zona <- matrix(rep(0, n * n), nrow = n, ncol = n)
k <- 3
for (semilla in 1:k) {
    while (TRUE) { # hasta que hallamos una posicion vacia para la semilla
        fila <- sample(1:n, 1)
        columna <- sample(1:n, 1)
        if (zona[fila, columna] == 0) {
            zona[fila, columna] = semilla
            break
        }
    }
}
print(zona)
png("sinrotar.png")
par(mar = c(0,0,0,0)) # sin margen
# para opciones de colores, ver https://www.r-bloggers.com/color-palettes-in-r/
image(zona, col=rainbow(k+1), xaxt='n', yaxt='n')
graphics.off()

png("conrotar.png")
par(mar = c(0,0,0,0)) # sin margen
rotate <- function(x) t(apply(x, 2, rev))
image(rotate(zona), col=rainbow(k+1), xaxt='n', yaxt='n')
graphics.off()
