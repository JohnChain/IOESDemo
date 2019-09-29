# -*- coding: utf-8 -*-
#!/usr/local/bin/python
import sys
import json
import IOESDemo
from utils import *
from ImageDataManager import ImageDataManager
from BGWorker import BGWorker
from IOESBGWorker import IOESBGWorker
from IASBGWorker import IASBGWorker
from MarkRect import MarkRectItem
from PreviewWidget import PreviewWidget

class IOESDemoApp(QMainWindow, IOESDemo.Ui_IOESDemo):
    _signal_hover = pyqtSignal(int, str, int)
    def __init__(self, parent=None):
        super(IOESDemoApp, self).__init__(parent)
        self.setupUi(self)
        self.registEvent()
        self.initStates()
        self.initValues()

    def initStates(self):
        self.statusBar().showMessage(VERSION)
        self.listImages.clear()
        self.edtImagePath.setReadOnly(True)
        self.edtURL.setText("http://192.168.1.222:9096/images/recog")
        self.combxSericeType.insertItem(0, "IOES")
        self.combxSericeType.insertItem(1, "IAS")
        self.combxSericeType.setCurrentIndex (0)

    def initValues(self):
        # 内部维护了一个字典，该字典中保存了结构化服务返回的所有图片的解析结果，
        # key为图片路径，value为图片中的所有目标信息(一个由多个字典组成的list，每个字典为一个目标)
        self.dataManager = ImageDataManager()
        self.previewWidget = None
        self.cbxDict = {
            JVIA_HUMAN: self.cbxPerson,
            JVIA_VEHICLE: self.cbxCar,
            JVIA_BIKE: self.cbxBike,
            FaceBoundingBox: self.cbxFace,
            HeadBoundingBox: self.cbxHead,
            UpperBoundingBox: self.cbxBody,
            LowerBoundingBox: self.cbxBody,
            CommonBox: self.cbxHead
        }
        # 保存当前打开图片中的所有类型目标的矩形框，用于后续checkbox中显示/不限时特定类型目标
        self.rectDict = {
            JVIA_HUMAN: [],
            JVIA_VEHICLE: [],
            JVIA_BIKE: [],
            FaceBoundingBox: [],
            HeadBoundingBox: [],
            UpperBoundingBox: [],
            LowerBoundingBox: [],
            CommonBox: []
        }

    def registEvent(self):
        self._signal_hover.connect(self.flushPreviewWidget)
        self.btnStartTask.clicked.connect(self.startTask)
        self.btnStopTask.clicked.connect(self.stopTask)
        self.btnDumpResult.clicked.connect(self.dumpResult)
        self.btnBraws.clicked.connect(self.brawsImage)
        self.listImages.itemClicked.connect(self.previewImage)
        self.btnMarkRect.clicked.connect(self.markRect)
        self.combxSericeType.currentIndexChanged.connect(self.updateServiceType)
        self.cbxBike.stateChanged.connect(self.rectOpsBike)
        self.cbxCar.stateChanged.connect(self.rectOpsCar)
        self.cbxPerson.stateChanged.connect(self.rectOpsPerson)
        self.cbxFace.stateChanged.connect(self.rectOpsFace)
        self.cbxBody.stateChanged.connect(self.rectOpsBody)
        self.cbxHead.stateChanged.connect(self.rectOpsHead)

    def addRect(self, scene, box, dataKey, row, index):
        rect = dict2Rect(box)
        pen = TYPE_2_PEN[dataKey]
        item = MarkRectItem(self._signal_hover, rect, dataKey, row, index)
        item.setPen(pen)
        if dataKey == JVIA_HUMAN or dataKey == JVIA_VEHICLE or dataKey == JVIA_BIKE or dataKey == CommonBox:
            item.setAcceptHoverEvents(True)
        if dataKey in self.rectDict:
            self.rectDict[dataKey].append(item)
        else:
            print("unknow dateType: %s" %dataKey)
        scene.addItem(item)
        state = True if self.cbxDict[dataKey].checkState() > 0 else False
        item.setVisible(state)

    def rectOps(self, checkState, rectList):
        targetState = True if checkState > 0 else False
        for rect in rectList:
            rect.setVisible(targetState)
    def rectOpsBike(self, checkState):
        self.rectOps(checkState, self.rectDict[JVIA_BIKE])
    def rectOpsCar(self, checkState):
        self.rectOps(checkState, self.rectDict[JVIA_VEHICLE])
    def rectOpsPerson(self, checkState):
        self.rectOps(checkState, self.rectDict[JVIA_HUMAN])
    def rectOpsFace(self, checkState):
        self.rectOps(checkState, self.rectDict[FaceBoundingBox])
    def rectOpsBody(self, checkState):
        self.rectOps(checkState, self.rectDict[UpperBoundingBox])
        self.rectOps(checkState, self.rectDict[LowerBoundingBox])
    def rectOpsHead(self, checkState):
        self.rectOps(checkState, self.rectDict[CommonBox])
        self.rectOps(checkState, self.rectDict[HeadBoundingBox])

    def clearRectDict(self):
        for key in self.rectDict.keys():
            self.rectDict[key].clear()

    def previewImage(self, item):
        self.clearRectDict()
        full_path = self.getFilePath(item.text())
        self.updateImage(full_path)
        scene = self.gvPreview.scene()
        row = "%d" %self.listImages.row(item)
        objectList = self.dataManager.get(row)
        for index in range(len(objectList)):
            objDict = objectList[index]
            meterDataDict = objDict["Metadata"]
            if UpperBoundingBox in meterDataDict:
                self.addRect(scene, meterDataDict[UpperBoundingBox], UpperBoundingBox, row, index)
            if LowerBoundingBox in meterDataDict:
                self.addRect(scene, meterDataDict[LowerBoundingBox], LowerBoundingBox, row, index)
            if HeadBoundingBox in meterDataDict:
                self.addRect(scene, meterDataDict[HeadBoundingBox], HeadBoundingBox, row, index)
            if FaceBoundingBox in meterDataDict:
                self.addRect(scene, meterDataDict[FaceBoundingBox], FaceBoundingBox, row, index)
            if "ObjectBoundingBox" in meterDataDict:
                self.addRect(scene, meterDataDict["ObjectBoundingBox"], meterDataDict["Type"], row, index)
        self.mtxtResponse.setText(json.dumps(objectList, indent=4, ensure_ascii=False)) # 格式化输出json

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

    def bgWorkderCallback(self, rspJson):
        if rspJson != "" and rspJson[:5] != "Error":
            self.dataManager.genMap(rspJson)
            self.lblParsedImageNumber.setText("%d" %self.dataManager.count())
        else:
            showMessageBox(self, "通信异常", rspJson)
            self.lblParsedImageNumber.setText("%d" %len(self.bgWorkder.taskList))
            self.stopTask()

    def onBgWorkderExit(self, msg):
        self.btnStartTask.setEnabled(True)

    def checkBGWorker(self):
        print("ComboBox change Index to %d" %self.combxSericeType.currentIndex())
        if self.combxSericeType.currentIndex() == 0:
            self.bgWorkder = IOESBGWorker()
        elif self.combxSericeType.currentIndex() == 1:
            self.bgWorkder = IASBGWorker()
        else:
            print("undefined self.combxSericeType.currentIndex: [%d]%s" %(self.combxSericeType.currentIndex(), self.combxSericeType.currentText()))
            return
        self.bgWorkder.bindSignal(SIG_TYPE_DATA, self.bgWorkderCallback)
        self.bgWorkder.bindSignal(SIG_TYPE_END, self.onBgWorkderExit)

    def updateServiceType(self, event):
        self.checkBGWorker()

    def startTask(self):
        url = self.edtURL.text()
        itemNum = self.listImages.count()
        if url == "" or itemNum == 0:
            return
        self.btnStartTask.setEnabled(False)
        self.dataManager.clearMap()     # 清掉前一批图片解析结果
        self.bgWorkder.start()      #启动后台线程
        fileList = []
        for row in range(itemNum):
            fileName = self.listImages.item(row).text()
            filePath = self.getFilePath(fileName)
            fileList.append(filePath)
        self.bgWorkder.addTask(url, fileList)

    def stopTask(self):
        self.bgWorkder.stop()
        self.btnStartTask.setEnabled(True)

    def flushPreviewWidget(self, isActive, row, index):
        if isActive == 1:
            rect = getRect(PREVIEW_WIDGET_X, PREVIEW_WIDGET_Y, PREVIEW_WIDGET_WIDTH, PREVIEW_WIDGET_HEIGHT)
            objectList = self.dataManager.get(row)
            dataDict = {}
            if len(objectList) > 0:
                dataDict = objectList[index]["Metadata"]
            if self.previewWidget == None:
                self.previewWidget = PreviewWidget(rect, row, index, dataDict, self)
        else:
            self.previewWidget.setParent(None)
            self.previewWidget = None

    def dumpResult(self):
        widthListImage = self.listImages.size().width()
        hightListImage = self.listImages.size().height()
        heightGVPreview = self.gvPreview.size().height()
        widthGVPreview = self.gvPreview.size().width()
        showMessageBox(self, "空间长宽", "widthGVPreview: %d， heightGVPreview: %d, widthListImage: %d, hightListImage: %d" %(widthGVPreview, heightGVPreview, widthListImage, hightListImage))

    def markRect(self):
        scene = self.gvPreview.scene()
        if scene != None:
            try:
                rectStr = self.edtX.text().strip().split(",")
                box = {"x": int(rectStr[0]), "y": int(rectStr[1]), "w": int(rectStr[2]), "h": int(rectStr[3])}
                self.addRect(scene, box, CommonBox, CommonBox, 0)
            except ValueError:
                showMessageBox(self, "标注异常", "请输入正确参数格式: x, y, w, h")

    def restoreState(self):
        self.lblTimeCost.setText("0")
        self.lblParsedImageNumber.setText("0")
        self.dataManager.clearMap()
        self.listImages.clear()
        if self.gvPreview.scene() != None:
            self.gvPreview.scene().clear()

        dir_path = self.edtImagePath.text()
        if dir_path != "":
            imageNames = getImageList(dir_path)
            for name in imageNames:
                item = QListWidgetItem("%s" % name)
                self.listImages.addItem(item)
            self.lblTotalImageNum.setText("%d" %len(imageNames))
        else:
            self.lblTotalImageNum.setText("0")

    def brawsImage(self):
        dir_path = getDirPath(self, "图片路径")
        if dir_path == "":
            return
        self.edtImagePath.setText(dir_path)
        self.restoreState()

def main():
    app = QApplication(sys.argv)
    form = IOESDemoApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
