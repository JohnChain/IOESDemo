# -*- coding: utf-8 -*-
#!/usr/local/bin/python
import sys
import json
from IOESMapping import *
from BaseDump import BaseDump

class IOESDataManager:
    def __init__(self):
        self.imageResponse = {}

    # 将server返回的json字串，整理为一个字典
    # {
    #   "imageID1": [{objectID1}, {objectID2},...],
    #   "imageID2": [{objectID1}, {objectID2},...],
    # }
    # return: OK: "" Error: "reason"
    def genMap(self, jsonResponse):
        rst = ""
        jsonDir = json.loads(jsonResponse)
        if "ret" not in jsonDir or jsonDir["ret"] != "200":
            rst = "Invalid json response"
        elif "ObjectList" in jsonDir:
            objectList = jsonDir["ObjectList"]
            for obj in objectList:
                imageId = obj["ImageID"]
                if imageId in self.imageResponse:
                    self.imageResponse[imageId].append(obj)
                else:
                    self.imageResponse[imageId] = [obj]
        else:
            if "error_msg" in jsonDir:
                rst = "response error_msg: %s" %jsonDir[error_msg]
        return rst

    def clearMap(self):
        self.imageResponse.clear()

    def get(self, imageID):
        if imageID in self.imageResponse:
            return self.imageResponse[imageID]
        else:
            return []

    def count(self):
        return len(self.imageResponse)

    def dump(self, destFile):
        dumper = BaseDump(destFile, ObjectType)
        # 给每个sheet写列名称
        dumper.insert(TYPE_CAR, list(IOESCarMapping.mapAttribute2Name.values()))
        dumper.insert(TYPE_BIKE, list(IOESBikeMapping.mapAttribute2Name.values()))
        dumper.insert(TYPE_PERSON, list(IOESPersonMapping.mapAttribute2Name.values()))

        # 写所有数据

        # 保存到文件
        dumper.save()

if __name__ == "__main__":
    dataMapper = IOESDataManager()
    dataMapper.dump("empty_book2.xlsx")