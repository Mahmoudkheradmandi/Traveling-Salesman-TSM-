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
