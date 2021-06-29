import matplotlib.pyplot as plt
import numpy as np
from utils import *

fp = open("out.npy","w+")

print("Starting")
bfa_arr = np.linspace(0.2, 4, 20)
poly, _ = mont_carlo_poly_sim(None, 10**6, N,b*f*a)
#plt.show()
#fig = plt.figure()
out = [poly]
print(0)
for idx,bfa in enumerate(bfa_arr):
    print(idx)
    poly, _ = mont_carlo_poly_sim(poly, 10**6, N,bfa)
    x,y = calc_curve(poly)
    #plt.plot(x, y)
    out.append(poly)
out = np.array(out)
np.save(fp,out)
#plt.show()
