import os
import base64
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

VERSION = "version: 2.2.2 2019102401"
DEFAULT_SERVICE_URL = "http://192.168.1.222:9098/images/recog"
MAX_BUNCH_LENGTH = 10
MAX_THREAD = 10

PREVIEW_WIDGET_X = 0
PREVIEW_WIDGET_Y = 200
PREVIEW_WIDGET_WIDTH = 300
PREVIEW_WIDGET_HEIGHT = 400
PREVIEW_WIDGET_BGCOLOR = QColor(27,78,125)

SIG_TYPE_DATA = "SIG_TYPE_DATA"
SIG_TYPE_END = "SIG_TYPE_END"
SIG_TYPE_ENTER = "SIG_TYPE_ENTER"
SIG_TYPE_LEAVE = "SIG_TYPE_LEAVE"
SIG_TYPE_DOUBLE_CLICK = "SIG_TYPE_DOUBLE_CLICK"

PEN_PERSON = QPen(Qt.red, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
PEN_FACE = QPen(Qt.magenta, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
PEN_HEAD = QPen(Qt.yellow, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
PEN_BODY = QPen(Qt.cyan, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
PEN_VEHICLE = QPen(Qt.green, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
PEN_NON_VEHICLE = QPen(Qt.blue, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
PEN_COMMON = QPen(Qt.red, 1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)

BRUSH_Y = QBrush(Qt.green)
BRUSH_F = QBrush(Qt.red)

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

JSON_PARSE_RET_CODE = "JSON_PARSE_RET_CODE"
JSON_PARSE_RET_REASON = "JSON_PARSE_RET_REASON"
JSON_PARSE_RET_PAYLOAD = "JSON_PARSE_RET_PAYLOAD"

JSON_PARSE_RET_OK = "0"
JSON_PARSE_RET_INVALID_JSON_RESPONSE = "-1"
JSON_PARSE_RET_PEER_ERROR = "-2"

JSON_PARSE_RET_MAPPER = {
    JSON_PARSE_RET_OK: "",
    JSON_PARSE_RET_INVALID_JSON_RESPONSE: "Invalid json response",
    JSON_PARSE_RET_PEER_ERROR: "Server return fail reason: ",
}

MODEL_FULL = "全目标据结构化"
MODEL_PBC = "行人、骑行、车辆检测识别"
MODEL_Face = "单独人脸检测识别"
MODEL_PB = "单独行人、骑行检测识别"
MODEL_Car = "单独车辆检测识别"
MODEL_LIST = [MODEL_FULL, MODEL_PBC, MODEL_Face, MODEL_PB, MODEL_Car]
MODEL_MAPPER= {
    MODEL_FULL: 1,
    MODEL_PBC: 2,
    MODEL_Face: 3,
    MODEL_PB: 4,
    MODEL_Car: 5,
}

GLOBAL_BUNCH_LENGTH = MAX_BUNCH_LENGTH
GLOBAL_THREAD = MAX_THREAD
GLOBAL_MODEL = MODEL_MAPPER[MODEL_FULL]

def showMessageBox(base, title, msg):
    QMessageBox.information(base, title, msg)

def getImageList(dir_path):
    image_names = [name for name in os.listdir(dir_path) \
        if name.endswith('.jpg') or name.endswith('.JPG') or name.endswith('.jpeg') or name.endswith('.JPEG') or name.endswith('.png') or name.endswith('.PNG') or name.endswith('.bmp') or name.endswith('.BMP')]
    return image_names

def getRectF(x, y, w, h):
    return QRectF(x, y, w, h)

def getRect(x, y, w, h):
    return QRect(x, y, w, h)

def dict2Rect(mDict):
    return getRectF(mDict["x"], mDict["y"], mDict["w"], mDict["h"])

def getDirPath(base, title):
    return QFileDialog.getExistingDirectory(base, title, "")

def getFilePath(base, filter = "", caption = ""):
    return QFileDialog.getSaveFileName(parent = base, caption = caption, filter = filter)

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