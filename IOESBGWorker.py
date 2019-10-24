# -*- coding: utf-8 -*-
#!/usr/local/bin/python
from BGWorker import *
from IOESThread import IOESThread

class IOESBGWorker(BGWorker):
    def __init__(self, parent=None):
        super(IOESBGWorker, self).__init__()
        self.freeCounter = 0
        self.threadAddTask = IOESThread()
    
    def run(self):
        if(self.flagRun):
            print("already runing")
            return
        self.flagRun = True
        while(self.flagRun):
            if(len(self.taskList) > 0):
                self.freeCounter = 0
                taskJson = self.taskList.pop(0)
                url = taskJson["url"]
                body = taskJson["body"]
                rspJson = self.postJson(url, body)
                self.callback(SIG_TYPE_DATA, rspJson)
                if rspJson == "" or rspJson[:5] == "Error":
                    break
            else:
                self.freeCounter += 1
                if self.freeCounter == 3:
                    break
                sleep(1)
        self.callback(SIG_TYPE_END, "")
        self.freeCounter = 0
        self.flagRun = False
        print("Thread exited")

    def addTaskInThead(self, argc, argv):
        url = argv[0]
        fileList = argv[1]
        tempCount = 0 # 辅助计算8张图片一组
        imageList = []
        for index in range(len(fileList)):
            if(not self.flagRun):
                imageList.clear()
                break
            tempCount = tempCount + 1
            if tempCount >= GLOBAL_BUNCH_LENGTH:
                self.addJsonTask(url, imageList)
                tempCount = 0
                imageList = []
            filePath = fileList[index]
            imageCell = {"ImageID": "%d" %index}
            imageCell["Data"] = fileBase64(filePath)
            imageList.append(imageCell)
        if len(imageList) > 0:  #最后一组不满8张
            self.addJsonTask(url, imageList)

    def addTask(self, url, fileList):
        argc = 2
        argv = [url, fileList]
        self.threadAddTask.registFunction(self.addTaskInThead, argc, argv)
        self.threadAddTask.start()

    def addJsonTask(self, url, imageList):
        output = {"Face": 1, "SubClass": 1}
        mdict = {"Output": output, "ImageList": imageList}
        task = {"url": url, "body": mdict}
        self.taskList.append(task)
