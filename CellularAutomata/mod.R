dim <- 10
num <-  dim^2

paso <- function(pos) {
    fila <- floor((pos - 1) / dim) + 1
    columna <- ((pos - 1) %% dim) + 1
    vecindad <-  actual[max(fila - 1, 1) : min(fila + 1, dim),
                        max(columna - 1, 1): min(columna + 1, dim)]
    return(1 * ((sum(vecindad) - actual[fila, columna]) == 3))
}

datos = data.frame()
for (p in seq(0.1, 0.9, 0.1)) {
    for (replica in 1:5) {
        mayor = 0
        ant = 0
        vidas = 1 * (runif(num) < p)
        actual <- matrix(vidas, nrow=dim, ncol=dim, byrow=TRUE)
        anterior = sum(actual)
        for (iteracion in 1:9) {
            siguiente = numeric()
            for (i in 1:num) {
                nuevo = paso(i)
                siguiente = c(siguiente, nuevo)
                if (nuevo == 1) {
                    vidas[i] = vidas[i] + 1
                } else {
                    ant = max(vidas[i], ant)
                    vidas[i] = 0
                }
            }
            vivos = sum(siguiente)
            mayor = max(mayor, anterior - vivos)
            if (vivos == 0) { # todos murieron
                break;
            }
            actual <- matrix(siguiente, nrow=dim, ncol=dim, byrow=TRUE)
        }
        datos = rbind(datos, c(p, mayor, ant))
    }
}
names(datos) = c('prob', 'mayor', 'racha')
print(datos)
