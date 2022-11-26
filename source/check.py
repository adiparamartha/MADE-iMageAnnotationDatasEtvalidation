# importing cv2 
import cv2 
import json
import random
import tkinter as tk
   
# path 
path = r'D:\3D Printing\0. Dataset Project 2022\20%\1.DLP(3557)\DLPXCXABSL1XXXXCD1X1102A.png'
json_path = r'D:\3D Printing\0. Dataset Project 2022\20%\1.DLP(3557)\DLPXCXABSL1XXXXCD1X1102A.png.json'
print(type(path))
f = open(json_path)
data = json.load(f)
annot_x = data['annotation_info']['Annotations[]_x']
annot_y = data['annotation_info']['Annotations[]_y']
print(annot_x, annot_y)

f.close()

def random_color():
    rgbl=[255,0,0]
    random.shuffle(rgbl)
    return tuple(rgbl)

img = cv2.imread(path)

annot_x = annot_x[1:-1]
annot_x = annot_x.split(', ')
annot_y = annot_y[1:-1]
annot_y = annot_y.split(', ')

print(annot_x)
print(annot_y)

cv2.rectangle(img, ( int(float(annot_x[0])), int(float(annot_y[0])) ), ( int(float(annot_x[1])), int(float(annot_y[1])) ), random_color(), 2)


print(img)
cv2.imshow('image', img)
  
cv2.waitKey(0)
cv2.destroyAllWindows()