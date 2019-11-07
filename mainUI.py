# -*- coding: utf-8 -*-
#!/usr/local/bin/python
import fix_qt_import_error
import sys
import json
import IOESDemo
from utils import *
from IOESDataManager import IOESDataManager
from BGWorker import BGWorker
from IOESBGWorker import IOESBGWorker
from IASBGWorker import IASBGWorker
from MarkRect import MarkRectItem
from PreviewWidget import PreviewWidget

class IOESDemoApp(QMainWindow, IOESDemo.Ui_IOESDemo):
    _signal_hover = pyqtSignal(str, str, int)
    _signal_dump = pyqtSignal(str, str)
    def __init__(self, parent=None):
        super(IOESDemoApp, self).__init__(parent)
        self.setupUi(self)
        self.registEvent()
        self.initStates()
        self.initValues()

    def initStates(self):
        self.setWindowTitle(APP_NAME + "_" + VERSION)
        self.listImages.clear()
        self.edtImagePath.setReadOnly(True)
        self.edtURL.setText(DEFAULT_SERVICE_URL)
        self.initComBx()
 
    def initComBx(self):
        self.combxSericeType.insertItem(0, PROJECT_IOES)
        self.combxSericeType.insertItem(1, PROJECT_IAS)
        self.combxSericeType.setCurrentIndex (0)

        for idx in range(len(MODEL_LIST)):
            key = MODEL_LIST[idx]
            self.combxModel.insertItem(idx, key)
        self.combxModel.setCurrentIndex(0)
        for idx in range(MAX_BUNCH_LENGTH):
            self.combxBunchSize.insertItem(idx, "%d" %(idx + 1))
        self.combxBunchSize.setCurrentIndex(MAX_BUNCH_LENGTH - 1)

    def initValues(self):
        # 内部维护了一个字典，该字典中保存了结构化服务返回的所有图片的解析结果，
        # key为图片路径，value为图片中的所有目标信息(一个由多个字典组成的list，每个字典为一个目标)
        self.scalePercentage = 1.0
        self.dataManager = IOESDataManager()
        # 存储所有image的全路径名称
        self.listImageName = []
        self.previewWidget = None
        self.cbxDict = {
            JVIA_HUMAN: self.cbxPerson,
            JVIA_VEHICLE: self.cbxCar,
            JVIA_BIKE: self.cbxBike,
            JVIA_FACE: self.cbxFace,
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
            JVIA_FACE: [],
            FaceBoundingBox: [],
            HeadBoundingBox: [],
            UpperBoundingBox: [],
            LowerBoundingBox: [],
            CommonBox: []
        }

    def registEvent(self):
        self._signal_hover.connect(self.flushPreviewWidget)
        self._signal_dump.connect(self.updateDumpProgress)
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
        self.menuConfigDumpPicture.triggered.connect(self.updateMenuDumpPicture)
        self.menuConfigSelfCheck.triggered.connect(self.updateMenuSelfCheck)
        self.combxModel.currentIndexChanged.connect(self.updateMode)
        self.combxBunchSize.currentIndexChanged.connect(self.updateBunchSize)

    def updateMenuDumpPicture(self, event):
        if self.menuConfigDumpPicture.isChecked():
            GLOBAL_FLAG_DUMP_WITH_PICTURE[0] = True
        else:
            GLOBAL_FLAG_DUMP_WITH_PICTURE[0] = False
    def updateMenuSelfCheck(self, event):
        if self.menuConfigSelfCheck.isChecked():
            GLOBAL_FLAG_SELF_CHECK[0] = True
        else:
            GLOBAL_FLAG_SELF_CHECK[0] = False

    def updateMode(self, event):
        key = self.combxModel.currentText()
        GLOBAL_MODEL[0] = MODEL_MAPPER[key]
        logger.info("current GLOBAL_MODEL: %d" %GLOBAL_MODEL[0])

    def updateBunchSize(self, event):
        key = self.combxBunchSize.currentText()
        GLOBAL_BUNCH_LENGTH[0] = int(key)
        logger.info("current GLOBAL_BUNCH_LENGTH: %d" %GLOBAL_BUNCH_LENGTH[0])

    def addRect(self, scene, box, dataKey, row, index):
        rect = dict2Rect(box, percentage=self.scalePercentage)
        pen = TYPE_2_PEN[dataKey]
        item = MarkRectItem(self._signal_hover, rect, dataKey, row, index)
        item.setPen(pen)
        if dataKey == JVIA_HUMAN or dataKey == JVIA_VEHICLE or dataKey == JVIA_BIKE or dataKey == HeadBoundingBox or dataKey == FaceBoundingBox or dataKey == CommonBox:
            item.setAcceptHoverEvents(True)
        if dataKey in self.rectDict:
            self.rectDict[dataKey].append(item)
        else:
            logger.debug("unknow dateType: %s" %dataKey)
            return
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
        self.rectOps(checkState, self.rectDict[JVIA_FACE])
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
        objectList = self.dataManager.getRow(row)
        for index in range(len(objectList)):
            meterDataDict = self.dataManager.getObjMetadata(row, index)
            if UpperBoundingBox in meterDataDict:
                self.addRect(scene, meterDataDict[UpperBoundingBox], UpperBoundingBox, row, index)
            if LowerBoundingBox in meterDataDict:
                self.addRect(scene, meterDataDict[LowerBoundingBox], LowerBoundingBox, row, index)
            if HeadBoundingBox in meterDataDict:
                self.addRect(scene, meterDataDict[HeadBoundingBox], HeadBoundingBox, row, index)
            if FaceBoundingBox in meterDataDict:
                self.addRect(scene, meterDataDict[FaceBoundingBox], FaceBoundingBox, row, index)
            if ObjectBoundingBox in meterDataDict:
                self.addRect(scene, meterDataDict[ObjectBoundingBox], meterDataDict["Type"], row, index)
        self.mtxtResponse.setText(json.dumps(objectList, indent=4, ensure_ascii=False)) # 格式化输出json

    def getFilePath(self, fileName):
        return self.edtImagePath.text() + "/" + fileName
    # override parent function
    def resizeEvent(self, e):
        item = self.listImages.currentItem()
        if item != None:
            self.previewImage(item)
        QWidget.resizeEvent(self, e)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, '警告', '退出后当前任务将停止,\n你确认要退出吗？', QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.stopTask()
            event.accept()
        else:
            event.ignore()

    def updateImage(self, image_path):
        pixmap = QPixmap(image_path)
        pixmapHight = pixmap.height()
        pixmapWidth = pixmap.width()
        scalePixmap = float(pixmapWidth) / float(pixmapHight)
        previewHight = self.gvPreview.height()
        previewWidth = self.gvPreview.width()
        scalePreview = float(previewWidth) / float(previewHight)
        newWidth = 0.0
        newHidth = 0.0
        if scalePixmap > scalePreview:
            newWidth = previewWidth
            newHidth = newWidth / scalePixmap
        else:
            newHidth = previewHight
            newWidth = newHidth * scalePixmap
        self.scalePercentage = float(newWidth) / float(pixmapWidth)
        scaledPixmap = pixmap.scaled(newWidth, newHidth)
        self.pixmap_item = QGraphicsPixmapItem(scaledPixmap)
        self.scene = QGraphicsScene(self.gvPreview)
        #self.scene.setSceneRect(0, 0, 300, 300)
        self.scene.addItem(self.pixmap_item)
        self.gvPreview.setScene(self.scene)

    def updateListWidgetItems(self, id2brush):
        for imageId in id2brush:
            brush = id2brush[imageId]
            try:
                row = int(imageId)
                item = self.listImages.item(row)
                item.setBackground(brush)
            except Exception as e:
                showMessageBox(self, "更新图片列别异常", str(e))

    def bgWorkderCallback(self, rspJson):
        if GLOBAL_FLAG_SELF_CHECK[0]:
            return
        if rspJson != "" and rspJson[:5] != "Error":
            ret = self.dataManager.genMap(rspJson)
            if ret[JSON_PARSE_RET_CODE] == JSON_PARSE_RET_OK:
                self.updateListWidgetItems(ret[JSON_PARSE_RET_PAYLOAD])
                self.lblParsedImageNumber.setText("%d" %self.dataManager.count())
            else:
                showMessageBox(self, "处理回复消息异常", ret[JSON_PARSE_RET_REASON])
        else:
            self.stopTask()
            showMessageBox(self, "通信异常", rspJson)
            self.lblParsedImageNumber.setText("%d" %len(self.bgWorkder.taskList))

    def onBgWorkderExit(self, msg):
        self.enableWidget(True)
        self.groupFailPics()

    def checkBGWorker(self):
        if self.combxSericeType.currentIndex() == 0:
            self.bgWorkder = IOESBGWorker()
        elif self.combxSericeType.currentIndex() == 1:
            self.bgWorkder = IASBGWorker()
        self.bgWorkder.bindSignal(SIG_TYPE_DATA, self.bgWorkderCallback)
        self.bgWorkder.bindSignal(SIG_TYPE_END, self.onBgWorkderExit)

    def updateServiceType(self, event):
        self.checkBGWorker()

    def enableWidget(self, flag):
        self.btnStartTask.setEnabled(flag)
        self.btnBraws.setEnabled(flag)
        self.btnMarkRect.setEnabled(flag)
        self.btnDumpResult.setEnabled(flag)
        self.combxModel.setEnabled(flag)
        self.combxSericeType.setEnabled(flag)
        self.combxBunchSize.setEnabled(flag)

    def startTask(self):
        url = self.edtURL.text()
        if url == "" or self.listImages.count() == 0:
            return
        self.enableWidget(False)
        self.restoreState()

        self.bgWorkder.start()      #启动后台线程
        self.bgWorkder.addTask(url, self.listImageName)

    def stopTask(self):
        self.dataManager.stopDump()
        self.bgWorkder.stop()
        self.enableWidget(True)

    def groupFailPics(self):
        lenList = self.listImages.count()
        for row in range(lenList):
            item = self.listImages.item(row)
            if item.background() != BRUSH_Y:
                item.setHidden(True)
                item2 = item.clone()
                item2.setBackground(BRUSH_N)
                self.listImages.addItem(item2)
                logger.warning("Hide pic at row: %d/%d, named: %s" %(row, lenList, item.text()))

    def removePreviewWidget(self):
        if self.previewWidget != None:
            self.previewWidget.setParent(None)
            self.previewWidget = None
    def flushPreviewWidget(self, SIG_TYPE, row, index):
        if SIG_TYPE == SIG_TYPE_ENTER:
            rect = getRect(PREVIEW_WIDGET_X, PREVIEW_WIDGET_Y, PREVIEW_WIDGET_WIDTH, PREVIEW_WIDGET_HEIGHT)
            dataDict = self.dataManager.getObjMetadata(row, index)
            if self.previewWidget == None:
                self.previewWidget = PreviewWidget(rect, row, index, dataDict, self)
        elif SIG_TYPE == SIG_TYPE_LEAVE:
            self.removePreviewWidget()
        elif SIG_TYPE == SIG_TYPE_DOUBLE_CLICK:
            dataDict = self.dataManager.getObj(row, index)
            self.mtxtParseResult.setText(json.dumps(dataDict, indent=4, ensure_ascii=False)) # 格式化输出json
        else:
            logger.error("unknow SIG_TYPE: ", SIG_TYPE)

    def updateDumpProgress(self, SIG_TYPE, state):
        if SIG_TYPE == SIG_DUMP_PROCESSING:
            self.lblTimeCost.setText(state)
        elif SIG_TYPE == SIG_DUMP_FINISHED:
            showMessageBox(self, MESSAGE_BOX_DUMP_TITLE, "导出结束：%s" %state)
            self.enableWidget(True)
        else:
            logger.error("updateDumpProgress unknow SIG_TYPE: ", SIG_TYPE)

    def dumpResult(self):
        if self.dataManager.count() > 0:
            flter = "WindowsOffice(*.xls *.xlsx)"
            outFilePath = getFilePath(self, filter= flter, caption="请选择导出文件")
            if outFilePath[0] != "":
                self.lblTimeCost.setText("0")
                self.enableWidget(False)
                rst = self.dataManager.startDump(self._signal_dump, self.listImageName, outFilePath[0])
        else:
            showMessageBox(self, MESSAGE_BOX_DUMP_TITLE, "暂无有效的数据待导出")

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
        self.listImageName.clear()
        if self.gvPreview.scene() != None:
            self.gvPreview.scene().clear()

        dir_path = self.edtImagePath.text()
        if dir_path != "":
            imageNames = getImageList(dir_path)
            for name in imageNames:
                item = QListWidgetItem("%s" % name)
                self.listImages.addItem(item)
                self.listImageName.append(self.getFilePath(name))
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
