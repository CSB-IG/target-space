import argparse
import csv


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

genes = sorted(pw.keys())



# create a rectangular matrix
rows = [ ['gene'] + genes,]
for gen1 in genes:
    row = [gen1, ]
    for gen2 in genes:
        row.append(jaccard_index(pw[gen1],pw[gen2]))
    rows.append(row)

    

# write matrix to output file
writer = csv.writer( args.output, delimiter="\t")
for row in rows:
    writer.writerow(row)

