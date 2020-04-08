# --------------------------------------------------------------------------------------------
# Author: John Kufuor
# Project: Detecting sockets and radiators in 360◦ images of indoor spaces using deep learning
# ---------------------------------------------------------------------------------------------

import numpy as np
import cv2
import os
import glob


# Opens a image in RGB mode
def tile(path):
    for file in glob.glob(path + '/*.jpg'):
        im = cv2.imread(file)
        height, width, channels = im.shape
        w = int(width/3)
        h = int(height/2)
        for z in range(0,2):
            for i in range(0,3):
                y=int(h*z)
                x=int(w*i)
                crop = im[y:y+h, x:x+w]
                cv2.imwrite('{}-{}{}.png'.format(file[-12:-4], i, z), crop)


image_path = os.getcwd()
tile(image_path)
