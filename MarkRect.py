# -*- coding: utf-8 -*-
#!/usr/local/bin/python
from utils import *

class MarkRectItem(QGraphicsRectItem):
    _signal = pyqtSignal(str, int)
    # 结合ImageDataManager中的
    # {
    #   "imageID1": [{objectID1}, {objectID2},...],
    #   "imageID2": [{objectID1}, {objectID2},...],
    # }
    # rect: 当前Item在QGraphicScene中的坐标框
    # boxtype :string : 标注框的类型(人/车/非机动车/人脸/上身/下身)
    # row: : string : "imageID1" / "imageID2" ...
    # index : int : index in each row list
    def __init__(self, rect, boxtype, row, index):
        super(MarkRectItem, self).__init__(rect)
        self.type = boxtype
        self.row = row
        self.index = index

    def mouseDoubleClickEvent(self, event):
        print("here in mouseDoubleClickEvent %s" %self.type)

    def mousePressEvent(self, event):
        print("here in mousePressEvent %s" %self.type)

    def mouseReleaseEvent(self, event):
        print("here in mouseReleaseEvent %s" %self.type)
        return QGraphicsRectItem.mouseReleaseEvent(self, event)

    def hoverMoveEvent(self, event):
        super(MarkRectItem, self).hoverMoveEvent(event)
        self.callback()

    def callback(self):
        #self._signal.emit(row, index)
        print("emit: row:%s index:%d" %(self.row, self.index))
        return

    def bindSignal(self, callback):
        #self._signal.connect(callback)
        return