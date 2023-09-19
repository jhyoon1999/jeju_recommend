from pydantic import BaseModel, conint
from typing import List

class New_User_Dict(BaseModel) :
    user : str
    item : str 
    label : int
    TRAVEL_MISSION_1 : str
    TRAVEL_MISSION_2 : str
    TRAVEL_MISSION_3 : str 
    TRAVEL_MISSION_4 : str
    TRAVEL_MISSION_5 : str
    TRAVEL_MISSION_6 : str 
    TRAVEL_MISSION_7 : str 
    TRAVEL_MISSION_8 : str
    TRAVEL_MISSION_9 : str 
    TRAVEL_MISSION_10 : str 
    TRAVEL_MISSION_11 : str
    TRAVEL_MISSION_12 : str 
    TRAVEL_MISSION_13 : str
    TRAVEL_MISSION_14 : str
    TRAVEL_MISSION_15 : str
    TRAVEL_MISSION_16 : str
    TRAVEL_MISSION_17 : str
    TRAVEL_MISSION_18 : str
    TRAVEL_MISSION_19 : str
    TRAVEL_MISSION_20 : str
    TRAVEL_MISSION_21 : str
    GENDER : str
    AGE_GRP : str 
    TRAVEL_STATUS_ACCOMPANY : str
    TRAVEL_MOTIVE_1 : str 
    TRAVEL_MOTIVE_2 : str
    TRAVEL_MOTIVE_3 : str
    TRAVEL_STYL_1 : str 
    TRAVEL_STYL_3 : str 
    TRAVEL_STYL_6 : str 
    RESIDENCE_TIME_MIN : str
    REVISIT_INTENTION : str 
    RCMDTN_INTENTION : str 
    VISIT_AREA_TYPE_CD_1 : str
    VISIT_AREA_TYPE_CD_2 : str 
    VISIT_AREA_TYPE_CD_3 : str
    VISIT_AREA_TYPE_CD_4 : str
    VISIT_AREA_TYPE_CD_5 : str
    VISIT_AREA_TYPE_CD_6 : str
    VISIT_AREA_TYPE_CD_7 : str
    VISIT_AREA_TYPE_CD_8 : str
    
    class Config :
        schema_extra = {
            "example" : {
                "user": "new_user_id",
                "item": "spot_5",
                "label": 1,
                "TRAVEL_MISSION_1": "\ud638\uce89\uc2a4 \uc5ec\ud589",
                "TRAVEL_MISSION_2": "\uce5c\ud658\uacbd \uc5ec\ud589(\ud50c\ub85c\uae45 \uc5ec\ud589)",
                "TRAVEL_MISSION_3": "missing",
                "TRAVEL_MISSION_4": "missing",
                "TRAVEL_MISSION_5": "missing",
                "TRAVEL_MISSION_6": "missing",
                "TRAVEL_MISSION_7": "missing",
                "TRAVEL_MISSION_8": "missing",
                "TRAVEL_MISSION_9": "missing",
                "TRAVEL_MISSION_10": "missing",
                "TRAVEL_MISSION_11": "missing",
                "TRAVEL_MISSION_12": "missing",
                "TRAVEL_MISSION_13": "missing",
                "TRAVEL_MISSION_14": "missing",
                "TRAVEL_MISSION_15": "missing",
                "TRAVEL_MISSION_16": "missing",
                "TRAVEL_MISSION_17": "missing",
                "TRAVEL_MISSION_18": "missing",
                "TRAVEL_MISSION_19": "missing",
                "TRAVEL_MISSION_20": "missing",
                "TRAVEL_MISSION_21": "missing",
                "GENDER": "\ub0a8",
                "AGE_GRP": "20\ub300",
                "TRAVEL_STATUS_ACCOMPANY": "\ub098\ud640\ub85c \uc5ec\ud589",
                "TRAVEL_MOTIVE_1": "\uc0c8\ub85c\uc6b4 \uacbd\ud5d8 \ucd94\uad6c",
                "TRAVEL_MOTIVE_2": "missing",
                "TRAVEL_MOTIVE_3": "missing",
                "TRAVEL_STYL_1": "\uc790\uc5f0\uc911\uac04\uc120\ud638",
                "TRAVEL_STYL_3": "\uc0c8\ub85c\uc6b4\uc9c0\uc5ed\ub9e4\uc6b0\uc120\ud638",
                "TRAVEL_STYL_6": "\uc798\uc54c\ub824\uc9c0\uc9c0\uc54a\uc740\ubc29\ubb38\uc9c0\uc57d\uac04\uc120\ud638",
                "RESIDENCE_TIME_MIN": "31.42857142857143",
                "REVISIT_INTENTION": "4.571428571428571",
                "RCMDTN_INTENTION": "4.571428571428571",
                "VISIT_AREA_TYPE_CD_1": "\uc5ed\uc0ac/\uc720\uc801/\uc885\uad50 \uc2dc\uc124(\ubb38\ud654\uc7ac, \ubc15\ubb3c\uad00, \ucd2c\uc601\uc9c0, \uc808 \ub4f1)",
                "VISIT_AREA_TYPE_CD_2": "\uc790\uc5f0\uad00\uad11\uc9c0",
                "VISIT_AREA_TYPE_CD_3": "\uccb4\ud5d8 \ud65c\ub3d9 \uad00\uad11\uc9c0",
                "VISIT_AREA_TYPE_CD_4": "missing",
                "VISIT_AREA_TYPE_CD_5": "missing",
                "VISIT_AREA_TYPE_CD_6": "missing",
                "VISIT_AREA_TYPE_CD_7": "missing",
                "VISIT_AREA_TYPE_CD_8": "missing"
        }
    }


class New_User_Dict_List(BaseModel):
    new_user_dict_list : List[New_User_Dict]



















