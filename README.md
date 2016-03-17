# target-space
Clustering genes by pathways, expression levels in cancer subtypes.


## Jaccard Index

The script '''jin.py''' will take the
druggable_target_space_brcan_lfc_plus_or_minus_allpathways.txt table
as input and create a rectangular matrix: rows and columns are the set
of genes, cells contain the Jaccard Index of the sets of both genes.
See the [data](data).

