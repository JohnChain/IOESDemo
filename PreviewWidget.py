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

    def setCommonMappable(self, attribute, attribute2Name, mappable2Mapper, addObjectInfo):
        if attribute in self.dataDict:
            key = attribute2Name[attribute]
            mapper = mappable2Mapper[attribute]
            tempValue = self.dataDict[attribute]
            value = mapper[tempValue]
            addObjectInfo(key, value)
        else:
            print("%s not in dataDict" %keyWord)
    def setCommonMirrorable(self, attribute, attribute2Name, addObjectInfo):
        if attribute in self.dataDict:
            key = attribute2Name[attribute]
            value = self.dataDict[attribute]
            addObjectInfo(key, value)
        else:
            print("%s not in dataDict" %keyWord)

    def setCommonBox(self, attribute, attribute2Name, addObjectInfo):
        if attribute in self.dataDict:
            key = attribute2Name[attribute]
            box = self.dataDict[attribute]
            value = "(%d, %d, %d, %d)" %(box["x"], box["y"], box["w"], box["h"])
            addObjectInfo(key, value)
        else:
            print("%s not in dataDict" %keyWord)
    def setCommonColor(self, attribute, attribute2Name, mappable2Mapper, addObjectInfo):
        if attribute in self.dataDict:
            key = attribute2Name[attribute]
            mapper = mappable2Mapper[attribute]
            listColor = self.dataDict[attribute]
            value = []
            for colorCode in listColor:
                if colorCode in mapper:
                    value.append(mapper[colorCode])
                else:
                    value.append(colorCode)
            addObjectInfo(key, "[%s]" %(', '.join(value)))
        else:
            print("%s not in dataDict" %keyWord)
    def setSafetyBelt(self, attribute, addObjectInfo):
        if attribute in self.dataDict:
            key = IOESMapping.mapCarAttribute2Name[attribute]
            subDict = self.dataDict[attribute]
            mapper = IOESMapping.ThreeStateType
            mainDriver = mapper[subDict[CAR_ATTRIBUTE_MainDriver]]
            coDriver = mapper[subDict[CAR_ATTRIBUTE_CoDriver]]
            value = "{主驾驶%s系, 副驾驶%s系}" %(mainDriver, coDriver)
            addObjectInfo(key, value)
        else:
            print("%s not in dataDict" %keyWord)

    def setCarInfo(self):
        # 映射项
        for attribute in IOESMapping.listCarMappableShortText:
            self.setCommonMappable(attribute, IOESMapping.mapCarAttribute2Name, IOESMapping.mapCarMappable2Mapper, self.addShortObjectInfo)
        for attribute in IOESMapping.listCarMappableLongText:
            self.setCommonMappable(attribute, IOESMapping.mapCarAttribute2Name, IOESMapping.mapCarMappable2Mapper, self.addLongObjectInfo)
        # 透传项
        for attribute in IOESMapping.listCarMirrorableShortText:
            self.setCommonMirrorable(attribute, IOESMapping.mapCarAttribute2Name, self.addShortObjectInfo)
        for attribute in IOESMapping.listCarMirrorableLongText:
            self.setCommonMirrorable(attribute, IOESMapping.mapCarAttribute2Name, self.addLongObjectInfo)
        # Box项
        for attribute in IOESMapping.listCarBoxKey:
            self.setCommonBox(attribute, IOESMapping.mapCarAttribute2Name, self.addLongObjectInfo, )
        # 颜色数组
        for attribute in IOESMapping.listCarColorKey:
            self.setCommonColor(attribute, IOESMapping.mapCarAttribute2Name, IOESMapping.mapCarMappable2Mapper, self.addShortObjectInfo)
        # 安全带
        self.setSafetyBelt(CAR_ATTRIBUTE_SafetyBelt, self.addLongObjectInfo)

    def setPersonInfo(self):
        # 映射项
        for attribute in IOESMapping.listPersonMappableShortText:
            self.setCommonMappable(attribute, IOESMapping.mapPersonAttribute2Name, IOESMapping.mapPersonMappable2Mapper, self.addShortObjectInfo)
        for attribute in IOESMapping.listPersonMappableLongText:
            self.setCommonMappable(attribute, IOESMapping.mapPersonAttribute2Name, IOESMapping.mapPersonMappable2Mapper, self.addLongObjectInfo)
        # 透传项
        for attribute in IOESMapping.listPersonMirrorableShortText:
            self.setCommonMirrorable(attribute, IOESMapping.mapPersonAttribute2Name, self.addShortObjectInfo)
        for attribute in IOESMapping.listPersonMirrorableLongText:
            self.setCommonMirrorable(attribute, IOESMapping.mapPersonAttribute2Name, self.addLongObjectInfo)
        # Box项
        for attribute in IOESMapping.listPersonBoxKey:
            self.setCommonBox(attribute, IOESMapping.mapPersonAttribute2Name, self.addLongObjectInfo, )
        # 颜色数组
        for attribute in IOESMapping.listPersonColorKey:
            self.setCommonColor(attribute, IOESMapping.mapPersonAttribute2Name, IOESMapping.mapPersonMappable2Mapper, self.addShortObjectInfo)

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