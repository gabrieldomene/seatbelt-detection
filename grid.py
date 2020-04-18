import numpy as np
import cv2
import os
import time
from random import sample

path_images = os.path.join(os.getcwd(), "dataset")
path_content = os.listdir(path_images)
path_content = sample(path_content, len(path_content))

while True:
    
    for idx, image in enumerate(path_content[:1]):
        '''Iterate over list of images'''
        name = os.path.join(path_images, image)
        print("input: {}" .format(name))
        img = cv2.imread(name, 1)

        height, width = img.shape[:2]
        # print("W:{} H:{}" .format(width, height))
        step_height = height//10
        step_width = width//10
    
        for step in range(1, 10):
            print(step_height*step, step_width*step)
            cv2.line(img, (0, step_height*step), (width, step_height*step), (0, 255, 0), 3)
            cv2.line(img, (step_width*step, 0), (step_width*step, height), (255, 0, 0), 3)

        img1 = img[5*step_height:, :]
        img2 = img[:5*step_height, :]
        # img3 = img[5*step_height:height, :]
        # img4 = img[5*step_height:height, :]

        cv2.imwrite("down"+image, img1)
        cv2.imwrite("up"+image, img2)

    break
    # if cv2.waitKey(1) & 0XFF == ord("q"):
    #     break

cv2.destroyAllWindows()