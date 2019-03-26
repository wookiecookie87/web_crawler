import os
import cv2
import numpy as np
from tqdm import tqdm


# pip install opencv-python
# pip install tqdm


#######################################################################################
# 정철님                        앱                크롭 결과물
# 카메라: (1440 x 2560) -> (1440 x 2560)   -->   (1300 x 2310)
# 크롤링:  (608 x 1080) -> (1440 x 2560)   -->    (549 x 975)

# 정욱님
# 카메라: (1440 x 2560) -> (1080 x 1920)   -->   (1300 x 2310)
# 크롤링:  (608 x 1080) -> (1440 x 2560)   -->    (549 x 975)

#######################################################################################

MODE = 'check' # check / save
TYPE = 'crawl' # cam / crawl / db_check

img_dir = 'sample/nails'
mask_dir = 'sample/nails_mask'

img_save_dir = 'save/nails'
mask_save_dir = 'save/nails_mask'
label_save_dir = 'save/labels'

#######################################################################################


def get_start_idx():
    try:
        files = os.listdir(img_save_dir)
    except FileNotFoundError:
        return 0

    if len(files) == 0:
        return 0
    else:
        files.sort()
        last = int(files[-1].split('.')[0])
        return last + 1


start_idx = get_start_idx()

if os.path.exists(img_dir + "/.DS_Store") :
    os.remove(img_dir + "/.DS_Store")

if os.path.exists(mask_dir + "/.DS_Store") :
    os.remove(mask_dir + "/.DS_Store")

img_names = os.listdir(img_dir)
mask_names = os.listdir(mask_dir)

img_names.sort(reverse=False)
mask_names.sort()

if MODE == 'check':

    i = 0

    while 1:
        img = cv2.imread(os.path.join(img_dir, img_names[i]))
        print('image_name : ', os.path.join(img_dir, img_names[i]))
        mask = cv2.imread(os.path.join(mask_dir, mask_names[i]))
        print('image_name : ', os.path.join(mask_dir, mask_names[i]))

        if TYPE == 'cam':
            mask = cv2.resize(mask, (1440, 2560))

            img = img[:2310, 70:1370]
            mask = mask[:2310, 70:1370]

        elif TYPE == 'crawl':
            #mask = cv2.resize(mask, (800, 1422))
            #img = img[:1284, 39:761]
            #mask = mask[:1284, 39:761]
            mask = cv2.resize(mask, (608, 1080))
            img = img[:975, 29:578]
            mask = mask[:975, 29:578]

        img = cv2.resize(img, (360, 640))
        mask = cv2.resize(mask, (360, 640))

        out = cv2.absdiff(mask, img)
        out = cv2.cvtColor(out, cv2.COLOR_BGR2GRAY)

        _, out = cv2.threshold(out, 15, 255, 0)
        out = cv2.medianBlur(out, 5)

        cv2.putText(out, '%d' % (start_idx + i), (10, 20), cv2.FONT_HERSHEY_PLAIN, 2, [255,255,255], 1)
        cv2.imshow('img', img)
        cv2.imshow('mask', mask)
        cv2.imshow('out', out)
        k = cv2.waitKey(0)
        if k == 27:
            break
        elif k == ord('v'):
            i += 1
        elif k == ord('c'):
            i -= 1

        if i < 0:
            i = len(img_names)-1
        if i >= len(img_names):
            i = 0

    cv2.destroyAllWindows()

elif MODE == 'save':

    if not os.path.exists(img_save_dir):
        os.makedirs(img_save_dir)
    if not os.path.exists(mask_save_dir):
        os.makedirs(mask_save_dir)
    if not os.path.exists(label_save_dir):
        os.makedirs(label_save_dir)

    for i in tqdm(range(len(img_names))):
        img = cv2.imread(os.path.join(img_dir, img_names[i]))
        mask = cv2.imread(os.path.join(mask_dir, mask_names[i]))

        if TYPE == 'cam':
            mask = cv2.resize(mask, (1440, 2560))

            img = img[:2310, 70:1370]
            mask = mask[:2310, 70:1370]

        elif TYPE == 'crawl':
            #mask = cv2.resize(mask, (800, 1422))
            #img = img[:1284, 39:761]
            #mask = mask[:1284, 39:761]
            mask = cv2.resize(mask, (608, 1080))
            img = img[:975, 29:578]
            mask = mask[:975, 29:578]

        label = cv2.absdiff(mask, img)
        label = cv2.cvtColor(label, cv2.COLOR_BGR2GRAY)

        _, label = cv2.threshold(label, 15, 255, 0)
        label = cv2.medianBlur(label, 5)

        cv2.imwrite(os.path.join(img_save_dir, '%05d.png' % (start_idx + i)), img)
        cv2.imwrite(os.path.join(mask_save_dir, '%05d.png' % (start_idx + i)), mask)
        cv2.imwrite(os.path.join(label_save_dir, '%05d.png' % (start_idx + i)), label)

elif MODE == 'db_check':

    i = 0

    while 1:
        img = cv2.imread(os.path.join(img_dir, img_names[i]))
        print('image_name : ', os.path.join(img_dir, img_names[i]))
        mask = cv2.imread(os.path.join(mask_dir, mask_names[i]))
        print('image_name : ', os.path.join(mask_dir, mask_names[i]))

        img = cv2.resize(img, (360, 640))
        mask = cv2.resize(mask, (360, 640))

        out = cv2.absdiff(mask, img)
        out = cv2.cvtColor(out, cv2.COLOR_BGR2GRAY)

        _, out = cv2.threshold(out, 15, 255, 0)
        out = cv2.medianBlur(out, 5)

        cv2.putText(out, '%d' % (start_idx + i), (10, 20), cv2.FONT_HERSHEY_PLAIN, 2, [255,255,255], 1)
        cv2.imshow('img', img)
        cv2.imshow('mask', mask)
        cv2.imshow('out', out)
        k = cv2.waitKey(0)
        if k == 27:
            break
        elif k == ord('v'):
            i += 1
        elif k == ord('c'):
            i -= 1

        if i < 0:
            i = len(img_names)-1
        if i >= len(img_names):
            i = 0

    cv2.destroyAllWindows()