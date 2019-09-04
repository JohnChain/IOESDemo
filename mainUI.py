# -*- coding: utf-8 -*-
#!/usr/local/bin/python
from PyQt5 import QtGui, QtWidgets
import sys
import IOESDemo

version = "version: 20190904001"

class IOESDemoApp(QtWidgets.QMainWindow, IOESDemo.Ui_MainWindow):
    def __init__(self, parent=None):
        super(IOESDemoApp, self).__init__(parent)
        self.setupUi(self)
        self.statusBar().showMessage(version)
        self.registEvent()
        self.initStates()
        
    def initStates(self):
        print("initStates")

    def registEvent(self):
        print("registEvent")

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = IOESDemoApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
