import numpy as np

def make_stat_row(seq):
    seq.sort()
    seq_no_dup = list(set(seq))
    seq_no_dup.sort()
    abs_freq = [seq.count(x) for x in seq_no_dup]
    rel_freq = [x / len(seq) for x in abs_freq]
    rel_freq_sums = [sum(rel_freq[0:i+1]) for i in range(len(rel_freq))]

    # print(seq_no_dup)
    # print(abs_freq)
    # print(rel_freq)
    # print(rel_freq_sums)

with open("data.txt") as file:
    bin, geom, pois = [[int(x) for x in l.split()] for l in file]

#print(make_stat_row(bin))
#print(make_stat_row(geom))
print(make_stat_row(pois))
