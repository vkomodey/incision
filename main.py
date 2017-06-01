import numpy as np
from numpy import sin, abs, max
from helpers import *
import time
start_time = time.time()
# Initial params
# l - length of binary vector in generation
l = 10
# t - iteration maximum
tmax = 3
# N - individuals amount in generation.
N = 50
# P_c - crossingover likelihood
p_c = 0.3
# P_m - mutation likelihood
p_m = 0.1

G = np.array([
    [0, 2, 4, 0, 1],
    [2, 0, 0, 7, 6],
    [4, 0, 0, 0, 5],
    [0, 7, 0, 0, 3],
    [1, 6, 5, 3, 0],
])

prev_generation = init_first_generation(l, N)

print "---- %s seconds " % (time.time() - start_time)
