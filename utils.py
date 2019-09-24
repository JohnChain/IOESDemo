import os
import base64
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

VERSION = "version: 20190924001"

PEN_PERSON = QPen(Qt.red, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
PEN_FACE = QPen(Qt.magenta, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
PEN_HEAD = QPen(Qt.yellow, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
PEN_BODY = QPen(Qt.cyan, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
PEN_VEHICLE = QPen(Qt.green, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
PEN_NON_VEHICLE = QPen(Qt.blue, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
PEN_COMMON = QPen(Qt.red, 1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)

JVIA_UNKNOWN = "0"  #!< 未能定义的物体
JVIA_HUMAN = "1"  #!< 行人
JVIA_VEHICLE = "2"  #!< 车辆
JVIA_FACE = "3"  #!< 人臉
JVIA_BIKE = "4"  #!< 人骑车

FaceBoundingBox = "FaceBoundingBox"
HeadBoundingBox = "HeadBoundingBox"
UpperBoundingBox = "UpperBoundingBox"
LowerBoundingBox = "LowerBoundingBox"
CommonBox = "CommonBox"

TYPE_2_PEN = {
    JVIA_HUMAN : PEN_PERSON,
    JVIA_VEHICLE : PEN_VEHICLE,
    JVIA_BIKE : PEN_NON_VEHICLE,
    FaceBoundingBox: PEN_FACE,
    HeadBoundingBox: PEN_HEAD,
    UpperBoundingBox: PEN_BODY,
    LowerBoundingBox: PEN_BODY,
    CommonBox: PEN_COMMON,
}

def showMessageBox(base, title, msg):
    QMessageBox.information(base, title, msg)

def getImageList(dir_path):
    image_names = [name for name in os.listdir(dir_path) \
        if name.endswith('.jpg') or name.endswith('.png') or name.endswith('.bmp')]
    return image_names

def getRect(x, y, w, h):
    return QRectF(x, y, w, h)

def dict2Rect(mDict):
    return getRect(mDict["x"], mDict["y"], mDict["w"], mDict["h"])

def getDirPath(base, title):
    return QFileDialog.getExistingDirectory(base, title, "")

def toBase64(plainStr):
    return base64.b64encode(plainStr).decode('utf-8')

def fromBase64(b64Str):
    return base64.b64decode(b64Str)

def fileBase64(fileName):
    base64_data = ""
    try:
        with open(fileName, 'rb') as fileObj:
            image_data = fileObj.read()
            base64_data = toBase64(image_data)
    except FileNotFoundError:
        print("No such file or directory: %s" %fileName)
        return ''
    return base64_data

def genBody(filePath, id):
    jsonStr = fileBase64(filePath)
    output = {"Face": 1, "SubClass": 1}
    imageList = {"ImageID": id}
    imageList["Data"] = fileBase64(filePath)
    mdir = {"Output": output, "ImageList": [imageList]}