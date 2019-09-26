# -*- coding: utf-8 -*-
#!/usr/local/bin/python
from utils import *

class MarkRectItem(QGraphicsRectItem):
    def __init__(self, rect, type):
        super(MarkRectItem, self).__init__(rect)
        self.type = type

    def mouseDoubleClickEvent(self, event):
        print("here in mouseDoubleClickEvent %s" %self.type)

    def mousePressEvent(self, event):
        print("here in mousePressEvent %s" %self.type)

    def mouseReleaseEvent(self, event):
        # recolor on click
        print("here in mouseReleaseEvent %s" %self.type)
        return QGraphicsRectItem.mouseReleaseEvent(self, event)

    def hoverMoveEvent(self, event):
        # Do your stuff here.
        brush = QBrush(Qt.NoBrush)
        QGraphicsRectItem.setBrush(self, brush)
        print("here in hoverMoveEvent %s" %self.type)