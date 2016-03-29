# Reescalar los valores del archivo pca_targetspace.csv entre cero y uno
# por columnas.

pca_data = read.csv("pca_targetspace.csv", header = TRUE, row.names = 1)
r = apply(pca_data, MARGIN = 2, FUN = function(X) (X - min(X))/diff(range(X)))
