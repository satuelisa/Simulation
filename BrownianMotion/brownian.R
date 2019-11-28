repetir <- 100
duracion <- 200
eucl <-  FALSE
library(parallel)
 
cluster <- makeCluster(detectCores() - 1)
clusterExport(cluster, "duracion")
clusterExport(cluster, "eucl")
datos <-  data.frame()
 
for (dimension in 1:8) {
    clusterExport(cluster, "dimension")
    resultado <- parSapply(cluster, 1:repetir,
                           function(r) {
                           pos <- rep(0, dimension)
                           mayor <- 0
                           for (t in 1:duracion) {
                               cambiar <- sample(1:dimension, 1)
                               cambio <- 1
                               if (runif(1) < 0.5) {
                                   cambio <- -1
                               }
                               pos[cambiar] <- pos[cambiar] + cambio
                               if (eucl) {
                                   d <- sqrt(sum(pos**2))
                               } else { # Manhattan
                                   d <- sum(abs(pos))
                               }
                               if (d > mayor) {
                                   mayor <- d
                               }
                           }
                           return(mayor)
                           })
    datos <- rbind(datos, resultado)
}
stopCluster(cluster)
if (eucl) {
    png("p1er.png")
    boxplot(data.matrix(datos), use.cols=FALSE, 
       xlab="Dimensi\u{F3}n", ylab="Distancia m\u{E1}xima", 
       main="Euclideana")
} else {
    png("p1mr.png")
    boxplot(data.matrix(datos), use.cols=FALSE, 
       xlab="Dimensi\u{F3}n", ylab="Distancia m\u{E1}xima", 
       main="Manhattan")
}
graphics.off()
