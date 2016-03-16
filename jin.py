import argparse
from pprint import pprint
import csv


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


pprint(jindexes)
