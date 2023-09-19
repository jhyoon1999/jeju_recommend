from src.domain.recommdation.recommendation_schema import New_User_Data
from src.database.models import ItemInfo

import pandas as pd
from sqlalchemy.orm import Session
import json
import requests

def make_recommendation(db:Session, new_user_info: New_User_Data) :
    new_user_id = 'new_user_id'
    
    # Fix here: access 'ratings' using dot notation and call items()
    ratings_items = new_user_info.ratings.items()
    new_user_base = pd.DataFrame(ratings_items, columns=['item', 'label'])
    new_user_base['user'] = new_user_id
    new_user_base = new_user_base[['user', 'item', 'label']]

    # Convert new_user_info to dictionary and remove 'ratings' key
    new_user_info_dict = new_user_info.dict()
    new_user_info_dict.pop('ratings', None)
    new_user_infomation = pd.DataFrame([new_user_info_dict])
    new_user_infomation['user'] = new_user_id

    new_user_base = pd.merge(new_user_base, new_user_infomation, on='user')
    items_info = db.query(ItemInfo).filter(ItemInfo.item.in_(new_user_base['item'].tolist())).all()
    items_data = [item.__dict__ for item in items_info]
    items_data = [{k: v for k, v in item.items() if k != "_sa_instance_state"} for item in items_data]
    items_data = pd.DataFrame(items_data)
    new_user = pd.merge(new_user_base, items_data, on='item', how='left')
    new_user_dict = new_user.to_dict('records')
    
    data_input = {}
    data_input["new_user_dict_list"] = new_user_dict 
    
    url = "https://p7bmzk64bakobv2n2j3m56aonm0niafa.lambda-url.ap-northeast-2.on.aws/recommend/"
    recommended_item = requests.post(url, json=data_input)
    recommended_item = recommended_item.json()   
    return recommended_item

def return_recommendation(db : Session, recommended_item: list) :
    rec_items = db.query(ItemInfo).filter(ItemInfo.item.in_(recommended_item)).all()
    data = [item.__dict__ for item in rec_items]
    data = [{k: v for k, v in item.items() if k != "_sa_instance_state"} for item in data]
    return data
