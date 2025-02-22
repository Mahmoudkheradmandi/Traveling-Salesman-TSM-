import cv2

# Drow Cities    
def drow_cities(img , location_list , color):
    for city in location_list: 
        img = cv2.circle(img , city , 7 , color , -1)
    return img    
