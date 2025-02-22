import cv2

# Drow Path Function
def drow_path(img , path , color):
    for i in range(len(path)-1):
        img = cv2.line(img , path[i] , path[i+1] , color , 2)
    return img

