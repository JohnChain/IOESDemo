# -*- coding: utf-8 -*-
#!/usr/local/bin/python
from BGWorker import *
from IOESThread import IOESThread

class IASBGWorker(BGWorker):
    def __init__(self, parent=None):
        super(IASBGWorker, self).__init__()
        self.threadAddTask = IOESThread()
        self.freeCounter = 0

    def addTask(self, url, fileList):
        argc = 2
        argv = [url, fileList]
        self.threadAddTask.registFunction(self.addTaskInThead, argc, argv)
        self.threadAddTask.start()

    def addTaskInThead(self, argc, argv):
        logger.warning("IAS function not supported yet!!!")
        #TBD: add task to taskList
        pass

    def run(self):
        if(self.flagRun):
            logger.info("already runing")
            return
        self.flagRun = True
        sigMsg = ""
        while(self.flagRun):
            if(len(self.taskList) > 0):
                self.freeCounter = 0
                taskJson = self.taskList.pop(0)
                #TBD: process taskJson
            else:
                self.freeCounter += 1
                if self.freeCounter == 3:
                    break
                sleep(1)
        self.callback(SIG_TYPE_END, sigMsg)
        self.freeCounter = 0
        self.flagRun = False
        logger.info("Thread exited")