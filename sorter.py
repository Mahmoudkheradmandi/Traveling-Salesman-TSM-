

def sorter(population_list , k):
    population_list.sort(key=lambda x: x[k])
    return population_list