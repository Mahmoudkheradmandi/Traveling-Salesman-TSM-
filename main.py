
import numpy as np 
import matplotlib.pyplot as plt
from random import randint as rnd
from city_randomizer import city_randomizer
from distance import distance_calculator
from drow_cities import draw_cities
from drow_path import draw_path
from parameters import * 
from random_path import random_path
from lexicographic import lexicographic_ordering
from path_cordinates import path_cordinates
     
# Main
if __name__ == "__main__":
        best_path = []
        best_path_distance = []
        cities = city_randomizer(N_CITIES, AREA_WIDTH, AREA_HEIGHT)
      
        
        for path in lexicographic_ordering(N_CITIES):
            area = np.full((AREA_WIDTH, AREA_HEIGHT, 3), 255, np.int16)
            area = draw_cities(area, cities)
            
            path_cord = path_cordinates(cities, path)
            
            area = draw_path(area, path_cord, (0,255,0))
            path_length = distance_calculator(path_cord)
            if len(best_path) == 0:
                best_path = path_cord
                best_path_distance = path_length
            else:
                if path_length < best_path_distance:
                    best_path = path_cord
                    best_path_distance = path_length

            area = draw_path(area, best_path, (187, 134, 192))

            plt.imshow(area)
            plt.title("Best Distance So far: {}".format(best_path_distance))
            plt.pause(0.5)
            plt.clf()
        area = np.full((AREA_WIDTH, AREA_HEIGHT, 3), 255, np.int16)
        area = draw_cities(area, cities)
        area = draw_path(area, best_path, (187, 134, 192))
        plt.imshow(area)
        plt.title("Best Found Distance\n {}".format(best_path_distance))
        plt.xlabel("Finished")
        plt.show()
else:
        print("Please Run the main.py file!")