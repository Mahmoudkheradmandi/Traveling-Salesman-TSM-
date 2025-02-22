from random import randint as rnd


def mutation(population_list ,n ,ps):
    # for chiled
    length = ps*2
    for i in range(ps  ,length):
        cell1 = rnd(0, n-1)
        cell2 = rnd(0, n-1)
        if cell1 != cell2:
            population_list[i][cell1], population_list[i][cell2] = population_list[i][cell2] , population_list[i][cell1]
            i+=1
    return population_list