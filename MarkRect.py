# -*- coding: utf-8 -*-
#!/usr/local/bin/python
from utils import *

class MarkRectItem(QGraphicsRectItem):
    # 结合ImageDataManager中的
    # {
    #   "imageID1": [{objectID1}, {objectID2},...],
    #   "imageID2": [{objectID1}, {objectID2},...],
    # }
    # rect: 当前Item在QGraphicScene中的坐标框
    # boxtype :string : 标注框的类型(人/车/非机动车/人脸/上身/下身)
    # row: : string : "imageID1" / "imageID2" ...
    # index : int : index in each row list
    def __init__(self, signal, rect, boxtype, row, index):
        super(MarkRectItem, self).__init__(rect)
        self.type = boxtype
        self.row = row
        self.index = index
        self._signal = signal

    def mouseDoubleClickEvent(self, event):
        print("here in mouseDoubleClickEvent %s" %self.type)

    def mousePressEvent(self, event):
        print("here in mousePressEvent %s" %self.type)

    def mouseReleaseEvent(self, event):
        print("here in mouseReleaseEvent %s" %self.type)
        return QGraphicsRectItem.mouseReleaseEvent(self, event)

    def hoverMoveEvent(self, event):
        super(MarkRectItem, self).hoverMoveEvent(event)
        self.callback(1)

    def hoverLeaveEvent(self, event):
        super(MarkRectItem, self).hoverMoveEvent(event)
        self.callback(0)

    def callback(self, isActive):
        self._signal.emit(isActive, self.row, self.index)
        print("emit: isActive: %d, row:%s index:%d" %(isActive, self.row, self.index))
        return

    def bindSignal(self, callback):
        self._signal.connect(callback)
        return