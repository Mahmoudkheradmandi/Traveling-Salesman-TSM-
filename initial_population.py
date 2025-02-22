from random import randint as rnd
from random import shuffle

def init_population(n, ps):
    # shahr random
    population_list = []
    for i in range(ps):
        path = [i for i in range(n)]
        shuffle(path)
        path += [None]
        population_list.append(path)
    return population_list    