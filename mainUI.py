# -*- coding: utf-8 -*-
#!/usr/local/bin/python
import sys
import json
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ImageDataManager import ImageDataManager
from utils import *
from BGWorker import BGWorker
import IOESDemo
from MarkRect import MarkRectItem
from PreviewWidget import PreviewWidget

class IOESDemoApp(QMainWindow, IOESDemo.Ui_IOESDemo):
    def __init__(self, parent=None):
        super(IOESDemoApp, self).__init__(parent)
        self.dataManager = ImageDataManager()
        self.bgWorkder = BGWorker()

        self.setupUi(self)
        self.statusBar().showMessage(VERSION)
        self.registEvent()
        self.initStates()

    def initStates(self):
        self.listImages.clear()
        self.edtImagePath.setReadOnly(True)
        self.edtURL.setText("http://192.168.1.222:11500/images/recog")
        self.bgWorkder.bindSignal(self.bgWorkderCallback)

    def registEvent(self):
       self.btnStartTask.clicked.connect(self.startTask)
       self.btnStopTask.clicked.connect(self.stopTask)
       self.btnDumpResult.clicked.connect(self.dumpResult)
       self.btnBraws.clicked.connect(self.brawsImage)
       self.listImages.itemClicked.connect(self.previewImage)
       self.btnMarkRect.clicked.connect(self.markRect)

    def addRect(self, scene, box, dataKey):
        rect = dict2Rect(box)
        pen = TYPE_2_PEN[dataKey]
        item = MarkRectItem(rect, dataKey)
        item.setPen(pen)
        if dataKey == JVIA_HUMAN or dataKey == JVIA_VEHICLE or dataKey == JVIA_BIKE:
            item.setAcceptHoverEvents(True)
        scene.addItem(item)

    def previewImage(self, item):
        scene = self.gvPreview.scene()
        if scene == None:
            return
        full_path = self.getFilePath(item.text())
        self.updateImage(full_path)
        row = "%d" %self.listImages.row(item)
        objectList = self.dataManager.get(row)
        for objDict in objectList:
            meterDataDict = objDict["Metadata"]
            self.addRect(scene, meterDataDict["ObjectBoundingBox"], meterDataDict["Type"])
            if UpperBoundingBox in meterDataDict:
                self.addRect(scene, meterDataDict[UpperBoundingBox], UpperBoundingBox)
            if LowerBoundingBox in meterDataDict:
                self.addRect(scene, meterDataDict[LowerBoundingBox], LowerBoundingBox)
            if HeadBoundingBox in meterDataDict:
                self.addRect(scene, meterDataDict[HeadBoundingBox], HeadBoundingBox)
            if FaceBoundingBox in meterDataDict:
                self.addRect(scene, meterDataDict[FaceBoundingBox], FaceBoundingBox)
        self.mtxtResponse.setText(json.dumps(objectList, indent=4)) # 格式化输出json

    def getFilePath(self, fileName):
        return self.edtImagePath.text() + "/" + fileName

    def updateImage(self, image_path):
        pixmap = QPixmap(image_path)
        #scaledPixmap = pixmap.scaled(500, 1000)
        self.pixmap_item = QGraphicsPixmapItem(pixmap)
        self.scene = QGraphicsScene(self.gvPreview)
        #self.scene.setSceneRect(0, 0, 300, 300)
        self.scene.addItem(self.pixmap_item)
        self.gvPreview.setScene(self.scene)

    def postJson(self, url, output, imageList):
        self.btnStartTask.setEnabled(False)
        mdict = {"Output": output, "ImageList": imageList}
        task = {"url": url, "body": mdict}
        self.bgWorkder.addTask(task)

    def bgWorkderCallback(self, rspJson):
        print("here bgWorkderCallback")
        if rspJson != "" and rspJson[:5] != "Error":
            self.dataManager.genMap(rspJson)
            self.lblParsedImageNumber.setText("%d" %self.dataManager.count())
        else:
            showMessageBox(self, "Task Error", rspJson)
            self.lblParsedImageNumber.setText("%d" %len(self.bgWorkder.taskList))
            self.stopTask()

    def startTask(self):
        url = self.edtURL.text()
        itemNum = self.listImages.count()
        if url == "" or itemNum == 0:
            return
        self.dataManager.clearMap() # 清掉前一批图片解析结果

        self.bgWorkder.start()

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
        if len(imageList) > 0:  #最后一组不满8张
            self.postJson(url, output, imageList)
        return

    def stopTask(self):
        self.bgWorkder.stop()
        self.btnStartTask.setEnabled(True)
        #showMessageBox(self, "startTask", "height: %d, width: %d" %(self.gvPreview.size().height(), self.gvPreview.size().width()))

    def dumpResult(self):
        ex = PreviewWidget(self)
        return

    def markRect(self):
        scene = self.gvPreview.scene()
        if scene != None:
            try:
                rectStr = self.edtX.text().strip().split(",")
                x = int(rectStr[0])
                y = int(rectStr[1])
                w = int(rectStr[2])
                h = int(rectStr[3])
                box = {"x": x, "y": y, "w": w, "h": h}
                self.addRect(scene, box, CommonBox)
            except ValueError:
                return
        return
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
