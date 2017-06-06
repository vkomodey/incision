from __future__ import division
from helpers import *

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
    
    def p_s(self, generation, ind_index):
        selected_ind = generation[ind_index]
        all_probs = [self.fitness_function(ind) for ind in generation]
        likelihood = self.fitness_function(selected_ind) / sum(all_probs)

        return likelihood

    def selection(self, generation):
        gen_len = len(generation)
        likelihood_array = [self.p_s(generation, i) for i in range(gen_len)]
        rand_float = random()

        for i in range(gen_len):
            if i != 0:
                likelihood_array[i] = likelihood_array[i] + likelihood_array[i - 1]
            if rand_float > likelihood_array[i - 1] and rand_float < likelihood_array[i]:
                return generation[i]

        # for i in range(gen_len - 1):
        #     if rand_float > likelihood_array[i] and rand_float < likelihood_array[i + 1]:
        #         return generation[i]

        return generation[gen_len - 1]
