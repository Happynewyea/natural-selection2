import numpy as np

def mutation(genome):
    a = np.random.rand(1, 2)
    return genome + (a[0][0] *  a[0][1]) * 15
