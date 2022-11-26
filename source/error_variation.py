from pathlib import Path
import os, json

errorType =[]

for jsonfile in Path(r'D:\3D Printing\0. Dataset Project 2022\23%').glob("**/*.json"):
    try:
        data = json.load(open(jsonfile))
        error = data['annotation_info']['Print error code']
        if not error in errorType:
            errorType.append(error)
        # print(jsonfile, "success")
    except Exception as e:
        print(jsonfile, "fail", e)

print(errorType)