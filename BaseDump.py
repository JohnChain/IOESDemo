# -*- coding: utf-8 -*-
#!/usr/local/bin/python
from openpyxl import Workbook
from openpyxl.utils import get_column_letter

class BaseDump():
    def __init__(self, destFile, mapSheetName):
        self.destFile = destFile
        self.wb = Workbook()
        self.wsDict = {}
        for key, value in mapSheetName.items():
            self.wsDict[key] = self.wb.create_sheet(title=value, index=0)

    def save(self):
        self.wb.save(filename = self.destFile)

    def insert(self):
        pass

if __name__ == "__main__":
    TYPE_PERSON     = "1"
    TYPE_CAR        = "2"
    TYPE_FACE       = "3"
    TYPE_BIKE       = "4"

    ObjectType = {
        TYPE_FACE: "人脸",
        TYPE_BIKE: "非机动车",
        TYPE_PERSON: "行人",
        TYPE_CAR: "机动车",
    }
    destFile = "empty_book2.xlsx"

    dumper = BaseDump(destFile, ObjectType)
    dumper.save()