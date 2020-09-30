p1 = 67869499
p2 = 67869533
factor = function(n) {
    if (n < 4) {
        return(-1)
    } else {
        if (n %% 2 == 0) { # par
            return(2)
        }
        for (div in seq(3, ceiling(sqrt(n)), 2)) {
            if (n %% div == 0) {
                return(div)
            }
        }
        return(-1)
    }
}
for (cand in p1:p2) {
    cat(c(cand, factor(cand)), '\n')
}
