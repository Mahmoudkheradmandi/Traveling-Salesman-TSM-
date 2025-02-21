
import numpy as np 
import matplotlib.pyplot as plt
from random import randint as rnd
from city_randomizer import city_randomizer
from distance import distance
from drow_cities import drow_cities
from drow_path import drow_path
from parameters import * 
from random_path import random_path

     
# Main

area = np.full((AREA_HEIGHT , AREA_WIDTH , 3) , 255 , np.uint8)
city_locations = city_randomizer(N_CITIES , AREA_HEIGHT , AREA_WIDTH)
best_distance = None
best_path = []
counter = 0


while True:
    area = np.full((AREA_HEIGHT , AREA_WIDTH , 3) , 255 , np.uint8)
    area = drow_cities(area , city_locations , (0,0,0,0))
    path = random_path(city_locations)
    area = drow_path(area , path , (26 , 32 , 40))
    d = distance(path)
    if best_distance != None:
        if d < best_distance:
            best_distance = d
            best_path = path.copy()    
    else: 
        best_distance = d
        best_path = path.copy()
    
    area = drow_path(area , best_path , (255 , 87 , 52))

    plt.imshow(area)
    plt.title(f'Best distance so far :  , {best_distance}')
    plt.xlabel(str(counter))
    plt.grid()
    plt.pause(0.5)
    plt.clf()
    counter += 1

plt.imshow(area)
plt.title(f'Best distance so far :  , {best_distance}')
plt.xlabel(str(counter))
plt.gride()
plt.show()
