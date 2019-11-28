k <- 10000
n <- 1000000
originales <- rnorm(k)
cumulos <- originales - min(originales) + 1
cumulos <- round(n * cumulos / sum(cumulos))
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
c <- median(cumulos) # tamanio critico de cumulos
d <- sd(cumulos) / 4 # factor arbitrario para suavizar la curva
rotura <- function(x) {
    return (1 / (1 + exp((c - x) / d)))
}
union <- function(x) {
    return (exp(-x / c))
}
romperse <- function(tam, cuantos) {
    res <- integer()
    for (cumulo in 1:cuantos) {
        if (runif(1) < rotura(tam)) {
            primera <- sample(1:(tam-1), 1)
            segunda <- tam - primera
            res <- c(res, primera, segunda)
        } else {
            res <- c(res, tam)
        }
    }
    return(res)
}
freq <- as.data.frame(table(cumulos))
names(freq) <- c("tam", "num")
freq$tam <- as.numeric(levels(freq$tam))[freq$tam]
duracion <- 10
digitos <- floor(log(duracion, 10)) + 1
xmax <- NULL
for (paso in 1:duracion) {
    pedazos <- integer()
    for (i in 1:dim(freq)[1]) {
        urna <- freq[i,]
        pedazos <- c(pedazos, romperse(urna$tam, urna$num))
    }
    tl <- paste(paso, "", sep<-"")
    while (nchar(tl) < digitos) {
        tl <- paste("0", tl, sep="")
    }
    if (is.null(xmax)) {
        xmax <- 1.05 * max(pedazos)
    }
    png(paste("p8_t", tl, ".png", sep=""), width=300, height=300)
    hist(pedazos, breaks=10, main=paste("Paso", paso, "con pura rotura"), 
         freq=FALSE, xlim=c(0, xmax), ylim=c(0, 0.05),
         xlab="Tama\u{00f1}no", ylab="Frecuencia relativa")
    graphics.off()
    freq <- as.data.frame(table(pedazos))
    names(freq) <- c("tam", "num")
    freq$tam <- as.numeric(levels(freq$tam))[freq$tam]
}
