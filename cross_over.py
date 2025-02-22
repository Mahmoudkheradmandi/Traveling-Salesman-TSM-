

def cross_over(population_list ,n ,ps):
    for i in range(ps):
        path =population_list[i][:n] + [None]
        population_list.append(path)
    return population_list