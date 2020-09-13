import numpy as np
import matplotlib.pyplot as plt
import math

V = 7
N = 5 + V % 16
P = 0.3 + 0.005*V
L = 0.5 + 0.01*V

def make_stat_row(seq):
    seq.sort()
    seq_no_dup = list(set(seq))
    seq_no_dup.sort()
    abs_freq = [seq.count(x) for x in seq_no_dup]
    rel_freq = [x / len(seq) for x in abs_freq]
    rel_freq_sums = [sum(rel_freq[0:i+1]) for i in range(len(rel_freq))]
    return (seq_no_dup, abs_freq, rel_freq, rel_freq_sums)


def plot_rel_freq_poly(seq_no_dup, rel_freq, teor):
    rel_freq_poly = [rel_freq[seq_no_dup.index(x)] if x in seq_no_dup else 0
                    for x in range(seq_no_dup[-1]+1)]

    x = range(seq_no_dup[0], seq_no_dup[-1]+1)
    t = [teor[i] for i in x]
    y = np.arange(0.0, max(max(rel_freq_poly), max(t)), 0.1)
    plt.title("Полигон относительных частот")
    plt.xlabel("X")
    plt.ylabel("Относительная частота")
    plt.xticks(x)
    plt.yticks(y)
    plt.grid()
    plt.plot(x, rel_freq_poly, x, t, "r")
    plt.legend(["Относительные частоты", "Теор. вероятности"])
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
                return math.nan
            return (seq_no_dup[abs_freq.index(max_n)] + seq_no_dup[i-1])/2

def assym(seq_no_dup, rel_freq):
    return (central_selective_moment(seq_no_dup, rel_freq, 3) /
           (standard_deviation(seq_no_dup, rel_freq)**3))

def exc(seq_no_dup, rel_freq):
    return (central_selective_moment(seq_no_dup, rel_freq, 4) /
           (standard_deviation(seq_no_dup, rel_freq)**4)) - 3

def plot_empiric(seq_no_dup, sum_freq):
    x = range(seq_no_dup[-1]+1)
    plt.xticks(x)
    plt.yticks(np.arange(0, 1.1, 0.1))
    xsp = np.arange(0, x[-1]+1, 0.01)
    ysp = [empiric(i, seq_no_dup, sum_freq) for i in xsp]
    plt.title("Эмпирическая функция распределения")
    plt.grid()
    plt.plot(xsp, ysp, "_")
    plt.show()

def empiric(x, seq_no_dup, sum_freq):
    ind = 0
    for i in range(len(seq_no_dup)):
        if seq_no_dup[i] > x:
            break
        ind += 1
    if ind < 1: return 0
    return sum_freq[ind-1]

def teor_geometric(p, seq_no_dup):
    return [p * (1-p)**(i-1) for i in range(seq_no_dup[-1]+1)]

def teor_binomial(n, p):
    return [math.comb(n, i) * p**i * (1-p)**(n-i) for i in range(n+1)]

def teor_poisson(l, seq_no_dup):
    return [math.exp(-l) * l**i / math.factorial(i) for i in seq_no_dup]

with open("data.txt") as file:
    bin, geom, pois = [[int(x) for x in l.split()] for l in file]



#print(make_stat_row(bin))
#print(make_stat_row(geom))
a, b, c, d = make_stat_row(pois)
# plot_rel_freq_poly(a, c, teor_poisson(L, a))
# print(a, b, c, d, sep="\n")
# plot_empiric(a, d)
# c = 1
# for i in pois:
#     print(i, end=" ")
#     if not (c % 10):
#         print("")
#     c += 1

# print(central_selective_moment(a, c, 1))
# print(central_selective_moment(a, c, 2))
# print(dispersion(a, c))

# print(teor_binomial(12, 0.335))
# print(teor_geometric(P, a))
print(teor_poisson(L, a))
# print(sample_mean(a, c), dispersion(a, c), standard_deviation(a, c),
# mode(a, b), assym(a, c), exc(a, c), sep="\n")
# print(st.moment(bin, 3)/(np.var(bin)**(3/2)))
