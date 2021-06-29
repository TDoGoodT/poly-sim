from random import randint as rint
from random import random as rand
import numpy as np
import math

# consts
N=10**3
b=10
f=1
a=1
states = np.array([(1,0),(-1,0),(0,1),(0,-1)])


# functions
def mont_carlo_poly_sim(poly, i, N, bfa):
    if poly is None:
        poly = np.array([states[rint(0,3)] for i in range(N)])
    for x in range(i):
        #1
        state_idx = rint(1,N-1)
        s_old_state = poly[state_idx]

        # get same index
        for idx, line in enumerate(states):  
            if (line == s_old_state).all():
                same_idx = idx
        diff_states = np.delete(states,same_idx,0)

        #2
        s_new_state = diff_states[rint(0,2)]

        #3
        bol_fac = math.exp((bfa)*(s_new_state[0]-s_old_state[0]))

        #4 
        if rand() < bol_fac:
            poly[state_idx] = s_new_state

        #5
        sum = np.sum(poly, axis=0)
    return poly, sum

def calc_curve(poly):
    x = []
    y = []
    curr_x = 0
    curr_y = 0
    for sig in poly:
        curr_x += sig[0]
        curr_y += sig[1]
        x.append(curr_x)
        y.append(curr_y)
    return x , y