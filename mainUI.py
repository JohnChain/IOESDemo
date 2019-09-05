# -*- coding: utf-8 -*-
#!/usr/local/bin/python
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from utils import *
import IOESDemo

class IOESDemoApp(QMainWindow, IOESDemo.Ui_IOESDemo):
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
       self.listImages.itemClicked.connect(self.previewImage)

    def previewImage(self, item):
        fullPath = self.edtImagePath.text() + "/" + item.text()
        self.updateImage(fullPath)

    def updateImage(self, image_path):
        pixmap = QPixmap(image_path)
        #scaledPixmap = pixmap.scaled(500, 1000)
        #self.pixmap_item = QGraphicsPixmapItem(scaledPixmap)
        self.pixmap_item = QGraphicsPixmapItem(pixmap)
        self.scene = QGraphicsScene(self.gvPreview)
        #self.scene.setSceneRect(0, 0, 300, 300)
        self.scene.addItem(self.pixmap_item)
        self.gvPreview.setScene(self.scene)

    def startTask(self):
        showMessageBox(self, "startTask", "height: %d, width: %d" %(self.gvPreview.size().height(), self.gvPreview.size().width()))

    def stopTask(self):
        scene = QGraphicsScene(self.gvPreview)
        scene.addText("Hello, world!")
        self.gvPreview.setScene(scene)

    def dumpResult(self):
        return

    def brawsImage(self):
        dir_path = getDirPath(self, "图片路径")
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
    app = QApplication(sys.argv)
    form = IOESDemoApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
