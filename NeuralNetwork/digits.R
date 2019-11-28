modelos <- read.csv("digits.txt", sep=" ", header=FALSE, stringsAsFactors=F)
modelos[modelos=='n'] <- 0.995 # pixeles negros en plantillas
modelos[modelos=='g'] <- 0.92 # pixeles grises en plantillas
modelos[modelos=='b'] <- 0.002 # pixeles blancos en plantillas
 
r <- 5
c <- 3
dim <- r * c
 
n <- 49
w <- ceiling(sqrt(n))
h <- ceiling(n / w)
 
png("p12g.png", width=1600, height=2000)
par(mfrow=c(w, h), mar = c(0,0,7,0))
suppressMessages(library("sna"))
 
for (j in 1:n) {
    d <- sample(0:9, 1)
    pixeles <- runif(dim) < modelos[d + 1,] # fila 1 contiene el cero, etc.
    imagen <- matrix(pixeles, nrow=r, ncol=c, byrow=TRUE)
    plot.sociomatrix(imagen, drawlab=FALSE, diaglab=FALSE, 
                     main=paste(d, ""), cex.main=5)
}
graphics.off()
