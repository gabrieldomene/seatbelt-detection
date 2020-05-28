"""
Script for saving individual ROI over static image, all images are placed inside the resource folder and then loaded
to a list for iterating over. Similar to the save.py, this one is made for static images.

NOTE: Select from top-left to bottom-right the ROI otherwise it will throw an error for image size.

"""

import cv2
import os

font = cv2.FONT_HERSHEY_SIMPLEX
ratio_scale = 0.25
rois = []
color = (0, 255, 255)

ratio_scale=0.3

def generate_roi(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        rois.append((x, y))
    if event == cv2.EVENT_LBUTTONUP:
        rois.append((x, y))
        if rois:
            roi_count = 0
            for i in range(0, len(rois), 2):
                roi_count += 1
                cv2.rectangle(roi_resize, rois[i], rois[i+1], color, 3)
                strRoi = "ROI {}".format(roi_count)
                cv2.putText(roi_resize, strRoi, rois[i], font, 1, (0, 255, 255), 2)
                cv2.imshow("ROI Selection", roi_resize)

count = 0
img_count =0
roi_number = 0
save_count = 0
playing = False
cv2.namedWindow("ROI Selection")
content = [img for img in os.listdir("resources/")]

while True:
    for file_img in content:
        img = cv2.imread("resources/{}".format(file_img))

        while not playing:
            roi_resize = cv2.resize(img, None, fx=ratio_scale, fy=ratio_scale)
            cv2.imshow("ROI Selection", roi_resize)
            cv2.setMouseCallback("ROI Selection", generate_roi)
            print("Waiting for ROI selection")
            if cv2.waitKey(0) == ord("c"):
                playing = True
                roi_number = int(len(rois)/2)
                print("Left while, started playing. . .")
                cv2.destroyAllWindows()
            
        if playing:
            roi_count = 0
            for i in range(0, len(rois), 2): # For with step 2 to get the pair [start, end]
                roi_count +=1 # variable for change the window name
                save_count += 1 # count variable used in setting a name for saving the img
                x_start, y_start = rois[i]
                x_end, y_end = rois[i+1]
                roi_name = "Roi {}".format(roi_count)
                new_roi = img[int(y_start/ratio_scale):int(y_end/ratio_scale), int(x_start/ratio_scale):int(x_end/ratio_scale)].copy()
                cv2.imshow(roi_name, cv2.resize(new_roi, None, fx=ratio_scale, fy=ratio_scale))
                cv2.imwrite("teste/{:05d}.png".format(save_count), new_roi)
            playing = False
            rois = []
            cv2.destroyAllWindows()
    break
