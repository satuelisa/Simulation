library(testit)
knapsack <- function(cap, peso, valor) {
    n <- length(peso)
    pt <- sum(peso) # deben ser enteros en este caso
    assert(n == length(valor))
    vt <- sum(valor) # pueden ser lo que sea
    if (pt < cap) { # cabe todo
        return(vt)
    } else {
        filas <- cap + 1 # una para cada posible peso acumulado desde cero hasta cap
        cols <- n + 1 # una para cada objeto y una extra al inicio para no llevar nada
        tabla <- matrix(rep(-Inf, filas * cols),
                       nrow = filas, ncol = cols) # al inicio todo vale negativo infinito
        for (fila in 1:filas) {
            tabla[fila, 1] <- 0 # todas las filas tienen un cero al inicio (no llevar nada da cero valor)
        }
        rownames(tabla) <- 0:cap # filas corresponden a pesos acumulados posibles
        colnames(tabla) <- c(0, valor) # columnas corresponden a objetos considerados
        for (objeto in 1:n) { # consideremos a cada objeto por turno
            p <- peso[objeto] # tomamos su peso a una variable
            v <- valor[objeto] # y su valor a otra variable
            for (acum in 1:(cap+1)) { # consideramos cada fila de la tabla
                 anterior <- acum - p
                 tabla[acum, objeto + 1] <- tabla[acum, objeto]               
                if (anterior > 0) { # si conocemos una combinacion con ese peso
                    tabla[acum, objeto + 1] <- max(tabla[acum, objeto], tabla[anterior, objeto] + v)
                } 
            }
        }
        print(tabla)
        return(max(tabla))
    }
}
peso <- c(1, 2, 4, 5, 5, 8, 12) # ordenados de menor a mayor
valor <- c(3, 8, 24, 7, 10, 12, 30)
print(knapsack(40, peso, valor))
