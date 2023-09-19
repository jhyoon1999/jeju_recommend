from schema import New_User_Dict_List

import pandas as pd
import tensorflow as tf
from libreco.data import DataInfo, DatasetFeat
from libreco.algorithms import DeepFM

def make_recommend(new_user_dict_list : New_User_Dict_List) :
    new_user_dict_list = new_user_dict_list.dict()['new_user_dict_list']
    new_user_df = pd.DataFrame(new_user_dict_list)
    
    tf.compat.v1.reset_default_graph()
    loaded_data_info = DataInfo.load("model_path", model_name='DeepFM')
    train_data,new_data_info = DatasetFeat.merge_trainset(new_user_df, loaded_data_info, merge_behavior=True)
    
    new_model =  DeepFM(
        task = "ranking",
        data_info = new_data_info,
        loss_type='cross_entropy',
        embed_size=50,
        n_epochs=5,
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
        neg_sampling=True,
        shuffle=True
    )
    
    rec_result = new_model.recommend_user(user = "new_user_id", n_rec = 5, filter_consumed = True)
    rec_result = list(rec_result['new_user_id'])
    return rec_result 

















