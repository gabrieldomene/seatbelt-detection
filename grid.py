import numpy as np
import cv2
import os
import time
from random import sample

path_images = os.path.join(os.getcwd(), "dataset")
path_content = os.listdir(path_images)
path_content = sample(path_content, len(path_content))

count = 0
while True:
    for idx, image in enumerate(path_content):
        '''Iterate over list of images'''
        name = os.path.join(path_images, image)
        img = cv2.imread(name, 1)

        height, width = img.shape[:2]
        step_height = height//10
        step_width = width//10
        
        # Split in half and flip for dat aug
        img_down = img[5*step_height:, :]
        img_up = img[:5*step_height, :]
        img_down_flip = cv2.flip(img_down, 1)
        img_up_flip = cv2.flip(img_up, 1)

        # cv2.imshow("Down region", cv2.resize(img_down, None, fx=0.3, fy=0.3))
        # cv2.imshow("Down FLIPPED region", cv2.resize(img_down_flip, None, fx=0.3, fy=0.3))
        # cv2.imshow("Up region", cv2.resize(img_up, None, fx=0.3, fy=0.3))
        # cv2.imshow("Up FLIPPED region", cv2.resize(img_up_flip, None, fx=0.3, fy=0.3))
        
        path_save = os.path.join(os.getcwd(), "data_aug/")
        cv2.imwrite(path_save+"{:04d}.png".format(count), img_down)
        cv2.imwrite(path_save+"{:04d}.png".format(count+1), img_down_flip)
        cv2.imwrite(path_save+"{:04d}.png".format(count+2), img_up)
        cv2.imwrite(path_save+"{:04d}.png".format(count+3), img_up_flip)
        count += 4
        print("[Process] - Created: {:04d}/{:04d} - Iterating {:03d}/{}" .format(count, len(path_content)*4, idx+1, len(path_content)))
     
    break

cv2.destroyAllWindows()