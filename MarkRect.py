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
        super(MarkRectItem, self).mouseDoubleClickEvent(event)
        self.callback(SIG_TYPE_DOUBLE_CLICK)

    def hoverEnterEvent(self, event):
        super(MarkRectItem, self).hoverEnterEvent(event)
        self.callback(SIG_TYPE_ENTER)

    def hoverLeaveEvent(self, event):
        super(MarkRectItem, self).hoverLeaveEvent(event)
        self.callback(SIG_TYPE_LEAVE)
        return QGraphicsRectItem.hoverLeaveEvent(self, event)

    def callback(self, SIG_TYPE):
        self._signal.emit(SIG_TYPE, self.row, self.index)
        return

    def bindSignal(self, callback):
        self._signal.connect(callback)
        return