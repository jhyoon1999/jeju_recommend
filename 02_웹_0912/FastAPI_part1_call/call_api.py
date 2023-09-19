import pandas as pd

new_user_info = {"TRAVEL_MISSION_1" : "호캉스 여행",
    "TRAVEL_MISSION_2" : "친환경 여행(플로깅 여행)",
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

new_user_id = 'new_user_id'

# Fix here: access 'ratings' using dot notation and call items()
ratings_items = new_user_info['ratings']
ratings_items
new_user_base = pd.DataFrame(ratings_items.items(), columns=['item', 'label'])
new_user_base
new_user_base['user'] = new_user_id
new_user_base = new_user_base[['user', 'item', 'label']]
new_user_base

# Convert new_user_info to dictionary and remove 'ratings' key
new_user_info_dict = new_user_info
new_user_info_dict.pop('ratings', None)
new_user_infomation = pd.DataFrame([new_user_info_dict])
new_user_infomation['user'] = new_user_id

new_user_base = pd.merge(new_user_base, new_user_infomation, on='user')
items_info = db.query(ItemInfo).filter(ItemInfo.item.in_(new_user_base['item'].tolist())).all()
items_data = [item.__dict__ for item in items_info]
items_data = [{k: v for k, v in item.items() if k != "_sa_instance_state"} for item in items_data]
items_data = pd.DataFrame(items_data)
new_user = pd.merge(new_user_base, items_data, on='item', how='left')



new_user = {"user": ["new_user_id", "new_user_id", "new_user_id"], "item": ["spot_5", "spot_10", "spot_20"], "label": [1, 0, 1], "TRAVEL_MISSION_1": ["호캉스 여행", "호캉스 여행", "호캉스 여행"], "TRAVEL_MISSION_2": ["친환경 여행(플로깅 여행)", "친환경 여행(플로깅 여행)", "친환경 여행(플로깅 여행)"], "TRAVEL_MISSION_3": ["missing", "missing", "missing"], "TRAVEL_MISSION_4": ["missing", "missing", "missing"], "TRAVEL_MISSION_5": ["missing", "missing", "missing"], "TRAVEL_MISSION_6": ["missing", "missing", "missing"], "TRAVEL_MISSION_7": ["missing", "missing", "missing"], "TRAVEL_MISSION_8": ["missing", "missing", "missing"], "TRAVEL_MISSION_9": ["missing", "missing", "missing"], "TRAVEL_MISSION_10": ["missing", "missing", "missing"], "TRAVEL_MISSION_11": ["missing", "missing", "missing"], "TRAVEL_MISSION_12": ["missing", "missing", "missing"], "TRAVEL_MISSION_13": ["missing", "missing", "missing"], "TRAVEL_MISSION_14": ["missing", "missing", "missing"], "TRAVEL_MISSION_15": ["missing", "missing", "missing"], "TRAVEL_MISSION_16": ["missing", "missing", "missing"], "TRAVEL_MISSION_17": ["missing", "missing", "missing"], "TRAVEL_MISSION_18": ["missing", "missing", "missing"], "TRAVEL_MISSION_19": ["missing", "missing", "missing"], "TRAVEL_MISSION_20": ["missing", "missing", "missing"], "TRAVEL_MISSION_21": ["missing", "missing", "missing"], "GENDER": ["남", "남", "남"], "AGE_GRP": ["20대", "20대", "20대"], "TRAVEL_STATUS_ACCOMPANY": ["나홀로 여행", "나홀로 여행", "나홀로 여행"], "TRAVEL_MOTIVE_1": ["새로운 경험 추구", "새로운 경험 추구", "새로운 경험 추구"], "TRAVEL_MOTIVE_2": ["missing", "missing", "missing"], "TRAVEL_MOTIVE_3": ["missing", "missing", "missing"], "TRAVEL_STYL_1": ["자연중간선호", "자연중간선호", "자연중간선호"], "TRAVEL_STYL_3": ["새로운지역매우선호", "새로운지역매우선호", "새로운지역매우선호"], "TRAVEL_STYL_6": ["잘알려지지않은방문지약간선호", "잘알려지지않은방문지약간선호", "잘알려지지않은방문지약간선호"], "RESIDENCE_TIME_MIN": ["31.42857142857143", "68.51351351351352", "157.5"], "REVISIT_INTENTION": ["4.571428571428571", "3.72972972972973", "5"], "RCMDTN_INTENTION": ["4.571428571428571", "3.824324324324324", "5"], "VISIT_AREA_TYPE_CD_1": ["역사/유적/종교 시설(문화재, 박물관, 촬영지, 절 등)", "상업지구(거리, 시장, 쇼핑시설)", "산책로, 둘레길 등"], "VISIT_AREA_TYPE_CD_2": ["자연관광지", "테마시설(놀이공원, 워터파크)", "자연관광지"], "VISIT_AREA_TYPE_CD_3": ["체험 활동 관광지", "missing", "missing"], "VISIT_AREA_TYPE_CD_4": ["missing", "missing", "missing"], "VISIT_AREA_TYPE_CD_5": ["missing", "missing", "missing"], "VISIT_AREA_TYPE_CD_6": ["missing", "missing", "missing"], "VISIT_AREA_TYPE_CD_7": ["missing", "missing", "missing"], "VISIT_AREA_TYPE_CD_8": ["missing", "missing", "missing"]}
new_user = pd.DataFrame(new_user)
new_user.head()
new_user.columns
new_user.info()

new_user_dict = new_user.to_dict(orient="records")
len(new_user_dict)

import json

with open('new_user_data.json', 'w') as file:
    json.dump(new_user_dict, file, indent=4)

#%% Call using new_user_dict
import json
import requests

with open('new_user_data.json', 'r') as file:
    data = json.load(file)

len(data)
data[0]

data_input = {}
data_input["new_user_dict_list"] = data
data_input

with open('new_user_data_list.json', 'w') as file:
    json.dump(data_input, file, indent=4)

url = "http://127.0.0.1:8000/recommend/"

response = requests.post(url, json=data_input)

response.status_code
response.json()['new_user_dict_list']

#%% 
with open('new_user_data_list.json', 'r') as file:
    data = json.load(file)

url = "http://127.0.0.1:8000/recommend/"
response = requests.post(url, json=data_input)
response.status_code
response.json()['new_user_dict_list']

#%%
with open('new_user_data_list.json', 'r') as file:
    data = json.load(file)

url = "http://127.0.0.1:8000/recommend/"
response = requests.post(url, json=data_input)
response.status_code
response.json()


#%% check
new_user_df = pd.DataFrame(data_input['new_user_dict_list'])
new_user_df
new_user_df.info()

new_user_df = new_user_df.astype({'REVISIT_INTENTION' : float, 
                                'RCMDTN_INTENTION' : float})

tf.compat.v1.reset_default_graph()
loaded_data_info = DataInfo.load("model_path", model_name='DeepFM')
train_data,new_data_info = DatasetFeat.merge_trainset(new_user_df, loaded_data_info, merge_behavior=True)

new_data_info.dense_col

train_data.dense_values
pd.Series(train_data.labels)

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


#%% Call post method
import json
import requests

with open('new_user_data_list.json', 'r') as file:
    data = json.load(file)
data

url = "https://p7bmzk64bakobv2n2j3m56aonm0niafa.lambda-url.ap-northeast-2.on.aws/"
url = url + "recommend"

response = requests.post(url, json=data)
response.status_code
response.json()


