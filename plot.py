import matplotlib.pyplot as plt
import numpy as np
from utils import *

bfa_arr = np.linspace(0.2, 4, 20)
poly, _ = mont_carlo_poly_sim(None, 10**6, N,b*f*a)
plt.show()
fig = plt.figure()

for bfa in bfa_arr:
    poly, _ = mont_carlo_poly_sim(poly, 10**6, N,bfa)
    x,y = calc_curve(poly)
    plt.plot(x, y)
plt.show()
