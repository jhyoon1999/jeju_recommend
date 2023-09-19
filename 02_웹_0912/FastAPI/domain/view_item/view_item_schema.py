from pydantic import BaseModel
from typing import List

class Item(BaseModel) :
    item : str
    name : str
    place_name : str
    address_name : str
    category_name : str
    place_url : str
    x : str
    y : str
    RESIDENCE_TIME_MIN: str
    VISIT_AREA_TYPE_CD_1 : str
    VISIT_AREA_TYPE_CD_2 : str
    VISIT_AREA_TYPE_CD_3 : str
    VISIT_AREA_TYPE_CD_4 : str
    VISIT_AREA_TYPE_CD_5 : str
    VISIT_AREA_TYPE_CD_6 : str
    VISIT_AREA_TYPE_CD_7 : str
    VISIT_AREA_TYPE_CD_8 : str
    REVISIT_INTENTION: str	
    RCMDTN_INTENTION: str

class ItemList(BaseModel) :
    item_list : List[Item] = []





