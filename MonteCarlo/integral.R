desde <- 3
hasta <- 7
pedazo <- 50000
cuantos <- 500
f <- function(x) { return(1 / (exp(x) + exp(-x))) }
g <- function(x) { return((2 / pi) * f(x)) }
suppressMessages(library(distr))
generador  <- r(AbscontDistribution(d = g)) # creamos un generador            
parte <- function() {
    valores <- generador(pedazo)
    return(sum(valores >= desde & valores <= hasta))
}
suppressMessages(library(doParallel))
registerDoParallel(makeCluster(detectCores() - 1))
montecarlo <- foreach(i = 1:cuantos, .combine=c) %dopar% parte()
stopImplicitCluster()
integral <- sum(montecarlo) / (cuantos * pedazo)
print((pi / 2) * integral)
