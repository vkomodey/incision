import numpy as np
from numpy import sum

def crossingover_coord(vec_len, p_c):
    for i in range(vec_len):
        r = random()
        if r > p_c:
            return i

    return vec_len - 1

def x_f(genotype):
    return np.argwhere(genotype).flatten()

def random():
    return np.random.rand()

def generate_individual(length):
    vec = np.random.randint(2, size=length)

    return vec

def init_first_generation(vec_length, ind_amount):
    generation = np.empty([ind_amount, vec_length])
    for i in range(ind_amount):
        genotype = generate_individual(vec_length)

        # TODO implement more stable regeneration
        if len(np.argwhere(genotype > 0)) == 0:
            genotype = generate_individual(vec_length)

        generation[i] = genotype

    return generation

def crossingover(first_ancestor, second_ancestor, p_c):
    vec_len = len(first_ancestor)
    coord = crossingover_coord(vec_len, p_c)
    crossed_first_ancestor = [first_ancestor[i] if i <= coord else second_ancestor[i] for i in range(vec_len)]
    crossed_second_ancestor = [second_ancestor[i] if i <= coord else first_ancestor[i] for i in range(vec_len)]

    yield crossed_first_ancestor
    yield crossed_second_ancestor


def mutate(individual, p_m):
    vec_len = len(individual)
    mutated = np.empty(vec_len)
    r = random()

    for i in range(vec_len):
        if r > p_m:
            mutated[i] = 0 if individual[i] == 1 else 1
        else:
            mutated[i] = individual[i]

    return mutated
