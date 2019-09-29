# -*- coding: utf-8 -*-
#!/usr/local/bin/python
from BGWorker import *

class IOESBGWorker(BGWorker):
    def __init__(self, parent=None):
        super(IOESBGWorker, self).__init__()
        self.freeCounter = 0
    
    def run(self):
        if(self.flagRun):
            print("already runing")
            return
        self.flagRun = True
        while(self.flagRun):
            if(len(self.taskList) > 0):
                self.freeCounter = 0
                taskJson = self.taskList.pop()
                url = taskJson["url"]
                body = taskJson["body"]
                rspJosn = self.postJson(url, body)
                self.callback(SIG_TYPE_DATA, rspJosn)
            else:
                self.freeCounter += 1
                if self.freeCounter == 3:
                    break
                sleep(1)
        self.callback(SIG_TYPE_END, "")
        self.freeCounter = 0
        self.flagRun = False
        print("Thread exited")
    
    def addTask(self, url, fileList):
        tempCount = 0 # 辅助计算8张图片一组
        imageList = []
        for index in range(len(fileList)):
            tempCount = tempCount + 1
            if tempCount > MAX_BUNCH_LENGTH:
                self.addJsonTask(url, imageList)
                tempCount = 0
                imageList = []
            filePath = fileList[index]
            imageCell = {"ImageID": "%d" %index}
            imageCell["Data"] = fileBase64(filePath)
            imageList.append(imageCell)
        if len(imageList) > 0:  #最后一组不满8张
            self.addJsonTask(url, imageList)

    def addJsonTask(self, url, imageList):
        output = {"Face": 1, "SubClass": 1}
        mdict = {"Output": output, "ImageList": imageList}
        task = {"url": url, "body": mdict}
        self.taskList.append(task)
