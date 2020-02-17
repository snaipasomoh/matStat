import numpy as np

with open("data.txt") as file:
    bin, geom, pois = [[int(x) for x in l.split()] for l in file]

# print(bin, geom, pois, sep = "\n\n\n")
bin.sort()
geom.sort()
pois.sort()
