euclideana <- function(p1, p2) {
    return(sqrt(sum((p1 - p2)**2)))
}
 
manhattan <- function(p1, p2) {
    return(sum(abs(p1 - p2)))
}
 
ed.orig <- function(p) {
    dimension <- length(p)
    origen <- rep(0, dimension)
    return(euclideana(p, origen))
}
 
md.orig <- function(p) {
    dimension <- length(p)
    origen <- rep(0, dimension)
    return(manhattan(p, origen))
}
