
require("data.table")
##massaging jin
#read jin table 
jin<- fread(input = "genes_jin.tsv",data.table = FALSE)
rownames(jin)<-jin[,1]
jin<-jin[,-1]
#hierarchical clustering by jin
clust_jin <- hclust(d = dist(x = as.matrix(jin)))
#get 10 clusters from jin
groups <- cutree(clust_jin, k = 10)
#write out groups as table 
write.table(cutree(clust_jin, k = 10), file = "grupos_genes_10_jin.txt", quote = FALSE, col.names = FALSE)
##