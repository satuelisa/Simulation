temporiza =  function(matrix, repeticiones) {
    for (i in 1:repeticiones) {
        Q = matrix %*% matrix
    }
}

n = 2^11
M = matrix(runif(n * n), ncol = n, nrow = n)
print(n)
library(pryr)
B = object_size(M)
kB = B / 2^10
MB = kB / 2^10
GB = MB / 2^10
cat(B, kB, MB, GB, "\n")
rep = 3
tiempo = system.time(temporiza(M, rep))[3]
print(tiempo / rep)
