from __future__ import division
import numpy as np
import time
import matplotlib.pyplot as plt
from numpy import sin, abs, max
from helpers import init_first_generation, mutate, x_f, crossingover
from generate_random_graph import generate_random_graph
from graph import Graph

start_time = time.time()
# Initial params

# t - iteration maximum
tmax = 20
# N - individuals amount in generation.
N = 100

graph_size = 40
# P_c - crossingover likelihood
p_c = 0.3
# P_m - mutation likelihood
p_m = 0.2

# graph = Graph([
    # [0, 19, 32, 11],
    # [19, 0, 5, 8],
    # [32, 5, 0, 1],
    # [11, 8, 1, 0]
# ])
graph = Graph(generate_random_graph(graph_size))
l = len(graph.g)


current_generation = init_first_generation(l, N)

results = np.empty(tmax)
for t in range(tmax):
    print t
    next_generation = np.empty([N, l])

    for k in range(N // 2):
        first_ancestor = graph.selection(current_generation)
        second_ancestor = graph.selection(current_generation)

        crossed_first_ancestor, crossed_second_ancestor = crossingover(first_ancestor, second_ancestor, p_c)

        mutated_first_ancestor = mutate(crossed_first_ancestor, p_m)
        mutated_second_ancestor = mutate(crossed_second_ancestor, p_m)

        next_generation[2*k - 1] = mutated_first_ancestor
        next_generation[2*k] = mutated_second_ancestor

    current_generation = next_generation
    results[t] = max([graph.fitness_function(geno) for geno in current_generation])

ll = plt.plot(np.arange(tmax), results)

plt.show()

print "---- %s seconds " % (time.time() - start_time)
