# -*- coding: utf-8 -*-
#!/usr/local/bin/python
import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from utils import *
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
        self.listImages.clear()
        self.edtImagePath.setReadOnly(True)

    def registEvent(self):
       self.btnStartTask.clicked.connect(self.startTask)
       self.btnStopTask.clicked.connect(self.stopTask)
       self.btnDumpResult.clicked.connect(self.dumpResult)
       self.btnBraws.clicked.connect(self.brawsImage)

    def startTask(self):
        pixmap = QPixmap("IOESDemo/face/face2.jpg")
        #scaledPixmap = pixmap.scaled(500, 1000)
        #self.pixmap_item = QGraphicsPixmapItem(scaledPixmap)
        self.pixmap_item = QGraphicsPixmapItem(pixmap)
        self.scene = QGraphicsScene(self.gvPreview)
        #self.scene.setSceneRect(0, 0, 300, 300)
        self.scene.addItem(self.pixmap_item)
        self.gvPreview.setScene(self.scene)

    def stopTask(self):
        scene = QGraphicsScene(self.gvPreview)
        scene.addText("Hello, world!")
        self.gvPreview.setScene(scene)

    def dumpResult(self):
        print(self.gvPreview.size())

    def getDirPath(self):
        return QtWidgets.QFileDialog.getExistingDirectory(self, "图片路径", "")

    def brawsImage(self):
        dir_path = self.getDirPath()
        if dir_path == "":
            return
        self.edtImagePath.setText(dir_path)
        self.listImages.clear()
        imageNames = getImageList(dir_path)
        for name in imageNames:
            item = QListWidgetItem("%s" % name)
            self.listImages.addItem(item)
        self.lblTotalImageNum.setText("%d" %len(imageNames))

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = IOESDemoApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
