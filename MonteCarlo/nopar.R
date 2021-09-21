desde <- 3
hasta <- 7
cuantos <- 1000 # puntitos en el cuadro
f <- function(x) { return(1 / (exp(x) + exp(-x))) } # funcion que piden
g <- function(x) { return((2 / pi) * f(x)) } # normalizado a distr
suppressMessages(library(distr)) # paquete
generador  <- r(AbscontDistribution(d = g)) # creamos un generador
valores <- generador(cuantos) # generamos valores
montecarlo = sum(valores >= desde & valores <= hasta) # checamos
integral <- sum(montecarlo) / cuantos # tasa: integral para g(x)
print((pi / 2) * integral) # integral para f(x) (renorm)
