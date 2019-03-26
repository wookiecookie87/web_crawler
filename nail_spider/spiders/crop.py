import cv2
import numpy as np

def crop_img(folderName, filename):
    file = folderName+"/" + filename
    img = cv2.imread(file)

    height, width = img.shape[:2]
    h = height
    w = width
    crop_h = 608
    crop_w = w
    mid_y = int(h / 2)
    crop_y = mid_y - int(crop_h / 2)
    crop_x = 0

    img = img[crop_y:crop_y + crop_h, crop_x:crop_x + crop_w]
    rotated = cv2.transpose(img)
    cv2.imwrite(folderName+"/" + filename, rotated)
