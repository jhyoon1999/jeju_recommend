from pydantic import BaseModel
from typing import Dict

class New_User_Data(BaseModel):
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
    ratings : dict = {}
    
    class Config :
        schema_extra = {
            "example" : {
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
                "ratings": {
                    "spot_5": 1,
                    "spot_10": 0,
                    "spot_20": 1
                }
            }
        }