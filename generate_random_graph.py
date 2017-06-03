import numpy as np

# size of graph
size = 49


def generate_random_graph(size):
    r = np.zeros((size, size))
    def random():
        return int(np.random.rand() * 100)

    range_arr = np.arange(size)
    for i in range_arr:
        for j in range_arr:
            if i != j and j > i:
                r[i][j] = r[j][i] = random()

    return r
