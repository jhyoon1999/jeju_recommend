from domain.recommendation.recommendation_schema import New_User_Data
from sqlalchemy.orm import Session
from models import ItemInfo

import pandas as pd
from libreco.data import DataInfo
from libreco.algorithms import DeepFM
import tensorflow as tf
from libreco.data import DatasetFeat

def make_new_user_data(db : Session, new_user_info : New_User_Data) :
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
    return new_user

def make_recommend(new_user : pd.DataFrame) :
    tf.compat.v1.reset_default_graph()
    loaded_data_info = DataInfo.load("model_path", model_name='DeepFM')
    train_data,new_data_info = DatasetFeat.merge_trainset(new_user, loaded_data_info, merge_behavior=True)
    new_model =  DeepFM(
        task = "ranking",
        data_info = new_data_info,
        loss_type='cross_entropy',
        embed_size=50,
        n_epochs=20,
        lr=1e-4,
        lr_decay=False,
        reg=1e-2,
        batch_size=256,
        use_bn=False,
        dropout_rate=0.2,
        hidden_units=(128, 64, 32, 16),
        tf_sess_config=None,
        multi_sparse_combiner='sqrtn'
    )
    new_model.rebuild_model(path = "model_path", model_name = 'DeepFM', full_assign = True)
    new_model.fit(
        train_data,
        neg_sampling=False,
        shuffle=True
    )
    rec_result = new_model.recommend_user(user = "new_user_id", n_rec = 5, filter_consumed = True)
    rec_result = list(rec_result['new_user_id'])
    return rec_result


def return_recommendation(db : Session, rec_result: list) :
    rec_items = db.query(ItemInfo).filter(ItemInfo.item.in_(rec_result)).all()
    data = [item.__dict__ for item in rec_items]
    data = [{k: v for k, v in item.items() if k != "_sa_instance_state"} for item in data]
    return data
