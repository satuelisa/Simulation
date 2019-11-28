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
unirse <- function(tam, cuantos) {
    res <- integer()
    for (cumulo in 1:cuantos) {
        if (runif(1) < union(tam)) {
            res <- c(res, -tam) # marcamos con negativo los que quieren unirse
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
for (paso in 1:duracion) {
    cumulos <- integer()
    for (i in 1:dim(freq)[1]) {
        urna <- freq[i,]
        cumulos <- c(cumulos, unirse(urna$tam, urna$num))
    }
    juntarse <- -cumulos[cumulos < 0] # sacarlos y hacerlos positivos 
    cumulos <- cumulos[cumulos > 0] # los demas se quedan tal cual
    nt <- length(juntarse)
    if (nt > 0) {
        if (nt > 1) {
            np <- floor(nt / 2) # cuantos pares se pueden formar
            juntarse <- sample(juntarse) # ponerles orden aleatorio
            for (i in 1:np) { # sacar los pares formados por el orden
                cumulos <- c(cumulos, juntarse[2*i-1] + juntarse[2*i])
            }
        }
        if (nt %% 2 == 1) { # es una cantidad impar
            cumulos <- c(cumulos, juntarse[length(juntarse)]) # el ultimo
        }
    }
    tl <- paste(paso, "", sep="")
    while (nchar(tl) < digitos) {
        tl <- paste("0", tl, sep="")
    }
    png(paste("p8_ut", tl, ".png", sep=""), width=300, height=300)
    hist(cumulos, breaks=20, main=paste("Paso", paso, "con pura uni\u{00f3}n"), 
         freq=FALSE, ylim=c(0, 0.05),
         xlab="Tama\u{00f1}o", ylab="Frecuencia relativa")
    graphics.off()
    freq <- as.data.frame(table(cumulos))
    names(freq) <- c("tam", "num")
    freq$tam <- as.numeric(levels(freq$tam))[freq$tam]
}
