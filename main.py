
import numpy as np 
import matplotlib.pyplot as plt
from city_randomizer import random_city_generator
from drow_cities import drow_cities
from drow_path import drow_path
from parameters import * 
from initial_population import init_population
from cross_over import cross_over
from mutation import mutation
from fitness import fitness
from sorter import sorter
from path_cordinates import path_cordinates

     

if __name__ == "__main__":
    cities_location = random_city_generator(N_CITIES ,AREA_WIDTH, AREA_HEIGHT)
    current_population = init_population(N_CITIES, POPULATION_SIZE)

    for i in range(1 ,EPOCH+1):
        current_population = cross_over(current_population , N_CITIES , POPULATION_SIZE)
        current_population = mutation(current_population , N_CITIES , POPULATION_SIZE)
        current_population = fitness(current_population, N_CITIES , cities_location)
        current_population = sorter(current_population , N_CITIES)
        current_population = current_population[:POPULATION_SIZE]
        #  print('Best path and Distance so far: ' , current_population[0])
        
    else:
        print('Best found solution: ' , current_population[0])
        area = np.full((AREA_WIDTH, AREA_HEIGHT, 3), 255, np.int16)
        area = drow_cities(area , cities_location , (0,0,255))
        current_path = path_cordinates(cities_location , current_population[0][:N_CITIES])
        current_path += [current_path[0]]
        area = drow_path(area , current_path ,(187, 134, 192))

        
        plt.imshow(area)
        plt.grid()
        plt.show()


