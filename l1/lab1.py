import numpy as np
import matplotlib.pyplot as plt

def make_stat_row(seq):
    seq.sort()
    seq_no_dup = list(set(seq))
    seq_no_dup.sort()
    abs_freq = [seq.count(x) for x in seq_no_dup]
    rel_freq = [x / len(seq) for x in abs_freq]
    rel_freq_sums = [sum(rel_freq[0:i+1]) for i in range(len(rel_freq))]
    return (seq_no_dup, abs_freq, rel_freq, rel_freq_sums)


def plot_rel_freq_poly(seq_no_dup, rel_freq):
    rel_freq_poly = [rel_freq[seq_no_dup.index(x)] if x in seq_no_dup else 0
                    for x in range(seq_no_dup[-1]+1)]

    plt.plot(range(seq_no_dup[-1]+1), rel_freq_poly)
    plt.show()


def sample_mean(seq_no_dup, rel_freq):
    return selective_moment(seq_no_dup, rel_freq, 1)


def selective_moment(seq_no_dup, rel_freq, deg):
    return sum([pow(seq_no_dup[i], deg)*rel_freq[i]
           for i in range(len(rel_freq))])


def dispersion(seq_no_dup, rel_freq):
    return (selective_moment(seq_no_dup, rel_freq, 2) -
           pow(sample_mean(seq_no_dup, rel_freq), 2))


def central_selective_moment(seq_no_dup, rel_freq, deg):
    sm = sample_mean(seq_no_dup, rel_freq)
    return sum([pow(seq_no_dup[i]-sm, deg)*rel_freq[i]
           for i in range(len(rel_freq))])

def standard_deviation(seq_no_dup, rel_freq):
    return np.sqrt(dispersion(seq_no_dup, rel_freq))


def mode(seq_no_dup, abs_freq):
    max_n = max(abs_freq)
    cnt = abs_freq.count(max_n)
    if cnt == 1:
        return seq_no_dup[abs_freq.index(max_n)]
    for i in range(abs_freq.index(max_n)+1, len(abs_freq)):
        if abs_freq[i] != max_n:
            if max_n in abs_freq[i:]:
                return NaN
            return (seq_no_dup[abs_freq.index(max_n)] + seq_no_dup[i-1])/2


with open("data.txt") as file:
    bin, geom, pois = [[int(x) for x in l.split()] for l in file]

#print(make_stat_row(bin))
#print(make_stat_row(geom))
a, b, c, d = make_stat_row(bin)
# plot_rel_freq_poly(a, c)

print(central_selective_moment(a, c, 1))
print(central_selective_moment(a, c, 2))
print(dispersion(a, c))
