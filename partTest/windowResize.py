# -- coding: utf-8 --
import sys
from PyQt5 import QtWidgets

class MyWindow(QtWidgets.QWidget):
    def init(self, parent=None):
        QtWidgets.QWidget.init(self, parent)
        self.resize(300, 100)

    def moveEvent(self, e):
        print("x = {0}; y = {1}".format(e.pos().x(), e.pos().y()))
        QtWidgets.QWidget.moveEvent(self, e)

    def resizeEvent(self, e):
        print("w = {0}; h = {1}".format(e.size().width(), e.size().height()))
        QtWidgets.QWidget.resizeEvent(self, e)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
