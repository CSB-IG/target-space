import argparse
import csv

import sys
import glob
import argparse
import os
import operator
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity




from pprint import pprint

# computes jacard index for two or mor sets
def jaccard_index(first, *others):
    return float( len( first.intersection(*others))) / float(len(first.union(*others)))


parser = argparse.ArgumentParser(description='')
parser.add_argument('--input', type=argparse.FileType('r'), required=True)
parser.add_argument('--output', type=argparse.FileType('w'), required=True)
args = parser.parse_args()


reader = csv.reader(args.input, delimiter=' ')
header = ['gen'] + reader.next()

# create dict of genes and their pathways
pw = {}
for r in reader:
    gen     = r[0]
    pw[gen] = set()
    for i in range(len(r)):
        # fields 1 thru 4 are cancer subtypes
        if i > 0 and i < 5:
            exp = "%s_%s" % (header[i],r[1])
            pw[gen].add( exp )
        # fields 6 onwards are pathways
        if i > 5 and int(r[i]):
            pw[gen].add(header[i])


txts = {}

for gene in pw:
    txts[gene] = " ".join(sorted(list(pw[gene])))



titulos=txts.keys()
documents=txts.values()
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
dicts = {t:{} for t in titulos}

i = 0
for row in cosine_similarity(tfidf_matrix[:], tfidf_matrix):
    tmp = {}
    j = 0
    for t in list(row):
        tmp[ titulos[j]]=t
        j += 1
    x = tmp
    sorted_x = sorted(x.items(), key=operator.itemgetter(1), reverse=True)
    dicts[titulos[i]] = sorted_x
    i += 1

pairs = {}
for gene1 in dicts:
    for similarity in dicts[gene1]:
        (gene2, cossim) = similarity
        pairs[(gene1,gene2)] = cossim





# write matrix to output file
writer = csv.writer( args.output, delimiter="\t")
writer.writerow(['gene',]+titulos)

for g1 in titulos:
    row = [g1, ] + [pairs[(g1,g2)] for g2 in titulos]   
    writer.writerow(row)
