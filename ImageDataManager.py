# -*- coding: utf-8 -*-
#!/usr/local/bin/python
import sys
import json
from utils import *
from HttpOps import HttpOps

class ImageDataManager:
    def __init__(self):
        self.imageResponse = {}
        self.httpOps = HttpOps()

    # 将server返回的json字串，整理为一个字典
    # {
    #   "imageID1": [{objectID1}, {objectID2},...],
    #   "imageID2": [{objectID1}, {objectID2},...],
    # }
    # return: OK: 0 Error: -1
    def genMap(self, jsonResponse):
        jsonDir = json.loads(jsonResponse)
        if jsonDir["ret"] != "200":
            return -1
        objectList = jsonDir["ObjectList"]
        for obj in objectList:
            imageId = obj["ImageID"]
            if imageId in self.imageResponse:
                self.imageResponse[imageId].append(obj)
            else:
                self.imageResponse[imageId] = [obj]
        return 0

    def clearMap(self):
        self.imageResponse.clear()

    def get(self, imageID):
        if imageID in self.imageResponse:
            return self.imageResponse[imageID]
        else:
            return []
    
    def count(self):
        return len(self.imageResponse)
