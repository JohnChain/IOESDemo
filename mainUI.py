# -*- coding: utf-8 -*-
#!/usr/local/bin/python
import sys
import json
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ImageDataManager import ImageDataManager
from utils import *
from HttpOps import HttpOps
import IOESDemo

class IOESDemoApp(QMainWindow, IOESDemo.Ui_IOESDemo):
    def __init__(self, parent=None):
        super(IOESDemoApp, self).__init__(parent)
        self.setupUi(self)
        self.statusBar().showMessage(VERSION)
        self.registEvent()
        self.initStates()
        self.httpOps = HttpOps()
        self.dataManager = ImageDataManager()

    def initStates(self):
        self.listImages.clear()
        self.edtImagePath.setReadOnly(True)
        self.edtURL.setText("http://192.168.1.222:11500/images/recog")

    def registEvent(self):
       self.btnStartTask.clicked.connect(self.startTask)
       self.btnStopTask.clicked.connect(self.stopTask)
       self.btnDumpResult.clicked.connect(self.dumpResult)
       self.btnBraws.clicked.connect(self.brawsImage)
       self.listImages.itemClicked.connect(self.previewImage)

    def previewImage(self, item):
        full_path = self.getFilePath(item.text())
        self.updateImage(full_path)
        row = "%d" %self.listImages.row(item)
        objectList = self.dataManager.get(row)
        for objDict in objectList:
            meterDataDict = objDict["Metadata"]
            objType = meterDataDict["Type"]
            box = meterDataDict["ObjectBoundingBox"]
            rect = dict2Rect(box)
            scene = self.gvPreview.scene()
            if scene != None:
                scene.addRect(rect, TYPE_2_PEN[objType])
                if "FaceBoundingBox" in meterDataDict:
                    box = meterDataDict["FaceBoundingBox"]
                    rect = dict2Rect(box)
                    scene.addRect(rect, PEN_FACE)
                if "HeadBoundingBox" in meterDataDict:
                    box = meterDataDict["HeadBoundingBox"]
                    rect = dict2Rect(box)
                    scene.addRect(rect, PEN_HEAD)
                if "UpperBoundingBox" in meterDataDict:
                    box = meterDataDict["UpperBoundingBox"]
                    rect = dict2Rect(box)
                    scene.addRect(rect, PEN_BODY)
                if "LowerBoundingBox" in meterDataDict:
                    box = meterDataDict["LowerBoundingBox"]
                    rect = dict2Rect(box)
                    scene.addRect(rect, PEN_BODY)
        self.mtxtResponse.setText(json.dumps(objectList))

    def getFilePath(self, fileName):
        return self.edtImagePath.text() + "/" + fileName

    def updateImage(self, image_path):
        pixmap = QPixmap(image_path)
        #scaledPixmap = pixmap.scaled(500, 1000)
        #self.pixmap_item = QGraphicsPixmapItem(scaledPixmap)
        self.pixmap_item = QGraphicsPixmapItem(pixmap)
        self.scene = QGraphicsScene(self.gvPreview)
        #self.scene.setSceneRect(0, 0, 300, 300)
        self.scene.addItem(self.pixmap_item)
        self.gvPreview.setScene(self.scene)

    def postJson(self, url, output, imageList):
        mdir = {"Output": output, "ImageList": imageList}
        rspjson = self.httpOps.post(url, mdir)
        print(rspjson)
        self.dataManager.genMap(rspjson)
        self.lblParsedImageNumber.setText("%d" %self.dataManager.count())

    def startTask(self):
        url = self.edtURL.text()
        itemNum = self.listImages.count()
        if url == "" or itemNum == 0:
            return
        self.dataManager.clearMap()
        output = {"Face": 1, "SubClass": 1}
        tempCount = 0 # 辅助计算8张图片一组
        imageList = []
        for row in range(itemNum):
            tempCount = tempCount + 1
            if tempCount > 8:
                self.postJson(url, output, imageList)
                tempCount = 0
                imageList = []
            item = self.listImages.item(row)
            fileName = item.text()
            filePath = self.getFilePath(fileName)
            imageCell = {"ImageID": "%d" %row}
            imageCell["Data"] = fileBase64(filePath)
            imageList.append(imageCell)
        if len(imageList) > 0:
            self.postJson(url, output, imageList)
        return

    def stopTask(self):
        showMessageBox(self, "startTask", "height: %d, width: %d" %(self.gvPreview.size().height(), self.gvPreview.size().width()))

    def dumpResult(self):
        scene = self.gvPreview.scene()
        if scene != None:
            scene.addRect(getRect(124, 34, 433, 344), PEN_HEAD)
            scene.addRect(getRect(217, 144, 260, 191), PEN_FACE)
            scene.addRect(getRect(14, 30, 571, 612), PEN_PERSON)
            scene.addRect(getRect(14, 30, 0, 0), PEN_PERSON)
            scene.addRect(getRect(14, 30, 0, 0), PEN_PERSON)

    def brawsImage(self):
        dir_path = getDirPath(self, "图片路径")
        if dir_path == "":
            return
        self.edtImagePath.setText(dir_path)
        self.listImages.clear()
        imageNames = getImageList(dir_path)
        for name in imageNames:
            item = QListWidgetItem("%s" % name)
            self.listImages.addItem(item)
        self.lblTotalImageNum.setText("%d" %len(imageNames))

def main():
    app = QApplication(sys.argv)
    form = IOESDemoApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
