import numpy as np 

# Euclidean Distance
def distance(path):
    dis = 0
    for i in range(len(path)-1):
        dis += np.sqrt((path[i][0]-path[i+1][0])**2 + (path[i][1]-path[i][1])**2)
    return dis    