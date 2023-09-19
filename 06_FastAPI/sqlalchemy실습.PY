from src.database.connection import SessionLocal
from src.database.models import ItemFeatures

import pandas as pd

db = SessionLocal()

item = db.query(ItemFeatures).filter(ItemFeatures.category_name_1 == "여행").first()
data = item.__dict__
data = [{k: v for k, v in data.items() if k != "_sa_instance_state"}]
data

#%% Load Data and Make data for train catboost
import pandas as pd
import numpy as np
import json

user_features = pd.read_excel(r'D:\(중요)추천시스템_업무\04_Modeling practice\train_data_catboost\user_features.xlsx')
user_features.columns
user_features.nunique()

item_features = pd.read_excel(r'D:\(중요)추천시스템_업무\04_Modeling practice\train_data_catboost\item_features_target.xlsx')
item_features.columns
item_features.drop(['spot_id', 'VISIT_AREA_NM', 'rename', 'address_name',
                    'category_name', 'place_name', 'place_url', 'x', 'y',
                    'category_name_1','category_name_2','category_name_3', 
                    'category_name_4','category_name_5'], axis=1, inplace=True)
item_features.head()
item_features.nunique()
item_features.shape
item_features.drop_duplicates(inplace=True)
item_features.shape

ratings = pd.read_excel(r'D:\(중요)추천시스템_업무\04_Modeling practice\train_data_catboost\ratings.xlsx')
ratings.columns
ratings.head()
ratings.shape

ratings.nunique()
user_features.nunique()
item_features.nunique()

ratings.shape
user_features.shape
data = pd.merge(ratings, user_features, on='TRAVEL_ID', how='left')
data.info()
data.shape
data.isna().sum().sum()

data.shape
item_features.shape
data = pd.merge(data, item_features, on='new_spot_id', how='left')
data.columns
data.shape
data.isna().sum().sum()

data.drop(['TRAVEL_ID','new_spot_id'], axis=1, inplace=True)
data.shape

#rating의 분포를 그려본다.
import matplotlib.pyplot as plt
plt.hist(data['rating'], bins=10)
plt.show()

first_row = data.iloc[0]
first_row = first_row.to_dict()
with open("exampl.json", 'w') as f:
    json.dump(first_row, f)

