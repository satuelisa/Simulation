doble <- function(x) {
    return(2*x);
}

a <- 13
b <- 23
if (doble(a) > b) {
    cat('hola\n');
}

for (x in 0:9) {
    cat(2**x, '\n');
}
