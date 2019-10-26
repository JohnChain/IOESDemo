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
CAR_ATTRIBUTE_HasPlate              = 'HasPlate'
CAR_ATTRIBUTE_PlateClass            = 'PlateClass'
CAR_ATTRIBUTE_PlateColor            = 'PlateColor'
CAR_ATTRIBUTE_Sunvisor              = 'Sunvisor'
CAR_ATTRIBUTE_Paper                 = 'Paper'
CAR_ATTRIBUTE_Decoration            = 'Decoration'
CAR_ATTRIBUTE_Drop                  = 'Drop'
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
CAR_ATTRIBUTE_VehicleColorNums      = 'VehicleColorNums'
CAR_ATTRIBUTE_Tag                   = 'Tag'
# 坐标矩形框项（需特殊处理）
CAR_ATTRIBUTE_ObjectBoundingBox     = 'ObjectBoundingBox'
# 颜色数组（需特殊处理）
CAR_ATTRIBUTE_VehicleColor          = 'VehicleColor'
# 安全带项（需特殊处理）
CAR_ATTRIBUTE_SafetyBelt            = 'SafetyBelt'
CAR_ATTRIBUTE_MainDriver            = 'MainDriver'
CAR_ATTRIBUTE_CoDriver              = 'CoDriver'
#######################################################
# 骑行
# 需要映射项
BIKE_ATTRIBUTE_BikeClass = "BikeClass"
BIKE_ATTRIBUTE_Gender = "Gender"
BIKE_ATTRIBUTE_Age = "Age"
BIKE_ATTRIBUTE_Angle = "Angle"
BIKE_ATTRIBUTE_HasBackpack = "HasBackpack"
BIKE_ATTRIBUTE_HasGlasses = "HasGlasses"
BIKE_ATTRIBUTE_HasCarrybag = "HasCarrybag"
BIKE_ATTRIBUTE_HasUmbrella = "HasUmbrella"
BIKE_ATTRIBUTE_CoatLength = "CoatLength"

BIKE_ATTRIBUTE_HasPlate = "HasPlate"
BIKE_ATTRIBUTE_HasHelmet = "HasHelmet"
BIKE_ATTRIBUTE_HelmetColor = "HelmetColor"
BIKE_ATTRIBUTE_HasMask = "HasMask"
BIKE_ATTRIBUTE_CoatTexture = "CoatTexture"
# 透传项
BIKE_ATTRIBUTE_CoatColorNums          = 'CoatColorNums'
# 坐标矩形框项（需特殊处理）
BIKE_ATTRIBUTE_ObjectBoundingBox      = 'ObjectBoundingBox'
BIKE_ATTRIBUTE_FaceBoundingBox        = 'FaceBoundingBox'
# 颜色数组（需特殊处理）
BIKE_ATTRIBUTE_CoatColor              = 'CoatColor'
#######################################################
# 行人
# 需要映射项
PERSON_ATTRIBUTE_Gender = "Gender"
PERSON_ATTRIBUTE_Age = "Age"
PERSON_ATTRIBUTE_Angle = "Angle"
PERSON_ATTRIBUTE_HasBackpack = "HasBackpack"
PERSON_ATTRIBUTE_HasGlasses = "HasGlasses"
PERSON_ATTRIBUTE_HasCarrybag = "HasCarrybag"
PERSON_ATTRIBUTE_HasUmbrella = "HasUmbrella"
PERSON_ATTRIBUTE_CoatLength = "CoatLength"
PERSON_ATTRIBUTE_TrousersLength = "TrousersLength"
PERSON_ATTRIBUTE_HasHat = "HasHat"
PERSON_ATTRIBUTE_HasMask = "HasMask"
PERSON_ATTRIBUTE_HairStyle = "HairStyle"
PERSON_ATTRIBUTE_CoatTexture = "CoatTexture"
PERSON_ATTRIBUTE_TrousersTexture = "TrousersTexture"
PERSON_ATTRIBUTE_HasTrolley = "HasTrolley"
PERSON_ATTRIBUTE_HasLuggage = "HasLuggage"
# 透传项
PERSON_ATTRIBUTE_CoatColorNums          = 'CoatColorNums'
PERSON_ATTRIBUTE_TrousersColorNums      = 'TrousersColorNums'
# 坐标矩形框项（需特殊处理）
PERSON_ATTRIBUTE_ObjectBoundingBox      = 'ObjectBoundingBox'
PERSON_ATTRIBUTE_HeadBoundingBox        = 'HeadBoundingBox'
PERSON_ATTRIBUTE_UpperBoundingBox       = 'UpperBoundingBox'
PERSON_ATTRIBUTE_LowerBoundingBox       = 'LowerBoundingBox'
PERSON_ATTRIBUTE_FaceBoundingBox        = 'FaceBoundingBox'
# 颜色数组（需特殊处理）
PERSON_ATTRIBUTE_TrousersColor          = 'TrousersColor'
PERSON_ATTRIBUTE_CoatColor              = 'CoatColor'
#######################################################
# 人脸
# 需要映射项
FACE_ATTRIBUTE_Gender = "Gender"
FACE_ATTRIBUTE_Age = "Age"
FACE_ATTRIBUTE_HasGlasses = "HasGlasses"
FACE_ATTRIBUTE_HasHat = "HasHat"
FACE_ATTRIBUTE_HasMask = "HasMask"
FACE_ATTRIBUTE_HairStyle = "HairStyle"
# 透传项
# 坐标矩形框项（需特殊处理）
FACE_ATTRIBUTE_HeadBoundingBox        = 'HeadBoundingBox'
FACE_ATTRIBUTE_FaceBoundingBox        = 'FaceBoundingBox'
# 颜色数组（需特殊处理）

ThreeStateType = {
    "0": "无",
    "1": "有",
    "-1": "未知",
}
ObjectType = {
    TYPE_FACE: "人脸",
    TYPE_BIKE: "非机动车",
    TYPE_PERSON: "行人",
    TYPE_CAR: "机动车",
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

class IOESBikeMapping():
    listMappableShortText = [
        BIKE_ATTRIBUTE_BikeClass,
        BIKE_ATTRIBUTE_Gender,
        BIKE_ATTRIBUTE_Age,
        BIKE_ATTRIBUTE_Angle,
        BIKE_ATTRIBUTE_HasBackpack,
        BIKE_ATTRIBUTE_HasGlasses,
        BIKE_ATTRIBUTE_HasCarrybag,
        BIKE_ATTRIBUTE_HasUmbrella,
        BIKE_ATTRIBUTE_CoatLength,
        BIKE_ATTRIBUTE_HasPlate,
        BIKE_ATTRIBUTE_HasHelmet,
        BIKE_ATTRIBUTE_HelmetColor,
        BIKE_ATTRIBUTE_HasMask,
        BIKE_ATTRIBUTE_CoatTexture,
    ]
    listMappableLongText = []
    listMirrorableShortText = [
        BIKE_ATTRIBUTE_CoatColorNums
    ]
    listMirrorableLongText = []
    listBoxKey = [
        BIKE_ATTRIBUTE_ObjectBoundingBox,
        BIKE_ATTRIBUTE_FaceBoundingBox,
    ]
    listColorKey = [
        BIKE_ATTRIBUTE_CoatColor
    ]
    mapAttribute2Name = {
        BIKE_ATTRIBUTE_BikeClass: "骑行类型",
        BIKE_ATTRIBUTE_Gender: "性别",
        BIKE_ATTRIBUTE_Age: "年龄",
        BIKE_ATTRIBUTE_Angle: "角度",
        BIKE_ATTRIBUTE_HasBackpack: "背包",
        BIKE_ATTRIBUTE_HasGlasses: "眼镜",
        BIKE_ATTRIBUTE_HasCarrybag: "手提包",
        BIKE_ATTRIBUTE_HasUmbrella: "打伞",
        BIKE_ATTRIBUTE_CoatLength: "上衣类型",
        BIKE_ATTRIBUTE_HasPlate: "挂车牌",
        BIKE_ATTRIBUTE_HasHelmet: "戴头盔",
        BIKE_ATTRIBUTE_HelmetColor: "头盔颜色",
        BIKE_ATTRIBUTE_HasMask: "口罩",
        BIKE_ATTRIBUTE_CoatTexture: "上身衣着款式",
        BIKE_ATTRIBUTE_ObjectBoundingBox: "位置",
        BIKE_ATTRIBUTE_FaceBoundingBox: "面部位置",
        BIKE_ATTRIBUTE_CoatColorNums: "上身颜色数目",
        BIKE_ATTRIBUTE_CoatColor: "上衣颜色数组",
    }
    mapMappable2Mapper = {
        BIKE_ATTRIBUTE_BikeClass: BikeClassType,
        BIKE_ATTRIBUTE_Gender: GenderType,
        BIKE_ATTRIBUTE_Age: AgeType,
        BIKE_ATTRIBUTE_Angle: AngleType,
        BIKE_ATTRIBUTE_HasBackpack: ThreeStateType,
        BIKE_ATTRIBUTE_HasGlasses: ThreeStateType,
        BIKE_ATTRIBUTE_HasCarrybag: ThreeStateType,
        BIKE_ATTRIBUTE_HasUmbrella: ThreeStateType,
        BIKE_ATTRIBUTE_CoatLength: CoatType,
        BIKE_ATTRIBUTE_HasPlate: ThreeStateType,
        BIKE_ATTRIBUTE_HasHelmet: ThreeStateType,
        BIKE_ATTRIBUTE_HelmetColor: ObjectColorType,
        BIKE_ATTRIBUTE_HasMask: ThreeStateType,
        BIKE_ATTRIBUTE_CoatTexture: CoatTexture,
        # 特殊映射(如二级内容)
        BIKE_ATTRIBUTE_CoatColor: ObjectColorType,
    }
class IOESPersonMapping():
    listMappableShortText = [
        PERSON_ATTRIBUTE_Gender,
        PERSON_ATTRIBUTE_Age,
        PERSON_ATTRIBUTE_Angle,
        PERSON_ATTRIBUTE_HasBackpack,
        PERSON_ATTRIBUTE_HasGlasses,
        PERSON_ATTRIBUTE_HasCarrybag,
        PERSON_ATTRIBUTE_HasUmbrella,
        PERSON_ATTRIBUTE_CoatLength,
        PERSON_ATTRIBUTE_TrousersLength,
        PERSON_ATTRIBUTE_HasHat,
        PERSON_ATTRIBUTE_HasMask,
        PERSON_ATTRIBUTE_HairStyle,
        PERSON_ATTRIBUTE_CoatTexture,
        PERSON_ATTRIBUTE_TrousersTexture,
        PERSON_ATTRIBUTE_HasTrolley,
        PERSON_ATTRIBUTE_HasLuggage,
    ]
    listMappableLongText = []
    listMirrorableShortText = [
        PERSON_ATTRIBUTE_CoatColorNums, 
        PERSON_ATTRIBUTE_TrousersColorNums,
    ]
    listMirrorableLongText = []
    listBoxKey = [
        PERSON_ATTRIBUTE_ObjectBoundingBox,
        PERSON_ATTRIBUTE_HeadBoundingBox,
        PERSON_ATTRIBUTE_UpperBoundingBox,
        PERSON_ATTRIBUTE_LowerBoundingBox,
        PERSON_ATTRIBUTE_FaceBoundingBox,
    ]
    listColorKey = [
        PERSON_ATTRIBUTE_TrousersColor,
        PERSON_ATTRIBUTE_CoatColor,
    ]
    mapAttribute2Name = {
        PERSON_ATTRIBUTE_Gender: "性别",
        PERSON_ATTRIBUTE_Age: "年龄",
        PERSON_ATTRIBUTE_Angle: "角度",
        PERSON_ATTRIBUTE_HasBackpack: "背包",
        PERSON_ATTRIBUTE_HasGlasses: "眼镜",
        PERSON_ATTRIBUTE_HasCarrybag: "手提包",
        PERSON_ATTRIBUTE_HasUmbrella: "打伞",
        PERSON_ATTRIBUTE_CoatLength: "上衣类型",
        PERSON_ATTRIBUTE_TrousersLength: "下身类型",
        PERSON_ATTRIBUTE_HasHat: "帽子",
        PERSON_ATTRIBUTE_HasMask: "口罩",
        PERSON_ATTRIBUTE_HairStyle: "发型",
        PERSON_ATTRIBUTE_CoatTexture: "上身衣着款式",
        PERSON_ATTRIBUTE_TrousersTexture: "下身衣着款式",
        PERSON_ATTRIBUTE_HasTrolley: "手推车",
        PERSON_ATTRIBUTE_HasLuggage: "行李箱",

        PERSON_ATTRIBUTE_CoatColorNums: "上衣颜色数目",
        PERSON_ATTRIBUTE_TrousersColorNums: "下身颜色数目",

        PERSON_ATTRIBUTE_ObjectBoundingBox: "位置",
        PERSON_ATTRIBUTE_HeadBoundingBox: "头部位置",
        PERSON_ATTRIBUTE_UpperBoundingBox: "上半身位置",
        PERSON_ATTRIBUTE_LowerBoundingBox: "下半身位置",
        PERSON_ATTRIBUTE_FaceBoundingBox: "面部位置",

        PERSON_ATTRIBUTE_TrousersColor: "下身颜色数组",
        PERSON_ATTRIBUTE_CoatColor: "上衣颜色数组",
    }
    mapMappable2Mapper = {
        PERSON_ATTRIBUTE_Gender: GenderType,
        PERSON_ATTRIBUTE_Age: AgeType,
        PERSON_ATTRIBUTE_Angle: AngleType,
        PERSON_ATTRIBUTE_HasBackpack: ThreeStateType,
        PERSON_ATTRIBUTE_HasGlasses: ThreeStateType,
        PERSON_ATTRIBUTE_HasCarrybag: ThreeStateType,
        PERSON_ATTRIBUTE_HasUmbrella: ThreeStateType,
        PERSON_ATTRIBUTE_CoatLength: CoatType,
        PERSON_ATTRIBUTE_TrousersLength: TrousersType,
        PERSON_ATTRIBUTE_HasHat: ThreeStateType,
        PERSON_ATTRIBUTE_HasMask: ThreeStateType,
        PERSON_ATTRIBUTE_HairStyle: HairStyle,
        PERSON_ATTRIBUTE_CoatTexture: CoatTexture,
        PERSON_ATTRIBUTE_TrousersTexture: TrousersTexture,
        PERSON_ATTRIBUTE_HasTrolley: ThreeStateType,
        PERSON_ATTRIBUTE_HasLuggage: ThreeStateType,

        # 特殊映射(如二级内容)
        PERSON_ATTRIBUTE_TrousersColor: ObjectColorType,
        PERSON_ATTRIBUTE_CoatColor: ObjectColorType,
    }
class IOESFaceMapping():
    listMappableShortText = [
        FACE_ATTRIBUTE_Gender,
        FACE_ATTRIBUTE_Age,
        FACE_ATTRIBUTE_HasGlasses,
        FACE_ATTRIBUTE_HasHat,
        FACE_ATTRIBUTE_HasMask,
        FACE_ATTRIBUTE_HairStyle,

    ]
    listMappableLongText = []
    listMirrorableShortText = []
    listMirrorableLongText = []
    listBoxKey = [
        PERSON_ATTRIBUTE_HeadBoundingBox,
        PERSON_ATTRIBUTE_FaceBoundingBox,
    ]
    listColorKey = []
    mapAttribute2Name = {
        PERSON_ATTRIBUTE_Gender: "性别",
        PERSON_ATTRIBUTE_Age: "年龄",
        PERSON_ATTRIBUTE_HasGlasses: "眼镜",
        PERSON_ATTRIBUTE_HasHat: "帽子",
        PERSON_ATTRIBUTE_HasMask: "口罩",
        PERSON_ATTRIBUTE_HairStyle: "发型",

        PERSON_ATTRIBUTE_HeadBoundingBox: "头部位置",
        PERSON_ATTRIBUTE_FaceBoundingBox: "面部位置",
    }
    mapMappable2Mapper = {
        PERSON_ATTRIBUTE_Gender: GenderType,
        PERSON_ATTRIBUTE_Age: AgeType,
        PERSON_ATTRIBUTE_HasGlasses: ThreeStateType,
        PERSON_ATTRIBUTE_HasHat: ThreeStateType,
        PERSON_ATTRIBUTE_HasMask: ThreeStateType,
        PERSON_ATTRIBUTE_HairStyle: HairStyle,
        # 特殊映射(如二级内容)
    }
class IOESCarMapping():
    listMappableShortText = [
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
    listMappableLongText = [
        CAR_ATTRIBUTE_HighwayTollVehicles,
    ]
    listMirrorableShortText = [
        CAR_ATTRIBUTE_PlateNo,
        CAR_ATTRIBUTE_VehicleColorNums,
        CAR_ATTRIBUTE_Tag,
    ]
    listMirrorableLongText = [
        CAR_ATTRIBUTE_VehicleBrand,
    ]
    listBoxKey = [
        CAR_ATTRIBUTE_ObjectBoundingBox,
    ]
    listColorKey = [
        CAR_ATTRIBUTE_VehicleColor,
    ]

    mapAttribute2Name = {
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
        CAR_ATTRIBUTE_HighwayTollVehicles: "收费车型",
        CAR_ATTRIBUTE_VehicleBrand: "车辆品牌",
        CAR_ATTRIBUTE_PlateNo: "车牌号码",
        CAR_ATTRIBUTE_ObjectBoundingBox: "位置",
        CAR_ATTRIBUTE_VehicleColor: "车辆颜色数组",
        CAR_ATTRIBUTE_SafetyBelt: "安全带",
    }

    mapMappable2Mapper = {
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
        
        # 特殊映射(如二级内容)
        CAR_ATTRIBUTE_VehicleColor: VehicleColorType,
        CAR_ATTRIBUTE_SafetyBelt: ThreeStateType,
    }

if __name__ == '__main__':
    carMapping = IOESCarMapping()
    PersonMapping = IOESPersonMapping()
    BikeMapping = IOESBikeMapping()
    print("===== Car =====")
    for (key,value) in carMapping.mapAttribute2Name.items(): 
        print("%s \t\t\t %s" %(key, value))
    
    print("===== Person =====")
    for (key,value) in PersonMapping.mapAttribute2Name.items(): 
        print("%s \t\t\t %s" %(key, value))

    print("===== Bike =====")
    for (key,value) in BikeMapping.mapAttribute2Name.items(): 
        print("%s \t\t\t %s" %(key, value))