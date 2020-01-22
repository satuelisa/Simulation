caminata <- function(dim, dur, dist) {
    pos <- rep(0, dim)
    mayor <- 0
    for (t in 1:dur) {
        cambiar <- sample(1:dim, 1)
        cambio <- 1
        if (runif(1) < 0.5) {
            cambio <- -1
        }
        pos[cambiar] <- pos[cambiar] + cambio
        d <- dist(pos)
        if (d > mayor) {
            mayor <- d
        }
    }
    return(mayor)
}
