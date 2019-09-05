import os
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

version = "version: 20190905001"

def getDirPath(base, title):
    return QFileDialog.getExistingDirectory(base, title, "")

def showMessageBox(base, title, msg):
    QMessageBox.information(base, title, msg)

def getImageList(dir_path):
    imageNames = [name for name in os.listdir(dir_path) if name.endswith('.jpg') or name.endswith('.png') or name.endswith('.bmp') ]
    return imageNames