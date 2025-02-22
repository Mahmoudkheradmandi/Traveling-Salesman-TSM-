from random import randint as rnd

# City Randomizer Function 
def city_randomizer(n , w , h): 
    offset = 20
    city_list = []
    for i in range(n): 
        x = rnd(offset , w+offset)
        y = rnd(offset , h+offset)
        city_list.append([x , y])
    return city_list


def random_city_generator(n, w, h):
    offset = 20
    cities = []
    i = 0
    while i < n:
        city_location = [rnd(offset,w-offset), rnd(offset,h-offset)]
        if city_location not in cities:
            cities.append(city_location)
            i+=1
    return cities