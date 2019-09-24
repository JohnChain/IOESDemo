# -*- coding: utf-8 -*-
#!/usr/local/bin/python
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MarkRectItem(QGraphicsRectItem):
    def mouseDoubleClickEvent(self, event):
        print("here in mouseDoubleClickEvent")

    def mousePressEvent(self, event):
        print("here in mousePressEvent")

    def mouseReleaseEvent(self, event):
        # recolor on click
        print("here in mouseReleaseEvent")
        return QGraphicsRectItem.mouseReleaseEvent(self, event)

    def hoverMoveEvent(self, event):
        # Do your stuff here.
        brush = QBrush(Qt.NoBrush)
        QGraphicsRectItem.setBrush(self, brush)
        print("here in hoverMoveEvent")