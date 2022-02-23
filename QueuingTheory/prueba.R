primo <- function(n) {
    if (n < 4) {
        return(TRUE)
    }
    if (n %% 2 == 0) {
        return(FALSE)
    }
    for (i in seq(3, max(3, ceiling(sqrt(n))), 2)) {
        if (n %% i == 0) {
            return(FALSE)
        }
    }
    return(TRUE)
}
 
d <- 100 # desde
h <-  200 # hasta
replicas <- 5
suppressMessages(library(doParallel))
registerDoParallel(makeCluster(detectCores() - 1))
tiempos <-  numeric()
for (r in 1:replicas) {
    # tomamos el "elapsed" de la salida de system.time, es el tercer dato
    t <- system.time(foreach(n = d:h, .combine=c) %dopar% primo(n))[3]
    tiempos <- c(tiempos, t)
}
stopImplicitCluster()
summary(tiempos)
