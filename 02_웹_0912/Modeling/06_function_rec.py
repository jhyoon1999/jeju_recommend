from libreco.data import DataInfo
from libreco.algorithms import DeepFM
import pandas as pd

loaded_data_info = DataInfo.load("model_path", model_name='DeepFM')
loaded_model = DeepFM.load("model_path", model_name='DeepFM', data_info=loaded_data_info)

#%% New_user_information
new_user_id = 'new_user_id'
new_user_info = {
    "TRAVEL_MISSION_1" : '호캉스 여행',
    'TRAVEL_MISSION_2' : "친환경 여행(플로깅 여행)",
    "TRAVEL_MISSION_3" : "missing",
    "TRAVEL_MISSION_4" : "missing",
    "TRAVEL_MISSION_5" : "missing",
    "TRAVEL_MISSION_6" : "missing",
    "TRAVEL_MISSION_7" : "missing",
    "TRAVEL_MISSION_8" : "missing",
    "TRAVEL_MISSION_9" : "missing",
    "TRAVEL_MISSION_10" : "missing",
    "TRAVEL_MISSION_11" : "missing",
    "TRAVEL_MISSION_12" : "missing",
    "TRAVEL_MISSION_13" : "missing",
    "TRAVEL_MISSION_14" : "missing",
    "TRAVEL_MISSION_15" : "missing",
    "TRAVEL_MISSION_16" : "missing",
    "TRAVEL_MISSION_17" : "missing",
    "TRAVEL_MISSION_18" : "missing",
    "TRAVEL_MISSION_19" : "missing",
    "TRAVEL_MISSION_20" : "missing",
    "TRAVEL_MISSION_21" : "missing",
    "GENDER" : "남",
    "AGE_GRP" : "20대",
    "TRAVEL_STATUS_ACCOMPANY" : "나홀로 여행",
    "TRAVEL_MOTIVE_1" : "새로운 경험 추구",
    "TRAVEL_MOTIVE_2" : "missing",
    "TRAVEL_MOTIVE_3" : "missing",
    "TRAVEL_STYL_1" : "자연중간선호",
    "TRAVEL_STYL_3" : "새로운지역매우선호",
    "TRAVEL_STYL_6" : "잘알려지지않은방문지약간선호",
    "ratings" : {"spot_5" : 1,  "spot_10" : 0, "spot_20" : 1}
}

new_user_ratings = {
    "spot_5" : 1,
    "spot_10" : 0,
    "spot_20" : 1
}

#%% Make new_user_info to DataFrame
new_user_rating_dat = pd.DataFrame(list(new_user_ratings.items()), columns = ['item', 'label'])
new_user_rating_dat['user'] = new_user_id
new_user_rating_dat = new_user_rating_dat[['user', 'item', 'label']]

new_user_info_dat = pd.DataFrame([new_user_info])
new_user_info_dat['user'] = new_user_id

new_user_dat = pd.merge(new_user_rating_dat, new_user_info_dat, on='user', how = 'left')
new_user_dat.head()

item_info = pd.read_excel(r'new_train_data\train_data_new.xlsx')
item_info = item_info[['item']+loaded_data_info.item_col]
item_info.head()
item_info.shape
item_info.nunique()
item_info.drop_duplicates(inplace=True)
item_info.shape

new_user_dat = pd.merge(new_user_dat, item_info, on='item', how = 'left')
new_user_dat.head()
new_user_dat.shape
new_user_dat.info()

#%% Merge new_user_dat in datainfo for retraining
from libreco.data import DatasetFeat
train_data,new_data_info = DatasetFeat.merge_trainset(new_user_dat, loaded_data_info, merge_behavior=True)

train_data.sparse_interaction.shape
train_data.labels
train_data

new_data_info.min_max_rating
new_data_info.sparse_col
new_data_info.user2id['new_user_id']
new_data_info.n_users


#%% Retrain Model
import tensorflow as tf
tf.compat.v1.reset_default_graph()  # need to reset graph in TensorFlow1

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































































































