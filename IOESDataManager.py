# -*- coding: utf-8 -*-
#!/usr/local/bin/python
import sys
import json
from IOESMapping import *
from BaseDump import BaseDump
from openpyxl.drawing.image import Image
from IOESThread import IOESThread
import openpyxl

class IOESDataManager:
    def __init__(self):
        self.imageResponse = {}
        self.threadAddTask = IOESThread()

    # 将server返回的json字串，整理为一个字典
    # {
    #   "imageID1": [{objectID1}, {objectID2},...],
    #   "imageID2": [{objectID1}, {objectID2},...],
    # }
    # return: 一个字典, eg
    # {
    # "JSON_PARSE_RET_CODE": "0",
    # "JSON_PARSE_RET_REASON": "xxxx",
    # "JSON_PARSE_RET_PAYLOAD": { "1": brush, "2": brush,...}
    # }
    def genMap(self, jsonResponse):
        ret = {}
        code = ""
        reason = ""
        id2brush = {}  # { "1": brush, "2": brush,...}
        jsonDir = json.loads(jsonResponse)
        if "ret" not in jsonDir or jsonDir["ret"] != "200":
            code = JSON_PARSE_RET_INVALID_JSON_RESPONSE
            reason = JSON_PARSE_RET_MAPPER[JSON_PARSE_RET_INVALID_JSON_RESPONSE]
        else:
            if "ObjectList" in jsonDir:
                code = JSON_PARSE_RET_OK
                objectList = jsonDir["ObjectList"]
                for obj in objectList:
                    imageId = obj["ImageID"]
                    if imageId in self.imageResponse: #已存在的imageID，追加入list
                        self.imageResponse[imageId].append(obj)
                    else: #新的imageID，增加为list
                        self.imageResponse[imageId] = [obj]
                        id2brush[imageId] = BRUSH_Y
            else:
                code = JSON_PARSE_RET_PEER_ERROR
                if "error_msg" in jsonDir:
                    reason = JSON_PARSE_RET_MAPPER[JSON_PARSE_RET_PEER_ERROR] + jsonDir[error_msg]
                else:
                    reason = JSON_PARSE_RET_MAPPER[JSON_PARSE_RET_PEER_ERROR] + "service not give reason"
        ret[JSON_PARSE_RET_CODE] = code
        ret[JSON_PARSE_RET_REASON] = reason
        ret[JSON_PARSE_RET_PAYLOAD] = id2brush

        return ret

    def clearMap(self):
        self.imageResponse.clear()

    def getRow(self, imageID):
        if imageID in self.imageResponse:
            return self.imageResponse[imageID]
        else:
            return []

    def getObjMetadata(self, imageID, index):
        obj = self.getObj(imageID, index)
        if "Metadata" in obj:
            return obj["Metadata"]
        else:
            return {}

    def getObj(self, imageID, index):
        if imageID in self.imageResponse:
            objList = self.imageResponse[imageID]
            if len(objList) > index:
                return objList[index]
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
    def dumpPrepare(self, mapper):
        listObj = ["图片", "图片路径"]
        # 给每个sheet写列名称
        self.dumpPrepareList(mapper.listMappableShortText, mapper.mapAttribute2Name, listObj)
        self.dumpPrepareList(mapper.listMappableLongText, mapper.mapAttribute2Name, listObj)
        self.dumpPrepareList(mapper.listMirrorableShortText, mapper.mapAttribute2Name, listObj)
        self.dumpPrepareList(mapper.listMirrorableLongText, mapper.mapAttribute2Name, listObj)
        self.dumpPrepareList(mapper.listBoxKey, mapper.mapAttribute2Name, listObj)
        self.dumpPrepareList(mapper.listColorKey, mapper.mapAttribute2Name, listObj)
        return listObj

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

    def genImage(self, fileName, row):
        img = openpyxl.drawing.image.Image(fileName)
        img.height = 50
        img.width = 50
        img.anchor = "A%d" %row
        return img
    def dumpImage(self, objType, dumper, fileName, listFileDumped):
        if fileName not in listFileDumped:
            row = dumper.getCurrentRow(objType)
            img = self.genImage(fileName, row)
            dumper.insertImage(objType, img)
            listFileDumped.append(fileName)

    def dumpCarInfo(self, dataDict, listFileDumped, dumper, fileName):
        listObj = ["", fileName] #空出第一列给原始图片
        # get common
        self.dumpCommonObj(dataDict, IOESCarMapping, listObj)
        # get safeBar
        self.dumpSafetyBelt(dataDict, IOESCarMapping.mapMappable2Mapper, listObj)
        dumper.insert(TYPE_CAR, listObj)
        self.dumpImage(TYPE_CAR, dumper, fileName, listFileDumped)
        dumper.save()

    def dumpPersonInfo(self, dataDict, listFileDumped, dumper, fileName):
        listObj = ["", fileName] #空出第一列给原始图片
        # get common
        self.dumpCommonObj(dataDict, IOESPersonMapping, listObj)
        dumper.insert(TYPE_PERSON, listObj)
        self.dumpImage(TYPE_PERSON, dumper, fileName, listFileDumped)
        dumper.save()

    def dumpBikeInfo(self, dataDict, listFileDumped, dumper, fileName):
        listObj = ["", fileName] #空出第一列给原始图片
        # get common
        self.dumpCommonObj(dataDict, IOESBikeMapping, listObj)
        dumper.insert(TYPE_BIKE, listObj)
        self.dumpImage(TYPE_BIKE, dumper, fileName, listFileDumped)
        dumper.save()
    
    def addTask(self, url, fileList):
        argc = 2
        argv = [url, fileList]
        self.threadAddTask.registFunction(self.addTaskInThead, argc, argv)
        self.threadAddTask.start()

    def dump(self, listImageName, destFile):
        dumper = BaseDump(destFile, ObjectType)
        listFileDumpedCar = []
        listFileDumpedBike = []
        listFileDumpedPerson = []

        listObj = self.dumpPrepare(IOESCarMapping)
        listObj.append(IOESCarMapping.mapAttribute2Name[CAR_ATTRIBUTE_SafetyBelt])
        dumper.insert(TYPE_CAR, listObj)

        listObj = self.dumpPrepare(IOESPersonMapping)
        dumper.insert(TYPE_PERSON, listObj)

        listObj = self.dumpPrepare(IOESBikeMapping)
        dumper.insert(TYPE_BIKE, listObj)
        # 写所有数据
        index = 0
        for oneRow in self.imageResponse.values():
            fileName = listImageName[index]
            index += 1
            for obj in oneRow:
                listRowValue = []
                dataDict = obj["Metadata"]
                if ATTRIBUTE_Type in dataDict:
                    objType = dataDict[ATTRIBUTE_Type]
                    if objType == TYPE_CAR:
                        self.dumpCarInfo(dataDict, listFileDumpedCar, dumper, fileName)
                    elif objType == TYPE_PERSON:
                        self.dumpPersonInfo(dataDict, listFileDumpedPerson, dumper, fileName)
                    elif objType == TYPE_BIKE:
                        self.dumpBikeInfo(dataDict, listFileDumpedBike, dumper, fileName)
                    else:
                        return "Error: unknow object type ", objType
                else:
                    return "Error: cannot find object type"
        return ""

if __name__ == "__main__":
    dataMapper = IOESDataManager()
    dataMapper.dump("empty_book2.xlsx")