desde <- 3
hasta <- 7
n <- 50
f <- function(x) { return(1 / (exp(x) + exp(-x))) }
g <- function(x) { return((2 / pi) * f(x)) }
suppressMessages(library(distr))
generador  <- r(AbscontDistribution(d = g)) # creamos un generador
valores <- generador(n)
mc = sum(valores >= desde & valores <= hasta)
integral <- sum(mc) / n
print((pi / 2) * integral)
