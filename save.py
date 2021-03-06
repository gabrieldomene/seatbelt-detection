import cv2
import os
import time
from random import randint
'''
This script is responsible for generate .png images from the video frame, the path
must be inside the videos/ folder in order to work properbly. The adjustment can be
done by modifying the COUNT % 10 == 0 (here it saves every 10 frames) for eliminate 
the possible duplicates scenarios.

The resized image can be select to be visible to go with the frame count.
The frames are saved by the imwrite() function in the desired folder, following the
count variable to name in order.

The frame roi are differente for each video and were selected based manual selection.
'''

font = cv2.FONT_HERSHEY_SIMPLEX
ratio_scale = 0.25
rois = []
color = (0, 255, 255)
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
cap = cv2.VideoCapture("VIDEO PATH HERE")
frame_lenght = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
playing = False
cv2.namedWindow("ROI Selection")

roi_number = 0
save_count = 0
while True:
    _, frame = cap.read()
    if not _:
        break
    
    while not playing:
        roi_resize = cv2.resize(frame, None, fx=ratio_scale, fy=ratio_scale)
        cv2.imshow("ROI Selection", roi_resize)
        cv2.setMouseCallback("ROI Selection", generate_roi)
        print("Waiting for releasing the ROI selections")
        if cv2.waitKey(0) == ord("c"):
            playing = True
            roi_number = int(len(rois)/2)
            print("Left while, started playing/saving. . .")
            cv2.destroyAllWindows()

    if playing:
        tempo = float(1/60)
        time.sleep(tempo)
        if count % 10 == 0: # Modify here the pace for saving every X frames
            resize = cv2.resize(frame, None, fx=ratio_scale, fy=ratio_scale)
            progress = "[{}/{}]".format(count, frame_lenght)
            roi_count = 0
            for i in range(0, len(rois), 2): # For with step 2 to get the pair [start, end]
                roi_count +=1 # variable for change the window name
                save_count += 1 # count variable used in setting a name for saving the img
                x_start, y_start = rois[i]
                x_end, y_end = rois[i+1]
                roi_name = "Roi {}".format(roi_count)
                new_roi = frame[int(y_start/ratio_scale):int(y_end/ratio_scale), int(x_start/ratio_scale):int(x_end/ratio_scale)].copy()
                cv2.imshow(roi_name, cv2.resize(new_roi, None, fx=ratio_scale, fy=ratio_scale))
                cv2.imwrite("DATASET FOLDER SELECT/{:05d}.png".format(save_count), new_roi)
                cv2.imwrite("teste{:05d}.png".format(save_count), frame)
        count += 1
        
        if cv2.waitKey(1) & 0XFF == ord("q"):
            break

cap.release()
