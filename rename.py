import os
from random import randint



path = os.path.join(os.getcwd(), "dataset/train")
image_list = os.listdir(path)
print("Found {} files in {}" .format(len(image_list), path))

def suffle_rename(path, images):
    success = 0
    failed = 0
    for idx, img in enumerate(images):
        name, _ = img.split("-")
        # id = randint(1, 99999999)
        new_name = name + "-" + str(randint(1, 9999999)) +".png"
        try:
            os.rename(os.path.join(path, img), os.path.join(path, new_name))
            success += 1
        except:
            print("{} failed to rename" .format(img))
            failed += 1
        print("[{}-{}] Old: {} - New: {}" .format(idx+1, len(images), img, new_name))
    print ("OK {} - FAILED {}" .format(success, failed))

suffle_rename(path, image_list)
