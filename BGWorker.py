from PyQt5.QtCore import *
from HttpOps import HttpOps
from ImageDataManager import ImageDataManager
from time import sleep

class BGWorker(QThread):
    #  通过类成员对象定义信号对象
    _signal = pyqtSignal(str)
 
    def __init__(self, parent=None):
        super(BGWorker, self).__init__()
        self.httpOps = HttpOps()
        self.taskList = []
        self.flagRun = False
 
    def __del__(self):
        self.wait()
 
    def addTask(self, task):
        print("here addTask")
        self.taskList.append(task)

    def stop(self):
        print("here call stop")
        self.flagRun = False

    def run(self):
        # 处理你要做的业务逻辑，这里是通过一个回调来处理数据，这里的逻辑处理写自己的方法
        print("runing")
        if(self.flagRun):
            print("already runing")
            return
        self.flagRun = True
        while(self.flagRun):
            if(len(self.taskList) > 0):
                taskJson = self.taskList.pop()
                url = taskJson["url"]
                body = taskJson["body"]
                rspJosn = self.postJson(url, body)
                self.callback(rspJosn)
            else:
                print("run sleep 1")
                sleep(1)
        print("Thread exited")

    def callback(self, rstJson):
        # 信号焕发，我是通过我封装类的回调来发起的
        self._signal.emit(rstJson)

    def bindSignal(self, callback):
        print("here bindSignal")
        self._signal.connect(callback)
    
    def postJson(self, url, mdir):
        rspjson = self.httpOps.post(url, mdir)
        return rspjson
