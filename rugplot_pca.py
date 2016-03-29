import csv
import numpy as np
import svgwrite, random
from rugplot import CircleMarker, Scatter
from itertools import combinations

from pprint import pprint

pca = [list() for n in range(5)]

colors = ['olivedrab', 'navajowhite',
          'indigo', 'tan',
          'slategrey', 'palegreen',
          'maroon', 'brown',
          'lightsteelblue', 'khaki', ]


gen_color = {}
catreader = csv.reader(open('grupos_genes_10_jin.txt'), delimiter=" ")
for g in catreader:
    gen_color[g[0]] = colors[int(g[1])-1]


reader = csv.reader(open('pca_targetspace.csv'))

reader.next()

markers = []
for l in reader:
    markers.append(CircleMarker(r=0.2, fill=gen_color[l[0]]))    
    for n in range(1,6):
        pca[n-1].append(float(l[n]))

    



    

npca = []
for c in pca:
    tmp = np.array(c)
    tmp *= 1.0/tmp.max()    
    npca.append(tmp)

rug = svgwrite.Drawing('example.svg')

pairs = []
for p in combinations(range(5),2):
    pairs.append(p)

for i in range(5):
    for j in range(5):
        if (i,j) in pairs:
            s = Scatter(npca[i], npca[j], markers, insert=(i*200+10,j*200+10), size=(200,200))
            s.drawBorder(stroke='grey', fill='white', stroke_width=0.8)
            s.drawMarkers()
            s.drawDotDash(['w','e','s','n'], dash_height=5, stroke="grey", stroke_width=0.2)
            rug.add(s.dwg)

rug.save()
