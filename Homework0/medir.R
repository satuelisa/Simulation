for (n in 9:14) {
    k = 2^n
    cat(k, system.time(matrix(runif(k*k), nrow=k))[3], '\n')
}
