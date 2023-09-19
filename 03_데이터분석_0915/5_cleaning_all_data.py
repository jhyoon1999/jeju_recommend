import pandas as pd
import numpy as np
import os

#%% Load Data
#1. Load user_features
user_features = pd.read_csv(r'separate_first_clean\user_features.csv', low_memory=False)
user_features.head()
user_features.shape
user_features.info()

#2. Load ratings data
ratings = pd.read_excel(r'separate_first_clean\item_rating_data.xlsx')
ratings.shape
ratings.nunique()

#3. Load item_features
item_features = pd.read_excel(r'sepaeate_second_clean\1_item_features_expanded.xlsx')
item_features.shape
item_features.nunique()

#%% drop data
#1. ratings에는 있지만 item_features에는 없는 spot_id를 드랍한다.
in_item_features = [x for x in ratings['spot_id'].unique() if x in item_features['spot_id'].unique()]
len(in_item_features)
ratings = ratings[ratings['spot_id'].isin(in_item_features)]
ratings.shape
ratings.nunique()

#2. ratings에는 있지만 user_features에 없는 TRAVEL_ID를 드랍한다.
in_user_features = [x for x in ratings['TRAVEL_ID'].unique() if x in user_features['TRAVEL_ID'].unique()] 
len(in_user_features)

ratings = ratings[ratings['TRAVEL_ID'].isin(in_user_features)]
ratings.nunique()
ratings.shape

#3. ratings에 없는 item_features를 드랍한다.
in_ratings = [x for x in item_features['spot_id'].unique() if x in ratings['spot_id'].unique()]
len(in_ratings)
item_features = item_features[item_features['spot_id'].isin(in_ratings)]
item_features.nunique()

#4. ratings에 없는 TRAVEL_ID를 드랍한다.
in_ratings = [x for x in user_features['TRAVEL_ID'].unique() if x in ratings['TRAVEL_ID'].unique()]
len(in_ratings)
user_features = user_features[user_features['TRAVEL_ID'].isin(in_ratings)]
user_features.nunique()


ratings.nunique()
item_features.nunique()
user_features.nunique()

#%% Make new_spot_id
ratings.columns
item_features.columns

#1. 먼저 혹시 실수가 없었는지 확인
item_features_key = list(item_features['spot_id'] + "_" + item_features['VISIT_AREA_NM'])
len(item_features_key)

ratings_key = ratings['spot_id'] + "_" + ratings['VISIT_AREA_NM']
ratings_key = list(ratings_key.drop_duplicates())
len(ratings_key)

in_not_item = [x for x in item_features_key if x not in ratings_key]
len(in_not_item)
in_not_item
in_not_rating = [x for x in ratings_key if x not in item_features_key]
len(in_not_rating)
in_not_rating

#2. new_spot_id를 부여한다.
item_features.info()
item_features.nunique()
item_features_new_id = {original: 'new_spot_' + str(idx) for idx, original in enumerate(item_features['rename'].unique())}
item_features['new_spot_id'] = item_features['rename'].map(item_features_new_id)
item_features.shape
item_features.info()
item_features.nunique()

#3. new_spot_id를 rating에도 부여한핟.
item_features_add_to_rating = item_features[['new_spot_id', 'spot_id']]
ratings = pd.merge(ratings, item_features_add_to_rating, how='left', on='spot_id')
ratings.info()
ratings.nunique()

#%% Save Data
user_features.to_excel(r'cleaning_all/user_features.xlsx', index=False)
ratings.to_excel(r'cleaning_all/ratings.xlsx', index=False)
item_features.to_excel(r'cleaning_all/item_features.xlsx', index=False)






















































































































































































