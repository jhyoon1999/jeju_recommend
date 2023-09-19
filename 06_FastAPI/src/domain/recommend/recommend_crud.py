import os
print(os.getcwd())
os.chdir(r'd:\(중요)추천시스템_업무\06_FastAPI')

from src.domain.recommend.recommend_schema import New_User_Data, Filter
from src.domain.recommend.recommend_schema import Recommend_Data,Recommend_Data_List
from src.database.models import ItemFeatures

import pandas as pd
from sqlalchemy.orm import Session
import json
import requests

item_select_list_1 = {
    "travel" : '여행',
    "sports" : '스포츠,레저',
    "cafe" : '음식점',
    "service" : '서비스,산업',
    "art" : '문화,예술',
    "market" : '가정,생활',
    "transport" : '교통,수송'
}

item_select_list_2 = {
    "cafe" : '카페',
    "market" : '시장'
}

def make_new_user_data(db : Session, new_user_data : New_User_Data):
    new_user_data_dict = new_user_data.dict()
    return new_user_data_dict

def call_item_info(db : Session, filter : Filter):
    filter_dict = filter.dict()
    item_info_collect = []
    for key, value in filter_dict.items():
        if value == 1 :
            if item_select_list_2.get(key) == None:
                search_keyword = item_select_list_1.get(key)
                item_info_call = db.query(ItemFeatures).filter(ItemFeatures.category_name_1 == search_keyword).all()
                items_data = [item.__dict__ for item in item_info_call]
                items_data = [{k: v for k, v in item.items() if k != "_sa_instance_state"} for item in items_data]
                item_info_collect.extend(items_data)
            
            elif item_select_list_2.get(key) != None :
                search_keyword1 = item_select_list_1.get(key)
                search_keyword2 = item_select_list_2.get(key)
                item_info_call = db.query(ItemFeatures).filter(ItemFeatures.category_name_1 == search_keyword1).filter(ItemFeatures.category_name_2 == search_keyword2).all()
                items_data = [item.__dict__ for item in item_info_call]
                items_data = [{k: v for k, v in item.items() if k != "_sa_instance_state"} for item in items_data]
                item_info_collect.extend(items_data)
    return item_info_collect



def make_recommend_data(new_user_data_dict, item_info_collect):
    item_data = pd.DataFrame(item_info_collect)

    new_user_data = pd.DataFrame(new_user_data_dict, index=[0])
    new_user_data = pd.concat([new_user_data]*len(item_data), ignore_index=True)

    recommend_data = pd.concat([item_data, new_user_data], axis=1)
    recommend_data_dict = recommend_data.to_dict(orient='records')

    recommend_data_dict_pydantic = Recommend_Data_List(recommend_data_list=recommend_data_dict)
    recommend_data_dict_pydantic

    recommend_data_input = recommend_data_dict_pydantic.dict()
    return recommend_data_input




























