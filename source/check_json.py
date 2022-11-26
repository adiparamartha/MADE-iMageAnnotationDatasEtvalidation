from pathlib import Path
import os, json

errorType =[]
jsonFile = []
imageFile = []
match = 0

for jsonfile in Path(r'D:\3D Printing\0. Dataset Project 2022\20%\5.I_FDM(2015)').glob("**/*.json"):
    try:
        jsonFile.append(jsonfile)
    except Exception as e:
        print(jsonfile, "fail", e)

for imgfile in Path(r'D:\3D Printing\0. Dataset Project 2022\20%\5.I_FDM(2015)').glob("**/*.png"):
    try:
        imageFile.append(imgfile)
    except Exception as e:
        print(imgfile, "fail", e)

print(len(jsonFile), len(imageFile))

for i in range(len(jsonFile)):
    if(str(jsonFile[i]) == (str(imageFile[i]))+".json"):
        match +=1

print("Total Match: ", match)