import os
import cv2
path = "image/"
images=[]
os.listdir(path)
os.splitext(file)
if ext in ['.gif', '.png', '.jpg', '.jpeg', '.jpeg']:
    file_name = path +"/" +file
    print (file_name)
    images.append()
    len(images)
    frame=cv2.imread(images[0])
    size = (width,height)
    print(size)
    out = cv2.VideoWritter('project avi', cv2.VideoWritter_fourcc(*'DIVX'), 0.8, size)
    cv2.imread()
    out.write()
    print("Done")