tams = c(1, 2, 3, 4, 5, 6, 7, 8, 9, 12)
cants = c(1, 1, 3, 1, 2, 2, 1, 2, 1, 1)
datos = data.frame(tam = tams, cant = cants)
datos$cont = datos$tam * datos$cant
filtro = 6 # umbral de filtrado (se atrapan mayores)
filtrados = datos[datos$tam >= filtro,]
n = sum(datos$cont) # total de particulas
f = sum(filtrados$cont) # particulas removidas
100 * f/n # porcentaje exitosamente filtrado
