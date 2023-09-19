#%% Load Data and Make data for train catboost
import pandas as pd
import numpy as np

user_features = pd.read_excel(r'train_data_catboost\user_features.xlsx')
user_features.columns
user_features.nunique()

item_features = pd.read_excel(r'train_data_catboost\item_features_target.xlsx')
item_features.columns
item_features.drop(['spot_id', 'VISIT_AREA_NM', 'rename', 'address_name',
                    'category_name', 'place_name', 'place_url', 'x', 'y', 'category_name_1',
                    'category_name_2','category_name_3', 'category_name_4',
                    'category_name_5'], axis=1, inplace=True)
item_features.head()
item_features.nunique()
item_features.shape
item_features.drop_duplicates(inplace=True)
item_features.shape

ratings = pd.read_excel(r'train_data_catboost\ratings.xlsx')
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

unique_values = {col: data[col].unique().tolist() for col in data.columns}
# 최대 길이 계산
max_len = max(len(lst) for lst in unique_values.values())

# 최대 길이에 맞게 리스트 확장하기
for key, value in unique_values.items():
    unique_values[key] = value + [np.nan] * (max_len - len(value))
    
unique_values_df = pd.DataFrame(unique_values)
unique_values_df.head()
unique_values_df.to_excel(r'train_data_catboost\unique_values.xlsx')

