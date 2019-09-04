# -*- coding: utf-8 -*-
#!/usr/local/bin/python
import sys
from PyQt5 import QtGui, QtWidgets
import IOESDemo

version = "version: 20190904001"

class IOESDemoApp(QtWidgets.QMainWindow, IOESDemo.Ui_IOESDemo):
    def __init__(self, parent=None):
        super(IOESDemoApp, self).__init__(parent)
        self.setupUi(self)
        self.statusBar().showMessage(version)

        self.registEvent()
        self.initStates()
        
    def initStates(self):
        print("initStates")

    def registEvent(self):
       self.btnStartTask.clicked.connect(self.startTask)
       self.btnStopTask.clicked.connect(self.stopTask)
       self.btnDumpResult.clicked.connect(self.dumpResult)
       self.btnBraws.clicked.connect(self.brawsImage)

    def startTask(self):
        print("startTask")
        #self.gvPreview.

    def stopTask(self):
        print("stopTask")

    def dumpResult(self):
        print("dumpResult")

    def brawsImage(self):
        download_path = QtWidgets.QFileDialog.getExistingDirectory(self, "浏览", "E:\workspace")
        self.edtImagePath.setText(download_path)

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = IOESDemoApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
