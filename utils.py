import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

VERSION = "version: 20190905001"
SAMPLEJSON = """{
		"x":	124,
		"y":	34,
		"w":	344,
		"h":	433
	}"""

PEN_PERSON = QPen(Qt.red, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
PEN_FACE = QPen(Qt.magenta, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
PEN_HEAD = QPen(Qt.yellow, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
PEN_BODY = QPen(Qt.cyan, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
PEN_VEHICLE = QPen(Qt.green, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
PEN_NON_VEHICLE = QPen(Qt.blue, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)

def showMessageBox(base, title, msg):
    QMessageBox.information(base, title, msg)

def getImageList(dir_path):
    image_names = [name for name in os.listdir(dir_path) \
        if name.endswith('.jpg') or name.endswith('.png') or name.endswith('.bmp')]
    return image_names

def getRect(x, y, h, w):
    return QRectF(x, y, h, w)

def getDirPath(base, title):
    return QFileDialog.getExistingDirectory(base, title, "")