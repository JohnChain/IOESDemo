# -*- coding: utf-8 -*-
#!/usr/local/bin/python
from utils import *

CAR_ATTRIBUTE_BRAND = 'VehicleBrand'
CAR_ATTRIBUTE_PLATENO = 'PlateNo'

class IOESMapping():
    ObjectType = {
        "1": "行人",
        "2": "车辆",
        "3": "人脸",
        "4": "人骑车",
    }

    GenderType = {
        "1": "男性",
        "2": "女性",
        "-1": "未知",
    }

    AgeType = {
        "4": "小朋友",
        "8": "青年",
        "16": "中年",
        "32": "老年",
        "-1": "未知",
    }

    AngleType = {
        "128": "正面",
        "256": "侧面",
        "512": "背面",
        "-1": "未知",
    }

    CoatType = {
        "1": "长袖",
        "2": "短袖",
        "-1": "未知",
    }

    TrousersType = {
        "1": "长裤",
        "2": "短裤",
        "3": "裙子",
        "-1": "未知",
    }

    ObjectColorType = {
        "5263440": "深灰",
        "0": "黑",
        "11842740": "灰",
        "343174": "棕",
        "16724484": "蓝",
        "8327170": "蓝（宝石蓝）",
        "16743167": "粉",
        "9983": "红",
        "12423793": "蓝（浅灰蓝）",
        "15311656": "蓝（淡蓝）",
        "16777215": "白",
        "5287936": "绿",
        "65535": "黄",
        "8761028": "棕（卡其）",
        "9576596": "紫",
        "16776448": "青",
        "37887": "橙",
        "11711154": "灰（银）",
        "2111058": "棕",
        "6579300": "灰",
        "11306222": "粉",
        "-1": "未知",
    }

    VehicleClassType = {
        "1":	"轿车",
        "2":	"越野车/SUV类",
        "3":	"商务车/MPV类",
        "4":	"小型货车",
        "5":	"中型货车",
        "6":	"大型货车",
        "7":	"轻客",
        "8":	"中型客车",
        "9":	"大型客车",
        "10":	"面包车",
        "11":	"皮卡",
        "12":	"罐车",
        "13":	"渣土车",
        "14":	"校车",
        "15":	"公交车",
        "98":	"三轮车",
        "99":	"其他（专用车）",
        "-1":	"未知",
    }

    carAttribute2Name = {
       CAR_ATTRIBUTE_BRAND: "车辆品牌",
       CAR_ATTRIBUTE_PLATENO: "车牌号码",
    }

    mirrorKeyList = [
        CAR_ATTRIBUTE_BRAND,
        CAR_ATTRIBUTE_PLATENO,
    ]
    mapKeyList = [
        "Type",
        "Angle",
        "VehicleClass",
        "VehicleColorNums",
        "HasPlate",
        "PlateClass",
        "PlateColor",
        "Sunvisor",
        "Paper",
        "Decoration",
        "Drop",
        "Tag",
        "HasCall",
        "HasSkylight",
        "HasBaggage",
        "HasAerial",
        "HasCrash",
        "HasDanger",
        "HighwayTollVehicles",
    ]

if __name__ == '__main__':
    pass