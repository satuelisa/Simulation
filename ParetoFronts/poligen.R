poli <- function(maxdeg, varcount, termcount) {
    f <- data.frame(variable=integer(),
                    coef=integer(),
                    degree=integer())
    for (t in 1:termcount) {
        var <- sample(1:varcount, 1)
        deg <- sample(0:maxdeg, 1)
        f <-  rbind(f, c(var, runif(1), deg))
    }
    names(f) <- c("variable", "coef", "degree")
    return(f)
}

eval <- function(polinomio, asignacion) {
    acumulado <- 0.0
    cuantos = dim(polinomio)[1] # filas
    for (t in 1:cuantos) {
        termino <- polinomio[t,] # un renglon
        valor = asignacion[termino$variable]
        grado = termino$degree
        mult = termino$coef # coeficiente
        evaluacion = mult * valor^grado # puro termino
        acumulado = acumulado + evaluacion
    }
    return(acumulado)
}

vc <- 4 # cuantas variables
md <- 3 # grado maximo
tc <- 5 # cuantos terminos
f <- poli(md, vc, tc) # crearlo
print(f) # verlo
a = runif(vc) # asignacion aleatoria
print(eval(f, a)) # evaluar

