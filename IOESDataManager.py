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

    def getRow(self, imageID):
        if imageID in self.imageResponse:
            return self.imageResponse[imageID]
        else:
            return []

    def getObj(self, imageID, index):
        if imageID in self.imageResponse:
            objList = self.imageResponse[imageID]
            if len(objList) > index and "Metadata" in objList[index]:
                return objList[index]["Metadata"]
            else:
                return {}
        else:
            return {}

    def count(self):
        return len(self.imageResponse)

    def dumpPrepareList(self, listAttribute, mapAttribute2Name, listObj):
        for attribute in listAttribute:
            if attribute in mapAttribute2Name:
                listObj.append(mapAttribute2Name[attribute])
            else:
                listObj.append("?_?")
    def dumpPrepare(self, mapper, listObj):
        # 给每个sheet写列名称
        self.dumpPrepareList(mapper.listMappableShortText, mapper.mapAttribute2Name, listObj)
        self.dumpPrepareList(mapper.listMappableLongText, mapper.mapAttribute2Name, listObj)
        self.dumpPrepareList(mapper.listMirrorableShortText, mapper.mapAttribute2Name, listObj)
        self.dumpPrepareList(mapper.listMirrorableLongText, mapper.mapAttribute2Name, listObj)
        self.dumpPrepareList(mapper.listBoxKey, mapper.mapAttribute2Name, listObj)
        self.dumpPrepareList(mapper.listColorKey, mapper.mapAttribute2Name, listObj)

    def dumpCommonMappable(self, dataDict, listAttribute, mapMappable2Mapper, listObj):
        for attribute in listAttribute:
            if attribute in mapMappable2Mapper and attribute in dataDict:
                mapper = mapMappable2Mapper[attribute]
                value = dataDict[attribute]
                listObj.append(mapper[value])
            else:
                listObj.append("-")

    def dumpCommonMirrorable(self, dataDict, listAttribute, listObj):
        for attribute in listAttribute:
            if attribute in dataDict:
                listObj.append(dataDict[attribute])
            else:
                listObj.append("-")
    def dumpCommonBox(self, dataDict, listAttribute, listObj):
        for attribute in listAttribute:
            if attribute in dataDict:
                box = dataDict[attribute]
                value = "(%d, %d, %d, %d)" %(box["x"], box["y"], box["w"], box["h"])
                listObj.append(value)
            else:
                listObj.append("-")

    def dumpCommonColor(self, dataDict, listAttribute, mapMappable2Mapper, listObj):
        for attribute in listAttribute:
            if attribute in dataDict and attribute in mapMappable2Mapper:
                mapper = mapMappable2Mapper[attribute]
                listColor = dataDict[attribute]
                value = []
                for colorCode in listColor:
                    if colorCode in mapper:
                        value.append(mapper[colorCode])
                    else:
                        value.append(colorCode)
                listObj.append("[%s]" %(', '.join(value)))
            else:
                listObj.append("-")

    # 返回 list
    def dumpCommonObj(self, dataDict, IOESMapping, listObj):
        self.dumpCommonMappable(dataDict, IOESMapping.listMappableShortText, IOESMapping.mapMappable2Mapper, listObj)
        self.dumpCommonMappable(dataDict, IOESMapping.listMappableLongText, IOESMapping.mapMappable2Mapper, listObj)
        self.dumpCommonMirrorable(dataDict, IOESMapping.listMirrorableShortText, listObj)
        self.dumpCommonMirrorable(dataDict, IOESMapping.listMirrorableLongText, listObj)
        self.dumpCommonBox(dataDict, IOESMapping.listBoxKey, listObj)
        self.dumpCommonColor(dataDict, IOESMapping.listColorKey, IOESMapping.mapMappable2Mapper, listObj)

    def dumpSafetyBelt(self, dataDict, mapMappable2Mapper, listObj):
        attribute = CAR_ATTRIBUTE_SafetyBelt
        if attribute in dataDict and attribute in mapMappable2Mapper:
            subDict = dataDict[attribute]
            mapper = mapMappable2Mapper[attribute]
            mainDriver = mapper[subDict[CAR_ATTRIBUTE_MainDriver]]
            coDriver = mapper[subDict[CAR_ATTRIBUTE_CoDriver]]
            listObj.append("{主驾驶%s系, 副驾驶%s系}" %(mainDriver, coDriver))
        else:
            listObj.append("-")

    def dumpCarInfo(self, dataDict, dumper):
        listObj = ["图片路径"]
        self.dumpPrepare(IOESCarMapping, listObj)
        listObj.append(IOESCarMapping.mapAttribute2Name[CAR_ATTRIBUTE_SafetyBelt])
        dumper.insert(TYPE_CAR, listObj)

        listObj = ["/home/xxx/xx/xx"]
        # get common
        self.dumpCommonObj(dataDict, IOESCarMapping, listObj)
        # get safeBar
        self.dumpSafetyBelt(dataDict, IOESCarMapping.mapMappable2Mapper, listObj)
        dumper.insert(TYPE_CAR, listObj)
        dumper.save()

    def dumpPersonInfo(self, dataDict, dumper):
        listObj = ["图片路径"]
        self.dumpPrepare(IOESPersonMapping, listObj)
        dumper.insert(TYPE_PERSON, listObj)

        listObj = ["/home/xxx/xx/xx"]
        # get common
        self.dumpCommonObj(dataDict, IOESPersonMapping, listObj)
        dumper.insert(TYPE_PERSON, listObj)
        dumper.save()

    def dumpBikeInfo(self, dataDict, dumper):
        listObj = ["图片路径"]
        self.dumpPrepare(IOESBikeMapping, listObj)
        dumper.insert(TYPE_BIKE, listObj)

        listObj = ["/home/xxx/xx/xx"]
        # get common
        self.dumpCommonObj(dataDict, IOESBikeMapping, listObj)
        dumper.insert(TYPE_BIKE, listObj)
        dumper.save()

    def dump(self, destFile):
        dumper = BaseDump(destFile, ObjectType)
        # 写所有数据
        for oneRow in self.imageResponse.values():
            for obj in oneRow:
                listRowValue = []
                dataDict = obj["Metadata"]
                if ATTRIBUTE_Type in dataDict:
                    objType = dataDict[ATTRIBUTE_Type]
                    if objType == TYPE_CAR:
                        self.dumpCarInfo(dataDict,dumper)
                    elif objType == TYPE_PERSON:
                        self.dumpPersonInfo(dataDict, dumper)
                    elif objType == TYPE_BIKE:
                        self.dumpBikeInfo(dataDict, dumper)
                    else:
                        return "Error: unknow object type ", objType
                else:
                    return "Error: cannot find object type"
        return ""

    def getObjectMapper(self, dataDict):
        if ATTRIBUTE_Type in dataDict:
            objType = dataDict[ATTRIBUTE_Type]
            if objType == TYPE_CAR:
                return TYPE_CAR, IOESCarMapping
            elif objType == TYPE_PERSON:
                return TYPE_PERSON, IOESPersonMapping
            elif objType == TYPE_BIKE:
                return TYPE_BIKE, IOESBikeMapping
            else:
                print("Error: unknow object type ", objType)
                return None, None
        else:
            print("Error: cannot find object type")
            return None, None

if __name__ == "__main__":
    dataMapper = IOESDataManager()
    dataMapper.dump("empty_book2.xlsx")