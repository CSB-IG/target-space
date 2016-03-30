# Reescalar los valores del archivo pca_targetspace.csv entre cero y uno
# por columnas.

dataframe = read.csv(
	"pca_targetspace.csv",
	header = TRUE,
	row.names = 1
)

data = dataframe[,1:5]

dmin = min(data)
dinterval = diff(range(data))

r = apply(
	data,
	MARGIN = 1,
	FUN = function(x) (x - dmin)/dinterval
)

write.csv(t(r), file="pca_targetspace.csv", quote=FALSE)
