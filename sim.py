from random import randint as rint
import numpy as np
import math
from utils import *
def get_sums():
    init_poly = np.array([states[rint(0,3)] for i in range(N)])
    sums = None
    for _ in range(10**2):
        _, sum = mont_carlo_poly_sim(init_poly, 10**4, N, b*f*a)
        if sums is None:
            sums = sum
        else:
            sums = np.vstack((sums,sum))
    return np.sum(sums, axis=0)

print(get_sums())


