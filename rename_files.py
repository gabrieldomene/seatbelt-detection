import os
import cv2

suffix = (".jpg", ".png", ".jpeg")

img_only = [file for file in os.listdir("FOLDER WHERE IMAGES ARE STORED") if file.endswith(suffix)]

count = 0

for file in img_only:
	new_name = "train/{:07d}.png".format(count)
	old_name = "train/{}".format(file)
	old_annotation = "train/{}.txt".format(file[:-4])
	new_annotation = "train/{:07d}.txt".format(count)
	os.rename(old_name, new_name)
	os.rename(old_annotation, new_annotation)
	count += 1
	print("[{}/{}]" .format(count, len(img_only)))
