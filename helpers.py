import numpy as np
from numpy import sum

def random():
    return np.random.rand()

def generate_individual(length):
    vec = np.random.randint(2, size=length)

    return vec

def init_first_generation(vec_length, ind_amount):
    generation = np.empty([ind_amount, vec_length])
    for i in range(ind_amount):
        generation[i] = generate_individual(vec_length)

    return generation

def x_f(genotype):

def p_s(generation, fitness_func, x_f, ind_index):
    selected_ind = generation[ind_index]
    all_probs = [fitness_func(x_f(ind)) for ind in generation]
    likelihood = fitness_func(x_f(selected_ind)) / sum(all_probs)

    return likelihood

def selection(generation, fitness_function, p_s, x_f):
    gen_len = len(generation)
    likelihood_array = [p_s(generation, fitness_function, x_f, i) for i in range(gen_len)]
    for i in range(gen_len):
        if i != 0:
            likelihood_array[i] = likelihood_array[i] + likelihood_array[i - 1]
    rand_float = random()

    for i in range(gen_len - 1):
        if rand_float > likelihood_array[i] and rand_float < likelihood_array[i + 1]:
            return generation[i]

    return generation[gen_len - 1]

def crossingover_coord(vec_len, p_c):
    for i in range(vec_len):
        r = random()
        if r > p_c:
            return i

    return vec_len - 1

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
