import argparse
import csv
from scipy.cluster.hierarchy import dendrogram
from scipy.cluster.hierarchy import linkage
import numpy as np
import matplotlib
matplotlib.use('svg')
import matplotlib.pyplot as plt


from pprint import pprint

# computes jacard index for two or mor sets
def jaccard_index(first, *others):
    return float( len( first.intersection(*others))) / float(len(first.union(*others)))


parser = argparse.ArgumentParser(description='')
parser.add_argument('tablota', type=argparse.FileType('r'))
args = parser.parse_args()


reader = csv.reader(args.tablota, delimiter=' ')
header = ['gen'] + reader.next()

# create dict of genes and their pathways
pw = {}
for r in reader:
    gen = r[0]
    pw[gen] = set()
    for i in range(len(r)):
        if i > 5 and int(r[i]):
            pw[gen].add(header[i])



genes = pw.keys()

jindexes = {}
for gen1 in genes:
    for gen2 in genes:
        if len(pw[gen1]) and len(pw[gen2]):            
            jindexes[(gen1, gen2)] = jaccard_index(pw[gen1],pw[gen2])







# count intersections, place them in a table (rows are lists of cols)

rows = []
for i in sorted(genes):
    col = []
    for j in sorted(genes):
        if (i,j) in jindexes:
            col.append(jindexes[(i,j)])
        else:
            col.append(0)
    rows.append(col)
rows = np.array( rows )


algorythms = [ 'average',
               'complete',
               'ward',
               'centroid',
               'single',
               'weighted',]


for algorythm in algorythms:
        # plot dendrograms
        fig = plt.figure(figsize=(15,40))


        fig.add_subplot()
        linkage_matrix = linkage(rows, algorythm)

        a = dendrogram(linkage_matrix,
                       color_threshold=1,
                       labels=sorted(genes),
                       show_leaf_counts=False,
                       leaf_font_size=5,
                       leaf_rotation=0.0,
                       orientation='left',
               )
        plt.savefig('dendrogram_%s.svg' % algorythm)
        plt.close()
