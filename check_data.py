import pandas as pd
import numpy as np
import cv2
import os
from os import listdir
import shutil
import math

imageFolder = "crawled_img/"
group_count = 200


fileNames = listdir(imageFolder)

file_count = len(fileNames)

folder_count = math.ceil(file_count/group_count)

print(folder_count)

for i in range(folder_count):
    folderName = imageFolder+'%05d'% (i+1)
    os.mkdir(folderName)
    start_index = group_count * i
    end_index = start_index + group_count
    for idx, filename in enumerate(fileNames[start_index:end_index]):
        print(idx, os.path.join(imageFolder, filename))
        originalPath = os.path.join(imageFolder, filename)
        destPath = os.path.join(folderName, filename)
        shutil.move(originalPath, destPath)





# data = pd.read_csv("nail_image_data.csv")
# df = pd.DataFrame(data)
# imageFolder = "crawled_img/"
# fileNames = listdir(imageFolder)
#
# index = df[df.file_name == "352911af-8263-4fdf-b055-2f056dcc31d7.jpg"].index.values.astype(int)[0]
#
# new_df = pd.DataFrame([], columns=[], index=[])
#
#
#
# for idx, filename in enumerate(fileNames):
#     file = filename.split("_")
#     print(idx, file[1])
#     index = df[df.file_name == file[1]].index.values.astype(int)[0]
#     dict_data = df.iloc[index].to_dict()
#     new_df = new_df.append(dict_data, ignore_index=True)
#
# df = df.reset_index()
# new_df.to_csv(r'nail_image_data_indexed.csv')






# data = pd.read_csv("nail_image_data.csv")
# df = pd.DataFrame(data)
# cols = [2]
# filename_df = df[df.columns[cols]]
# fileNames = np.array(filename_df)
#
#
#
# file_num = 1
#
# print(len(fileNames))
# print(fileNames[0][0])
#
# for idx, filename, in enumerate(fileNames):
#     imageFolder = "crawled_img2/"
#     imagePath = imageFolder + filename[0]
#
#
#     img = cv2.imread(imagePath)
#
#     if img is not None:
#         height, width = img.shape[:2]
#         if(height >= 1080):
#             print(fileNames[idx], img.shape[:2], '%05d'% file_num+"_"+filename[0])
#             #cv2.imshow("imge",img)
#             os.rename(imagePath, os.path.join(imageFolder, '%05d'% file_num+"_"+filename[0]))
#             file_num += 1
#         else:
#         #     df = df.drop([idx], axis=0)
#             os.remove(imagePath)
#
#     #     print(df.iloc[idx])
#     #     df=df.drop([idx])
#
#
#
#
