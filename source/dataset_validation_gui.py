# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\dataset.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from pathlib import Path
import os, json
import random
import cv2
from PIL import Image as im
import csv

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        x = 0
        Dialog.setObjectName("NSL - Dataset Validation Software (by: Adi Paramartha)")
        Dialog.resize(874, 652)
        Dialog.setWindowIcon(QtGui.QIcon(r'D:\3D Printing\0. Dataset Project 2022\KIT.jpg'))

        self.counter = -1
        self.jsonFileList = []
        self.imageFileList = []
        self.data = []

        self.label_folder_path = QtWidgets.QLabel(Dialog)
        self.label_folder_path.setGeometry(QtCore.QRect(110, 26, 481, 21))
        self.label_folder_path.setObjectName("label_folder_path")

        self.button_select_folder = QtWidgets.QPushButton(Dialog)
        self.button_select_folder.setGeometry(QtCore.QRect(20, 20, 81, 31))
        self.button_select_folder.setAutoFillBackground(True)
        self.button_select_folder.setStyleSheet("")
        self.button_select_folder.setObjectName("button_select_folder")
        self.button_select_folder.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.label_image_name = QtWidgets.QLabel(Dialog)
        self.label_image_name.setGeometry(QtCore.QRect(110, 60, 481, 21))
        self.label_image_name.setObjectName("label_image_name")
        
        self.label_json_name = QtWidgets.QLabel(Dialog)
        self.label_json_name.setGeometry(QtCore.QRect(110, 75, 481, 21))
        self.label_json_name.setObjectName("label_json_name")

        self.label = QtWidgets.QPushButton(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 65, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label") 

        self.NSL_img = QtWidgets.QLabel(Dialog)
        self.NSL_img.setGeometry(QtCore.QRect(675, 40, 175, 31))
        self.NSL_img.setScaledContents(True)
        self.NSL_img.setPixmap(QtGui.QPixmap(r'D:\3D Printing\0. Dataset Project 2022\logo.png'))
        self.NSL_img.setObjectName("NSL_img")     

        self.frame = QtWidgets.QLabel(Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 120, 721, 510))
        self.frame.setPixmap(QtGui.QPixmap(r'D:\3D Printing\0. Dataset Project 2022\background.JPG'))   
        self.frame.setObjectName("frame")
        self.frame.setScaledContents(True)
        self.frame.setStyleSheet("border: 2px solid black")

        # Right-side Interaction Menu

        self.labelNumber = QtWidgets.QLabel(Dialog)
        self.labelNumber.setGeometry(QtCore.QRect(760, 110, 101, 31))
        self.labelNumber.setObjectName("labelNumber")
        self.labelNumber.setAlignment(QtCore.Qt.AlignCenter)
                
        self.labelStatus = QtWidgets.QLabel(Dialog)
        self.labelStatus.setGeometry(QtCore.QRect(760, 140, 101, 31))
        self.labelStatus.setObjectName("labelStatus")
        self.labelStatus.setStyleSheet("font-weight: bold; color: black")
        self.labelStatus.setAlignment(QtCore.Qt.AlignCenter)

        self.valueStatus = QtWidgets.QLabel(Dialog)
        self.valueStatus.setGeometry(QtCore.QRect(760, 165, 101, 31))
        self.valueStatus.setObjectName("valueStatus")    
        self.valueStatus.setAlignment(QtCore.Qt.AlignCenter)

        self.toggle_annotation = QtWidgets.QPushButton("Toggle",Dialog)
        self.toggle_annotation.setCheckable(True)
        self.toggle_annotation.setGeometry(QtCore.QRect(760, 200, 101, 62))
        self.toggle_annotation.setObjectName("toggle_annotation")
        self.toggle_annotation.setStyleSheet("background-color: rgba(0,0, 255, 50);  border: 2px solid blue;")
        self.toggle_annotation.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toggle_annotation.clicked.connect(self.changeAnotate)
        self.toggle_annotation.setDisabled(True)

        self.button_blowout = QtWidgets.QPushButton(Dialog)
        self.button_blowout.setGeometry(QtCore.QRect(760, 280, 101, 31))
        self.button_blowout.setAutoFillBackground(True)
        self.button_blowout.setObjectName("button_blowout")
        self.button_blowout.setStyleSheet("background-color: rgba(255,0, 0, 20);  border: 2px solid red;")
        self.button_blowout.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.button_stringing = QtWidgets.QPushButton(Dialog)
        self.button_stringing.setGeometry(QtCore.QRect(760, 320, 101, 31))
        self.button_stringing.setAutoFillBackground(True)
        self.button_stringing.setObjectName("button_stringing")
        self.button_stringing.setStyleSheet("background-color: rgba(255,0, 0, 20);  border: 2px solid red;")
        self.button_stringing.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        self.button_lines = QtWidgets.QPushButton(Dialog)
        self.button_lines.setGeometry(QtCore.QRect(760, 360, 101, 31))
        self.button_lines.setObjectName("button_lines")
        self.button_lines.setStyleSheet("background-color: rgba(255,0, 0, 20);  border: 2px solid red;")  
        self.button_lines.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.button_etc = QtWidgets.QPushButton(Dialog)
        self.button_etc.setGeometry(QtCore.QRect(760, 400, 101, 31))
        self.button_etc.setObjectName("button_etc")
        self.button_etc.setStyleSheet("background-color: rgba(255,0, 0, 20);  border: 2px solid red;")
        self.button_etc.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.button_warping = QtWidgets.QPushButton(Dialog)
        self.button_warping.setGeometry(QtCore.QRect(760, 440, 101, 31))
        self.button_warping.setObjectName("button_warping")
        self.button_warping.setStyleSheet("background-color: rgba(255,0, 0, 20);  border: 2px solid red;")
        self.button_warping.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))     

        self.button_gaps = QtWidgets.QPushButton(Dialog)
        self.button_gaps.setGeometry(QtCore.QRect(760, 480, 101, 31))
        self.button_gaps.setObjectName("button_gaps")
        self.button_gaps.setStyleSheet("background-color: rgba(255,0, 0, 20);  border: 2px solid red;")
        self.button_gaps.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.button_separation = QtWidgets.QPushButton(Dialog)
        self.button_separation.setGeometry(QtCore.QRect(760, 520, 101, 31))
        self.button_separation.setObjectName("button_separation")
        self.button_separation.setStyleSheet("background-color: rgba(255,0, 0, 20);  border: 2px solid red;")
        self.button_separation.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.button_normal = QtWidgets.QPushButton(Dialog)
        self.button_normal.setGeometry(QtCore.QRect(760, 570, 101, 31))
        self.button_normal.setObjectName("button_normal")
        self.button_normal.setStyleSheet("background-color: rgba(0, 255, 0, 20); border: 2px solid green;")
        self.button_normal.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.button_revert = QtWidgets.QPushButton(Dialog)
        self.button_revert.setGeometry(QtCore.QRect(760, 610, 101, 20))
        self.button_revert.setObjectName("button_revert")
        self.button_revert.setStyleSheet("background-color: rgba(255,255,0,100); border: 2px solid rgb(246,190,0);")
        self.button_revert.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_revert.clicked.connect(self.revert)           

        self.button_select_folder.clicked.connect(self.selectFolder)

        self.button_normal.clicked.connect(self.clickNormal)
        self.button_gaps.clicked.connect(self.clickGaps)
        self.button_blowout.clicked.connect(self.clickBlowout)
        self.button_stringing.clicked.connect(self.clickStringing)
        self.button_lines.clicked.connect(self.clickLinesofPrint)
        self.button_warping.clicked.connect(self.clickWarping)
        self.button_separation.clicked.connect(self.clickSeparation)
        self.button_etc.clicked.connect(self.clickEtc)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def changeAnotate(self):
        if self.toggle_annotation.isChecked():
            self.anotate_status = 1
            self.toggle_annotation.setText("Wrong Annotation")
            self.toggle_annotation.setStyleSheet("background-color: rgba(255,0, 0, 50);  border: 2px solid blue;")
        else:
            self.anotate_status = 0
            self.toggle_annotation.setText("Correct Annotation")
            self.toggle_annotation.setStyleSheet("background-color: rgba(0,0, 255, 50);  border: 2px solid blue;")

    def removeCSV(self):
        with open(self.filename, 'r+') as fp:
            lines = fp.readlines()
            fp.seek(0)
            fp.truncate()
            fp.writelines(lines[:-1])
            fp.close()

    def writeCSV(self):
        self.data.append(self.anotate_status)
        if self.data[3] == self.data[8]:
            self.data.append(1)
        else:
            self.data.append(0)
        with open(self.filename, 'a', newline="") as file:
            csvwriter = csv.writer(file) 
            csvwriter.writerow(self.data)

    def clickNormal(self):
        if len(self.imageFileList) == 0:
            self.alert_box()
            return        
        self.data.append("-")
        self.writeCSV()
        self.checkAnotation()

    def clickBlowout(self):
        if len(self.imageFileList) == 0:
            self.alert_box()
            return
        self.data.append("Blow out")
        self.writeCSV()
        self.checkAnotation()
    
    def clickStringing(self):
        if len(self.imageFileList) == 0:
            self.alert_box()
            return
        self.data.append("Stringing")
        self.writeCSV()
        self.checkAnotation()

    def clickLinesofPrint(self):
        if len(self.imageFileList) == 0:
            self.alert_box()
            return
        self.data.append("Lines of Print")
        self.writeCSV()
        self.checkAnotation()

    def clickGaps(self):
        if len(self.imageFileList) == 0:
            self.alert_box()
            return
        self.data.append("Gaps")
        self.writeCSV()
        self.checkAnotation()

    def clickSeparation(self):
        if len(self.imageFileList) == 0:
            self.alert_box()
            return
        self.data.append("Separation")
        self.writeCSV()
        self.checkAnotation()    

    def clickWarping(self):
        if len(self.imageFileList) == 0:
            self.alert_box()
            return
        self.data.append("Warping")
        self.writeCSV()
        self.checkAnotation()

    def clickEtc(self):
        if len(self.imageFileList) == 0:
            self.alert_box()
            return
        self.data.append("Etc_Print Error")
        self.writeCSV()
        self.checkAnotation()

    def resetstyle(self):
        self.button_warping.setStyleSheet("background-color: rgba(255, 0, 0, 20); border: 2px solid red;")
        self.button_lines.setStyleSheet("background-color: rgba(255, 0, 0, 20); border: 2px solid red;")
        self.button_gaps.setStyleSheet("background-color: rgba(255, 0, 0, 20); border: 2px solid red;")
        self.button_separation.setStyleSheet("background-color: rgba(255, 0, 0, 20); border: 2px solid red;")
        self.button_stringing.setStyleSheet("background-color: rgba(255, 0, 0, 20); border: 2px solid red;")
        self.button_blowout.setStyleSheet("background-color: rgba(255, 0, 0, 20); border: 2px solid red;")
        self.button_etc.setStyleSheet("background-color: rgba(255, 0, 0, 20); border: 2px solid red;")
        self.button_normal.setStyleSheet("background-color: rgba(0, 255, 0, 20); border: 2px solid green;")

    def revert(self):
        self.button_normal.setDisabled(False)
        self.button_stringing.setDisabled(False)
        self.button_etc.setDisabled(False)
        self.button_lines.setDisabled(False)
        self.button_warping.setDisabled(False)
        self.button_blowout.setDisabled(False)
        self.toggle_annotation.setDisabled(False)
        self.button_separation.setDisabled(False)
        self.button_gaps.setDisabled(False)
        self.rerun=False
        self.checkAnotation(False)

    def alert_box(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Please Load the File")
        msg.setWindowTitle("Information")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        retval = msg.exec_()

    def checkAnotation(self, param=True):
        if len(self.imageFileList) == 0:
            self.alert_box()
            return

        self.data = []
        self.anotate_status = '-'
        if param == False:
            if self.counter != 0:
                self.counter =  self.counter - 1
                self.removeCSV()
        else:
            self.counter =  self.counter + 1
        if self.counter != len(self.jsonFileList):
            self.labelNumber.setText(str(self.counter + 1)+"/"+str(len(self.jsonFileList)))
            self.data.append(self.counter)
            self.label_image_name.setText(str(self.imageFileList[self.counter]))
            self.label_json_name.setText(str(self.jsonFileList[self.counter]))

            self.data.append(str(self.imageFileList[self.counter]))
            self.data.append(str(self.jsonFileList[self.counter]))

            f = open(self.jsonFileList[self.counter])
            data = json.load(f)
            annot_x = data['annotation_info']['Annotations[]_x']
            if(annot_x == '-'):
                self.resetstyle()
                self.data.extend(['-', '-', '-', '-', '-'])
                self.frame.setPixmap(QtGui.QPixmap(str(Path(self.imageFileList[self.counter]))))
                self.valueStatus.setText("No Error")
                self.valueStatus.setStyleSheet("font-weight: bold; color: black")
                self.button_normal.setStyleSheet("font-weight: bold; background-color: rgba(0, 255, 0, 20); border: 2px solid green;")
                
            else:
                annot_y = data['annotation_info']['Annotations[]_y']
                annot_width = int(float(data['annotation_info']['Annotations[]_width']))
                annot_height = int(float(data['annotation_info']['Annotations[]_height']))
                error_code = data['annotation_info']['Print error code']
                self.data.append(error_code)

                self.resetstyle()

                if error_code == "Warping":
                    self.button_warping.setStyleSheet("font-weight: bold; background-color: rgba(255, 0, 0, 30); border: 2px solid red;")
                elif error_code == "Lines of Print":
                    self.button_lines.setStyleSheet("font-weight: bold; background-color: rgba(255, 0, 0, 30); border: 2px solid red;")
                elif error_code == "Gaps":
                    self.button_gaps.setStyleSheet("font-weight: bold; background-color: rgba(255, 0, 0, 30); border: 2px solid red;")
                elif error_code == "Separation":
                    self.button_separation.setStyleSheet("font-weight: bold; background-color: rgba(255, 0, 0, 30); border: 2px solid red;")
                elif error_code == "Stringing":
                    self.button_stringing.setStyleSheet("font-weight: bold; background-color: rgba(255, 0, 0, 30); border: 2px solid red;")
                elif error_code == "Blow out":
                    self.button_blowout.setStyleSheet("font-weight: bold; background-color: rgba(255, 0, 0, 30); border: 2px solid red;")
                elif error_code == "Etc_Print Error":
                    self.button_etc.setStyleSheet("font-weight: bold; background-color: rgba(255, 0, 0, 30); border: 2px solid red;")
                
                f.close()        
                annot_x = annot_x[1:-1]
                annot_x = annot_x.split(', ')
                annot_y = annot_y[1:-1]
                annot_y = annot_y.split(', ')

                self.data.append(str(int(float(annot_x[0]))))
                self.data.append(str(int(float(annot_x[1]))))
                self.data.append(str(int(float(annot_y[0]))))
                self.data.append(str(int(float(annot_y[1]))))

                self.addAnotateandNext(annot_x, annot_y, annot_width, annot_height, error_code)        

        else:
            self.show_final_box()

    def addAnotateandNext(self, annot_x, annot_y, annot_width, annot_height, error_code):
        img = cv2.imread(str(Path(self.imageFileList[self.counter])))
        cv2.rectangle(img, ( int(float(annot_x[0])), int(float(annot_y[0])) ), ( int(float(annot_x[1])), int(float(annot_y[1])) ), self.random_color(), 2)
        annotatedImg = im.fromarray(img)
        annotatedImg.save('tmp.png',subsampling=0, quality=0)
        self.frame.setPixmap(QtGui.QPixmap('tmp.png'))
        self.valueStatus.setText(error_code)
        self.changeAnotate()
        self.valueStatus.setStyleSheet("font-weight: bold; color: red")      
        
    def random_color(self):
        rgbl=[255,0,0]
        random.shuffle(rgbl)
        return tuple(rgbl)

    def selectFolder(self):
        self.jsonFileList = []
        self.imageFileList = []
        fpath = QtWidgets.QFileDialog.getExistingDirectory(None, 'Select a directory')
        if fpath:
            self.label_folder_path.setText(fpath)
            for jsonfile in Path(fpath).glob("**/*.json"):
                try:
                    self.jsonFileList.append(jsonfile)                     
                except Exception as e:
                    print(jsonfile, "fail", e)

            for imagefile in Path(fpath).glob("**/*.png"):
                try:
                    self.imageFileList.append(imagefile)                     
                except Exception as e:
                    print(imagefile, "fail", e)
        print(self.imageFileList)

        self.filename = str(fpath).split('/')[-1] + ".csv"
        with open(self.filename, 'w', newline="") as file:
            csvwriter = csv.writer(file) 
            csvwriter.writerow(['number', 'filename_json', 'filename_img', 'init_status', 'annotation_x_start', 'annotation_x_stop','annotation_y_start', 'annotation_y_stop', 
            'observed_status', 'observed_annotation','same_result'])

        self.show_message_box()     

    def show_final_box(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("All File Loaded. Would you like to Import new Folder?")
        msg.setWindowTitle("Information")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        returnValue = msg.exec()
        if returnValue == QtWidgets.QMessageBox.Ok:
            self.frame.setPixmap(QtGui.QPixmap(r'D:\3D Printing\0. Dataset Project 2022\background.JPG'))
            self.labelNumber.setText("-/-")
            self.label_folder_path.setText("-")
            self.labelStatus.setText("-")
            self.label_image_name.setText("-")
            self.label_json_name.setText("-")
            self.counter = -1
            self.jsonFileList = []
            self.imageFileList = []
            self.data = []

        else:
            self.rerun=True
            self.button_normal.setDisabled(True)
            self.button_stringing.setDisabled(True)
            self.button_etc.setDisabled(True)
            self.button_lines.setDisabled(True)
            self.button_warping.setDisabled(True)
            self.button_blowout.setDisabled(True)
            self.toggle_annotation.setDisabled(True)
            self.button_separation.setDisabled(True)
            self.button_gaps.setDisabled(True)
            

    def show_message_box(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        if len(self.imageFileList) == 0:
            msg.setText("Import Failed, Please Select the Folder")
            msg.setWindowTitle("Information")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        else:    
            msg.setText("Import Successfull")
            msg.setWindowTitle("Information")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            self.toggle_annotation.setDisabled(False)
            self.counter = -1
            self.button_normal.setDisabled(False)
            self.button_stringing.setDisabled(False)
            self.button_etc.setDisabled(False)
            self.button_lines.setDisabled(False)
            self.button_warping.setDisabled(False)
            self.button_blowout.setDisabled(False)
            self.toggle_annotation.setDisabled(False)
            self.button_separation.setDisabled(False)
            self.button_gaps.setDisabled(False)
            self.checkAnotation()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "NSL - Dataset Validation Software (by: Adi Paramartha)"))
        self.button_normal.setText(_translate("Dialog", "Normal"))
        self.button_warping.setText(_translate("Dialog", "Warping"))
        self.button_etc.setText(_translate("Dialog", "Etc_Print Error"))
        self.button_lines.setText(_translate("Dialog", "Lines of Print"))
        self.label.setText(_translate("Dialog", "File Name"))
        self.label_image_name.setText(_translate("Dialog", "-"))
        self.labelStatus.setText(_translate("Dialog", "STATUS"))
        self.labelNumber.setText(_translate("Dialog", "-/-"))
        self.button_revert.setText(_translate("Dialog", "Revert"))
        self.valueStatus.setText(_translate("Dialog", "-"))
        self.label_json_name.setText(_translate("Dialog", "-"))
        self.button_stringing.setText(_translate("Dialog", "Stringing"))
        self.button_gaps.setText(_translate("Dialog", "Gaps"))
        self.button_separation.setText(_translate("Dialog", "Separation"))
        self.button_blowout.setText(_translate("Dialog", "Blow Out"))
        self.label_folder_path.setText(_translate("Dialog", "-"))
        self.button_select_folder.setText(_translate("Dialog", "Select Folder"))
        self.toggle_annotation.setText(_translate("Dialog", "Annotation"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
