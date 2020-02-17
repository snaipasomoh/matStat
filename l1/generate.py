import numpy as np

V = 7
N = 5 + V % 16
P = 0.3 + 0.005*V
L = 0.5 + 0.01*V

with open("data.txt", 'w') as file:
    a = np.random.binomial(N, P, 200)
    for i in a: file.write(str(i) + " ")
    file.write("\n")
    a = np.random.geometric(P, 200)
    for i in a: file.write(str(i) + " ")
    file.write("\n")
    a = np.random.poisson(L, 200)
    for i in a: file.write(str(i) + " ")
    file.write("\n")
