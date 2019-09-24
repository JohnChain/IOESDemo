#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class PreviewWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        
    def initUI(self):
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.red)
        self.setPalette(p)

        lbl1 = QLabel('Zetcode', self)
        lbl1.move(15, 10)

        lbl2 = QLabel('tutorials', self)
        lbl2.move(35, 40)
        
        lbl3 = QLabel('for programmers', self)
        lbl3.move(55, 70)
        
        self.setGeometry(30, 300, 250, 150)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PreviewWidget()
    ex.setWindowTitle('Absolute')
    sys.exit(app.exec_())