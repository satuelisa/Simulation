datos <-  data.frame()
largos <- c(100, 1000, 10000)

for (dimension in 2:5) {
    for (duracion in largos) {
    	for (replica in 1:5) {
            pos <- rep(0, dimension)
            mayor <- 0
            for (t in 1:duracion) {
                cambiar <- sample(1:dimension, 1)
                cambio <- 1
                if (runif(1) < 0.5) {
                    cambio <- -1
                }
                pos[cambiar] <- pos[cambiar] + cambio
                d <- sum(abs(pos))
                if (d > mayor) {
                    mayor <- d
                }
            }
            resultado <- c(dimension, duracion, replica, mayor)
            datos <- rbind(datos, resultado)
        }
    }
}
names(datos) <- c("Dim", "Dur", "Rep", "Dist")
print("INICIO")
head(datos)
print("FINAL")
tail(datos)
