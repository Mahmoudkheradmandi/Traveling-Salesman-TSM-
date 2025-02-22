from path_cordinates import path_cordinates
from distance import euclidean_distance

def fitness(population_list ,n , location_list):
    for i in range(len(population_list)):
        if population_list[i][-1] == None:
            current_path = path_cordinates(location_list , population_list[i][:n]+[population_list[i][0]])
            d = euclidean_distance(current_path)
            population_list[i][n] = d
    return population_list  
    