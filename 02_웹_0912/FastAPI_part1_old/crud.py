from schema import New_User

import pandas as pd
from libreco.data import DataInfo
from libreco.algorithms import DeepFM
import tensorflow as tf
from libreco.data import DatasetFeat

def make_recommend(new_user_dict : New_User):
    new_user_dict = new_user_dict.dict()
    new_user = pd.DataFrame(new_user_dict)
    new_user = new_user[['user', 'item', 'label', 'TRAVEL_MISSION_1', 'TRAVEL_MISSION_2',
                        'TRAVEL_MISSION_3', 'TRAVEL_MISSION_4', 'TRAVEL_MISSION_5',
                        'TRAVEL_MISSION_6', 'TRAVEL_MISSION_7', 'TRAVEL_MISSION_8',
                        'TRAVEL_MISSION_9', 'TRAVEL_MISSION_10', 'TRAVEL_MISSION_11',
                        'TRAVEL_MISSION_12', 'TRAVEL_MISSION_13', 'TRAVEL_MISSION_14',
                        'TRAVEL_MISSION_15', 'TRAVEL_MISSION_16', 'TRAVEL_MISSION_17',
                        'TRAVEL_MISSION_18', 'TRAVEL_MISSION_19', 'TRAVEL_MISSION_20',
                        'TRAVEL_MISSION_21', 'GENDER', 'AGE_GRP', 'TRAVEL_STATUS_ACCOMPANY',
                        'TRAVEL_MOTIVE_1', 'TRAVEL_MOTIVE_2', 'TRAVEL_MOTIVE_3',
                        'TRAVEL_STYL_1', 'TRAVEL_STYL_3', 'TRAVEL_STYL_6', 'RESIDENCE_TIME_MIN',
                        'REVISIT_INTENTION', 'RCMDTN_INTENTION', 'VISIT_AREA_TYPE_CD_1',
                        'VISIT_AREA_TYPE_CD_2', 'VISIT_AREA_TYPE_CD_3', 'VISIT_AREA_TYPE_CD_4',
                        'VISIT_AREA_TYPE_CD_5', 'VISIT_AREA_TYPE_CD_6', 'VISIT_AREA_TYPE_CD_7',
                        'VISIT_AREA_TYPE_CD_8']]
    new_user.astype({'REVISIT_INTENTION':float,
                    'RCMDTN_INTENTION': float,
                    'RESIDENCE_TIME_MIN' : float})
    
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
