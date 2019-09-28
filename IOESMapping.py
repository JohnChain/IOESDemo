# -*- coding: utf-8 -*-
#!/usr/local/bin/python
from utils import *

ATTRIBUTE_Type  = 'Type'
TYPE_PERSON     = "1"
TYPE_CAR        = "2"
TYPE_FACE       = "3"
TYPE_BIKE       = "4"
#######################################################
# 车辆
# 需要映射项
CAR_ATTRIBUTE_Angle                 = 'Angle'
CAR_ATTRIBUTE_VehicleClass          = 'VehicleClass'
CAR_ATTRIBUTE_VehicleColorNums      = 'VehicleColorNums'
CAR_ATTRIBUTE_HasPlate              = 'HasPlate'
CAR_ATTRIBUTE_PlateClass            = 'PlateClass'
CAR_ATTRIBUTE_PlateColor            = 'PlateColor'
CAR_ATTRIBUTE_Sunvisor              = 'Sunvisor'
CAR_ATTRIBUTE_Paper                 = 'Paper'
CAR_ATTRIBUTE_Decoration            = 'Decoration'
CAR_ATTRIBUTE_Drop                  = 'Drop'
CAR_ATTRIBUTE_Tag                   = 'Tag'
CAR_ATTRIBUTE_HasCall               = 'HasCall'
CAR_ATTRIBUTE_HasSkylight           = 'HasSkylight'
CAR_ATTRIBUTE_HasBaggage            = 'HasBaggage'
CAR_ATTRIBUTE_HasAerial             = 'HasAerial'
CAR_ATTRIBUTE_HasCrash              = 'HasCrash'
CAR_ATTRIBUTE_HasDanger             = 'HasDanger'
CAR_ATTRIBUTE_HighwayTollVehicles   = 'HighwayTollVehicles'
# 透传项
CAR_ATTRIBUTE_VehicleBrand          = 'VehicleBrand'
CAR_ATTRIBUTE_PlateNo               = 'PlateNo'
# 坐标矩形框项（需特殊处理）
CAR_ATTRIBUTE_ObjectBoundingBox     = 'ObjectBoundingBox'
# 车辆颜色数组（需特殊处理）
CAR_ATTRIBUTE_VehicleColor          = 'VehicleColor'
# 安全带项（需特殊处理）
CAR_ATTRIBUTE_SafetyBelt            = 'SafetyBelt'
CAR_ATTRIBUTE_MainDriver            = 'MainDriver'
CAR_ATTRIBUTE_CoDriver              = 'CoDriver'

#######################################################
# 骑行
#

#######################################################
# 行人
#

class IOESMapping():
    listCarMappableShortText = [
        CAR_ATTRIBUTE_Angle,
        CAR_ATTRIBUTE_VehicleClass,
        CAR_ATTRIBUTE_HasPlate,
        CAR_ATTRIBUTE_PlateClass,
        CAR_ATTRIBUTE_PlateColor,
        CAR_ATTRIBUTE_Sunvisor,
        CAR_ATTRIBUTE_Paper,
        CAR_ATTRIBUTE_Decoration,
        CAR_ATTRIBUTE_Drop,
        CAR_ATTRIBUTE_HasCall,
        CAR_ATTRIBUTE_HasSkylight,
        CAR_ATTRIBUTE_HasBaggage,
        CAR_ATTRIBUTE_HasAerial,
        CAR_ATTRIBUTE_HasCrash,
        CAR_ATTRIBUTE_HasDanger,
    ]
    listCarMappableLongText = [
        CAR_ATTRIBUTE_HighwayTollVehicles,
    ]
    listCarMirrorableShortText = [
        CAR_ATTRIBUTE_PlateNo,
        CAR_ATTRIBUTE_VehicleColorNums,
        CAR_ATTRIBUTE_Tag,
    ]
    listCarMirrorableLongText = [
        CAR_ATTRIBUTE_VehicleBrand,
    ]
    listCarBoxKey = [
        CAR_ATTRIBUTE_ObjectBoundingBox,
    ]
    listCarColorKey = [
        CAR_ATTRIBUTE_VehicleColor,
    ]

    mapCarAttribute2Name = {
        CAR_ATTRIBUTE_Angle: "角度",
        CAR_ATTRIBUTE_VehicleClass: "车辆类型",
        CAR_ATTRIBUTE_VehicleColorNums: "车辆颜色数目",
        CAR_ATTRIBUTE_HasPlate: "车牌",
        CAR_ATTRIBUTE_PlateClass: "车牌种类",
        CAR_ATTRIBUTE_PlateColor: "车牌颜色",
        CAR_ATTRIBUTE_Sunvisor: "遮阳板状态",
        CAR_ATTRIBUTE_Paper: "纸巾盒",
        CAR_ATTRIBUTE_Decoration: "摆饰",
        CAR_ATTRIBUTE_Drop: "挂饰",
        CAR_ATTRIBUTE_Tag: "年检标数量",
        CAR_ATTRIBUTE_HasCall: "打电话状态",
        CAR_ATTRIBUTE_HasSkylight: "天窗",
        CAR_ATTRIBUTE_HasBaggage: "行李架",
        CAR_ATTRIBUTE_HasAerial: "天线",
        CAR_ATTRIBUTE_HasCrash: "是否有撞损",
        CAR_ATTRIBUTE_HasDanger: "是否危化车",
        CAR_ATTRIBUTE_HighwayTollVehicles: "公路收费车型",
        CAR_ATTRIBUTE_VehicleBrand: "车辆品牌",
        CAR_ATTRIBUTE_PlateNo: "车牌号码",
        CAR_ATTRIBUTE_ObjectBoundingBox: "位置",
        CAR_ATTRIBUTE_VehicleColor: "车辆颜色数组",
        CAR_ATTRIBUTE_SafetyBelt: "安全带",
    }

    ThreeStateType = {
        "0": "无",
        "1": "有",
        "-1": "未知",
    }
    ObjectType = {
        TYPE_PERSON: "行人",
        TYPE_CAR: "机动车",
        TYPE_FACE: "人脸",
        TYPE_BIKE: "非机动车",
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
    PlateClassType = {
        "1": "普通蓝牌",
        "2": "普通黑牌",
        "3": "普通黄牌",
        "4": "警车车牌",
        "5": "武警车牌",
        "6": "军队车牌",
        "7": "使馆车牌",
        "8": "港澳车牌",
        "9": "农用车牌",
        "10": "驾校车牌",
        "11": "新能源小车",
        "12": "新能源大车",
        "99": "其他车牌",
        "-1": "未知",
    }
    PlateColorType = {
        "1": "黄",
        "2": "蓝",
        "3": "黑",
        "4": "白",
        "5": "绿",
        "6": "黄绿",
        "7": "渐变绿",
        "-1": "未知",
    }
    VehicleColorType = {
        "1": "黑",
        "2": "蓝",
        "3": "棕",
        "4": "绿",
        "5": "灰",
        "6": "橙",
        "7": "粉",
        "8": "紫",
        "9": "红",
        "10": "银",
        "11": "白",
        "12": "黄",
        "13": "金",
        "-1": "未知",
    }
    BikeClassType = {
        "1": "二轮摩托车",
        "2": "自行车",
        "3": "三轮车",
        "-1": "未知",
    }
    HairStyle = {
        "1" :"长发",
        "2"	:"短发",
        "-1": "未知",
    }
    CoatTexture = {
        "1":	"净色",
        "2":	"间条",
        "3":	"格子",
        "4":	"图案",
        "5":	"拼接",
        "-1":	"未知",
    }
    TrousersTexture = {
        "1"	: "净色",
        "2"	: "间条",
        "3"	: "图案",
        "-1": "未知",
    }
    HighwayTollVehiclesType = {
        "1": "1类客车",
        "2": "2类客车",
        "3": "3类客车",
        "4": "4类客车",
        "5": "1类货车",
        "6": "2类货车",
        "7": "3类货车",
        "8": "4类货车",
        "9": "5类货车",
        "10": "6类货车",
        "11": "1类专业作业车",
        "12": "2类专业作业车",
        "13": "3类专业作业车",
        "14": "4类专业作业车",
        "15": "5类专业作业车",
        "16": "6类专业作业车",
    }

    mapCarMappable2Mapper = {
        CAR_ATTRIBUTE_Angle: AngleType,
        CAR_ATTRIBUTE_VehicleClass: VehicleClassType,
        CAR_ATTRIBUTE_HasPlate: ThreeStateType,
        CAR_ATTRIBUTE_PlateClass: PlateClassType,
        CAR_ATTRIBUTE_PlateColor: PlateColorType,
        CAR_ATTRIBUTE_Sunvisor: ThreeStateType,
        CAR_ATTRIBUTE_Paper: ThreeStateType,
        CAR_ATTRIBUTE_Decoration: ThreeStateType,
        CAR_ATTRIBUTE_Drop: ThreeStateType,
        CAR_ATTRIBUTE_HasCall: ThreeStateType,
        CAR_ATTRIBUTE_HasSkylight: ThreeStateType,
        CAR_ATTRIBUTE_HasBaggage: ThreeStateType,
        CAR_ATTRIBUTE_HasAerial: ThreeStateType,
        CAR_ATTRIBUTE_HasCrash: ThreeStateType,
        CAR_ATTRIBUTE_HasDanger: ThreeStateType,
        CAR_ATTRIBUTE_HighwayTollVehicles: HighwayTollVehiclesType,
    }

if __name__ == '__main__':
    pass