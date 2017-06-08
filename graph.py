from __future__ import division
from helpers import *
from numpy import random

class Graph():
    def __init__(self, g):
        self.g = g
        self.vertexes = np.arange(len(self.g))

    def addiction(self, genotype):
        return np.setdiff1d(self.vertexes, x_f(genotype))
    
    def fitness_function(self, genotype):
        U = x_f(genotype)
        V = self.addiction(genotype)
        
        weight = 0

        for u in U:
            for v in V:
                weight += self.g[u][v]

        return weight

    def selection(self, generation):
        gen_len = len(generation)

        first_gen = generation[int(gen_len * random.random())]
        second_gen = generation[int(gen_len * random.random())]

        return first_gen if self.fitness_function(first_gen) > self.fitness_function(second_gen) else second_gen
