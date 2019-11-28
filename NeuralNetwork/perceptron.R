tasa <- 0.15 # tasa de aprendizaje
tranqui <- 0.95 # se va bajando con ajustes hechos
dim <- 2
w <- runif(dim) # pesos del perceptron, al azar inicialmente
 
dibuja <- TRUE
 
if (dibuja) {
    xT <- double()
    yT <- double()
    xF <- double()
    yF <- double()
    xi <- -1
    xf <- 2
}
 
# contadores
tP <- 0 # true positive (ambos son 1)
fP <- 0 # da falso aunque era verdad
tN <- 0 # true negative (ambos son 0)
fN <- 0 # da verdad aunque era falso
 
tmax <- 150 # pasos en total
entrenamiento <- ceiling(0.7 * tmax)
prueba <- tmax - entrenamiento # probamos despues de entrenar
if (dibuja) {
    dl <- floor(log(tmax, 10)) + 1
    system("rm -f p12_t*.png")
}
for (t in 1:tmax) {
    x <- runif(1)
    y <- runif(1)
    deseada <- x > y
    entrada <- c(x, y)
    resultado <- sum(w * entrada) >= 0
    if (t <= entrenamiento) { # aprende durante entrenamiento
        if (deseada != resultado) { # pero hubo un error en la salida
            ajuste <- tasa * (deseada - resultado)
            tasa <- tranqui * tasa # ajustamos menos cada vez
            w <- w + ajuste * entrada
            bien <- FALSE
        } else {
            bien <- TRUE
        }
        if (dibuja) {
            fase <- "Fase de entrenamiento,"
            if (deseada) {
                xT <- c(xT, x)
                yT <- c(yT, y)
            } else {
                xF <- c(xF, x)
                yF <- c(yF, y)
            }
        }
    } else { # responde en la fase prueba
        if (deseada == resultado) {
            bien <- TRUE
            if (deseada) {
                tP <- tP + 1
            } else {
                tN <- tN + 1
            }
        } else {
            bien <- FALSE
            if (deseada) {
                fN <- fN + 1
            } else {
                fP <- fP + 1
            }
        }
        if (dibuja) {
            fase <- "Fase de prueba,"
        }
    }
    if (dibuja) {
        tl <- paste(t, "", sep="")
        while (nchar(tl) < dl) {
            tl <- paste("0", tl, sep="")
        }
        png(paste("p12_t", tl, ".png", sep=""))
        pendiente <- -w[1] / w[2]
        plot(c(xi, xf), c(pendiente * xi, pendiente * xf),
             type="l", lwd=3, col="blue",
             xlim=c(0, 1), ylim=c(0, 1), xlab='x', ylab='y',
             main=paste(fase, "paso", t)) # perceptron
        points(xT, yT, pch=15, col="gray")
        points(xF, yF, pch=16, col="gray")
        if (bien) {
            points(x, y, pch=17, col="green", cex=2)
        } else { # la deseada no fue correcta
            points(x, y, pch=18, col="red", cex=2)
        }
        graphics.off()
    }
}
if (dibuja) {
    system("convert -delay 50 -size 300x300 p12_t*.png -loop 0 p12.gif")
}
print("Bien")
print(paste(tP, tN))
print("Mal")
print(paste(fP, fN))
