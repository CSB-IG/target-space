import csv
import numpy as np
import svgwrite, random
from rugplot import CircleMarker, Scatter

from pprint import pprint

pca = [list() for n in range(5)]


reader = csv.reader(open('pca_targetspace.csv'))

reader.next()
N = 0
for l in reader:
    N += 1    
    for n in range(1,6):
        pca[n-1].append(float(l[n]))


npca = []
for c in pca:
    tmp = np.array(c)
    tmp *= 1.0/tmp.max()    
    npca.append(tmp)

    
pprint(npca)

markers = []
for i in range(N):
    markers.append(CircleMarker(x=npca[0][i], y=npca[1][i], r=2.5,
                                fill=random.choice(['purple', 'blue',
                                                    'green', 'orange', 'red'])))

s0 = Scatter(npca[0], npca[1], markers, insert=(100,30), size=(200,200))
s0.drawBorder(stroke='grey', fill='white', stroke_width=0.8)
s0.drawMarkers()
s0.drawDotDash(['e','s'], dash_height=15, stroke="grey", stroke_width=1.4)


rug = svgwrite.Drawing('example.svg')
rug.add(s0.dwg)
#rug.add(s1.dwg)
#rug.add(s2.dwg)
rug.save()
