# Reescalar los valores del archivo pca_targetspace.csv entre cero y uno
# por columnas.

# Leer la información
data = read.csv("pca_targetspace.csv",
	header = TRUE,
	row.names = 1,
)

# ordenar la información para obtener los parámetros comparables
sorted = apply(data,
	MARGIN = 2,
	FUN = sort
)

# Estos valores son los que se usan para todas las columnas
means = rowMeans(sorted)

# Reemplazar los valores en el orden adecuado
order = data
r = data
for (n in colnames(data)) {
	# Aquí encontramos el orden de los vectores
	order[[n]] = order(data[[n]])
	# Aquí reemplazamos los valores por las medias en el orden correcto.
	r[[n]] = means[order[[n]]]
}

r = apply(r,
	MARGIN = 2,
	FUN = function(x) (x - min(x)) / diff(range(x))
)

# Finalmente escribir el archivo
write.csv(r, file="pca_targetspace.csv", quote=FALSE)
