#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from utils import *
from IOESMapping import *

class NewLabel(QLabel):
    def __init__(self, msg):
        super().__init__(msg)
        self.setStyleSheet("color:white;")

class PreviewWidget(QWidget):
    def __init__(self, rect, row, index, dataDict, parent=None):
        super().__init__(parent)
        self.row = row
        self.rect = rect
        self.index = index
        self.dataDict = dataDict
        self.initUI()

    def initUI(self):
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), PREVIEW_WIDGET_BGCOLOR)
        self.setPalette(p)

        self.hbox = QHBoxLayout()
        self.vbox = QVBoxLayout()
        self.formLayoutLeft = QFormLayout()
        self.formLayoutRight = QFormLayout()
        self.formLayouSingle = QFormLayout()

        self.hbox.setSpacing(8)
        self.vbox.setSpacing(8)
        self.hbox.setContentsMargins(QMargins(0, 0, 0, 0))
        self.vbox.setContentsMargins(QMargins(8, 8, 8, 8))
        self.formLayouSingle.setContentsMargins(QMargins(0, 8, 0, 8))

        self.hbox.addLayout(self.formLayoutLeft)
        self.hbox.addLayout(self.formLayoutRight)
        self.hbox.addStretch(1)

        self.vbox.addLayout(self.hbox)
        self.vbox.addLayout(self.formLayouSingle)
        self.vbox.addStretch(1)

        self.setObjectInfo()

        self.setLayout(self.vbox)
        self.setGeometry(self.rect)
        self.show()

    # 较短的目标属性字串，一行够显示两个
    def addShortObjectInfo(self, key, value):
        lblKey = NewLabel(key + ":")
        lblValue = NewLabel(value)
        if self.formLayoutLeft.rowCount() == self.formLayoutRight.rowCount():
            self.formLayoutLeft.addRow(lblKey, lblValue)
        else:
            self.formLayoutRight.addRow(lblKey, lblValue)

    # 较长的目标属性字串，一行只够显示一个
    def addLongObjectInfo(self, key, value):
        lblKey = NewLabel(key + ":")
        lblValue = NewLabel(value)
        self.formLayouSingle.addRow(lblKey, lblValue)

    def setObjectInfo(self):
        if ATTRIBUTE_Type in self.dataDict:
            objType = self.dataDict[ATTRIBUTE_Type]
            if objType == TYPE_CAR:
                self.setCarInfo()
            elif objType == TYPE_PERSON:
                self.setPersonInfo()
            elif objType == TYPE_FACE:
                self.setFaceInfo()
            elif objType == TYPE_BIKE:
                self.setBikeInfo()
            else:
                pass
        else:
            print("Error: cannot find object type")
            return

    def setCarMappable(self, attribute, addObjectInfo):
        if attribute in self.dataDict:
            key = IOESMapping.mapCarAttribute2Name[attribute]
            mapper = IOESMapping.mapCarMappable2Mapper[attribute]
            tempValue = self.dataDict[attribute]
            value = mapper[tempValue]
            addObjectInfo(key, value)
        else:
            print("%s not in dataDict" %keyWord)
    def setCarMirrorable(self, attribute, addObjectInfo):
        if attribute in self.dataDict:
            key = IOESMapping.mapCarAttribute2Name[attribute]
            value = self.dataDict[attribute]
            addObjectInfo(key, value)
        else:
            print("%s not in dataDict" %keyWord)
    def setCarInfo(self):
        # 映射项
        for attribute in IOESMapping.listCarMappableShortText:
            self.setCarMappable(attribute, self.addShortObjectInfo)
        for attribute in IOESMapping.listCarMappableLongText:
            self.setCarMappable(attribute, self.addLongObjectInfo)
        # 透传项
        for attribute in IOESMapping.listCarMirrorableShortText:
            self.setCarMirrorable(attribute, self.addShortObjectInfo)
        for attribute in IOESMapping.listCarMirrorableLongText:
            self.setCarMirrorable(attribute, self.addLongObjectInfo)
        # TODO：需特殊处理项

    def setPersonInfo(self):
        pass
    def setFaceInfo(self):
        pass
    def setBikeInfo(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    rect = getRect(PREVIEW_WIDGET_X, PREVIEW_WIDGET_Y, PREVIEW_WIDGET_WIDTH, PREVIEW_WIDGET_HEIGHT)
    ex = PreviewWidget(rect, 1, 123, {})

    ex.setWindowTitle('样例数据')
    ex.addShortObjectInfo("车辆类型", "轿车")
    ex.addShortObjectInfo("危化车", "否")
    ex.addShortObjectInfo("车辆颜色数目", "1")
    ex.addShortObjectInfo("有无车牌", "有")
    ex.addLongObjectInfo("公路车收费车型", "1类客车")

    sys.exit(app.exec_())