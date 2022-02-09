repetir <- 100 # replicas
duracion <- 200 # pasos
datos <-  data.frame() # almacenar resultados 
for (dimension in 1:8) { # variar dimension
    resultado = numeric() # juntar los datos de las replicas
    for (replica in 1:repetir) { # realizar replicas
        pos <- rep(0, dimension) # iniciar en origen
        mayor <- 0 # mayor distancia inicia en cero
        for (t in 1:duracion) { # realizar los pasos
            cambiar <- sample(1:dimension, 1) # elegir eje
            cambio <- 1 
            if (runif(1) < 0.5) {
                cambio <- -1
            }
            pos[cambiar] <- pos[cambiar] + cambio # mover
            mayor <- max(mayor, sqrt(sum(pos**2))) # dist eucl
        }
        resultado = c(resultado, mayor) # almacenar el mayor valor
    }
    datos <- rbind(datos, resultado) # almacenar los resultados de esta dimension
}
png("figuraR.png") # mandar la figura a un archivo
# las filas van a ser los "grupos" de la figura
boxplot(data.matrix(datos), use.cols = FALSE, 
        xlab="Dimensi\u{F3}n", ylab="Distancia m\u{E1}xima", 
        main="Distancia Euclideana")
graphics.off()
