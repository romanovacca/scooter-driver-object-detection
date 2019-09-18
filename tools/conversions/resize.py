import cv2
import os
from skimage import io

#In KB
DESIRED_IMAGESIZE = 125
dir_path = "/your/custom/path/"
extensions = [".jpg",".JPG",".JPEG",".jpeg"]

for filename in os.listdir(dir_path):
    full_path = dir_path + '/' + filename
    if filename.endswith(tuple(extensions)):
        # If file is smaller than X amount of KB
        if os.path.getsize(full_path)/1000 > DESIRED_IMAGESIZE:
            image = cv2.imread(full_path)
            resized = cv2.resize(image,None,fx=0.35, fy=0.35, interpolation=cv2.INTER_AREA)
            io.imsave(full_path, resized)