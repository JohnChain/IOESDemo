
# -*- coding: utf-8 -*-
 
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class AppDemo(QMainWindow):
 
    def __init__(self):
        super(AppDemo, self).__init__()
        self.init_ui()
 
    def init_ui(self):
        self.resize(300, 200)
        self.setWindowTitle('666')
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText('六神花露水')
        self.label.setGeometry(5, 5, 145, 185)
        self.label.setMouseTracking(True)
 
        self.label_mouse_x = QLabel(self)
        self.label_mouse_x.setGeometry(155, 5, 80, 30)
        self.label_mouse_x.setText('x')
        self.label_mouse_x.setMouseTracking(True)
 
        self.label_mouse_y = QLabel(self)
        self.label_mouse_y.setText('y')
        self.label_mouse_y.setGeometry(155, 40, 80, 30)
        self.label_mouse_y.setMouseTracking(True)

        self.setMouseTracking(True)
 
    def mouseMoveEvent(self, event):
        s = event.windowPos()
        self.label_mouse_x.setText('X:' + str(s.x()))
        self.label_mouse_y.setText('Y:' + str(s.y()))
    
    def setMouseTracking(self, flag):
        def recursive_set(parent):
            for child in parent.findChildren(QObject):
                try:
                    child.setMouseTracking(flag)
                except:
                    pass
                recursive_set(child)
        QWidget.setMouseTracking(self, flag)
        recursive_set(self)
 
def run_it():
    app = QApplication(sys.argv)
    w = AppDemo()
    w.show()
    sys.exit(app.exec_())
 
 
if __name__ == '__main__':
    run_it()
