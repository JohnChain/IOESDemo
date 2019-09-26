# -*- coding: utf-8 -*-
#!/usr/local/bin/python
from PyQt5.QtCore import *
from HttpOps import HttpOps
from ImageDataManager import ImageDataManager
from time import sleep
from utils import *

class BGWorker(QThread):
    _signal = pyqtSignal(str)
    _signalExit = pyqtSignal(str)
    def __init__(self, parent=None):
        super(BGWorker, self).__init__()
        self.httpOps = HttpOps()
        self.taskList = []
        self.flagRun = False
 
    def __del__(self):
        self.flagRun = False
        self.taskList.clear()
        self.wait()
 
    def addTask(self, task):
        print("here addTask")
        self.taskList.append(task)

    def stop(self):
        print("here call stop")
        self.flagRun = False
        self.clearTask()
    
    def clearTask(self):
        self.taskList.clear()

    def run(self):
        # 处理你要做的业务逻辑，这里是通过一个回调来处理数据，这里的逻辑处理写自己的方法
        print("runing")

    def callback(self, type, rstJson):
        if type == SIG_TYPE_DATA:
            self._signal.emit(rstJson)
        elif type == SIG_TYPE_END:
            self._signalExit.emit(rstJson)

    def bindSignal(self, type, callback):
        if type == SIG_TYPE_DATA:
            self._signal.connect(callback)
        elif type == SIG_TYPE_END:
            self._signalExit.connect(callback)

    def postJson(self, url, mdir):
        rspjson = self.httpOps.post(url, mdir)
        return rspjson
