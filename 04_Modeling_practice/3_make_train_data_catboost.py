import pandas as pd
import numpy as np
import os

#%%Load data

#1. item_features 
item_features = pd.read_excel(r'cleaning_all\item_features.xlsx')
item_features.shape
item_features.head()
item_features.nunique()

#2. ratings
ratings = pd.read_excel(r'cleaning_all\ratings.xlsx')
ratings.shape
ratings.head()
ratings.nunique()

#3. user_features
user_features = pd.read_excel(r'cleaning_all\user_features_recleaning.xlsx')
user_features.shape
user_features.head()
user_features.nunique()

#%% 추천할 아이템만 남기자.
item_features.columns
item_features['category_name_1'].value_counts()

#1. 여행
item_part1 = item_features[item_features['category_name_1']=='여행']
item_part1.shape

#2. 스포츠,레저
item_part2 = item_features[item_features['category_name_1']=='스포츠,레저']
item_part2.shape

#3. 음식점_카페
item_part3 = item_features[item_features['category_name_1']=='음식점']
item_part3 = item_part3[item_part3['category_name_2']=='카페']
item_part3.shape

#4. 서비스, 산업
item_part4 = item_features[item_features['category_name_1']=='서비스,산업']
item_part4.shape

#5. 문화, 예술
item_part5 = item_features[item_features['category_name_1']=='문화,예술']
item_part5.shape

#6.가정,생활_시장
item_part6 = item_features[item_features['category_name_1']=='가정,생활'] 
item_part6 = item_part6[item_part6['category_name_2']=='시장']
item_part6.shape

#7. 교통,수송
item_part7 = item_features[item_features['category_name_1']=='교통,수송']
item_part7.shape

item_features_target = pd.concat([item_part1,item_part2,item_part3,item_part4,item_part5,item_part6,item_part7])
item_features_target.shape
item_features_target.head()
item_features_target.nunique()

#%%ratings에서 해당 new_spot_id만 남긴다.
ratings.head()
ratings = ratings[ratings['new_spot_id'].isin(item_features_target['new_spot_id'])]
ratings.shape
ratings.nunique()
ratings.info()

#만족도 점수가 없는 케이스 2개는 드랍한다.
ratings.dropna(subset=['DGSTFN'], inplace=True)
ratings.shape
ratings.info()
ratings.nunique()

#만족도 점수를 만든다.
ratings['rating'] = (ratings['DGSTFN'] + ratings['REVISIT_INTENTION'] + ratings['RCMDTN_INTENTION'])/3
ratings['rating'].max()
ratings['rating'].min()

#만족도 점수의 분포를 그려보자
import matplotlib.pyplot as plt
plt.hist(ratings['rating'], bins=10)
plt.show()

#%% user도 rating에 남은 애들만 남긴다.
user_features = user_features[user_features['TRAVEL_ID'].isin(ratings['TRAVEL_ID'])]
user_features.shape
user_features.nunique()

ratings.nunique()
item_features_target.nunique()
user_features.nunique()

#%% user_cleaning
user_features.columns
user_features.head()
user_features.drop(['TRAVELER_ID', 'TRAVEL_RANGE', 'TRAVEL_COMPANIONS_NUM',
                    'TRAVEL_STYL_2','TRAVEL_STYL_4', 'TRAVEL_STYL_7', 'TRAVEL_STYL_8'],
                axis=1, inplace=True)
user_features.head()
user_features.iloc[:, 0:3].head()

#1. TRAVEL_MISSION에 대한 get_dummies
mission = user_features[['TRAVEL_ID', 'TRAVEL_MISSION_1', 'TRAVEL_MISSION_2', 'TRAVEL_MISSION_3',
                        'TRAVEL_MISSION_4', 'TRAVEL_MISSION_5', 'TRAVEL_MISSION_6',
                        'TRAVEL_MISSION_7', 'TRAVEL_MISSION_8', 'TRAVEL_MISSION_9',
                        'TRAVEL_MISSION_10', 'TRAVEL_MISSION_11', 'TRAVEL_MISSION_12',
                        'TRAVEL_MISSION_13', 'TRAVEL_MISSION_14', 'TRAVEL_MISSION_15',
                        'TRAVEL_MISSION_16', 'TRAVEL_MISSION_17', 'TRAVEL_MISSION_18',
                        'TRAVEL_MISSION_19', 'TRAVEL_MISSION_20', 'TRAVEL_MISSION_21']]
mission.info()

mission_melted = mission.melt(id_vars=['TRAVEL_ID'],
                            value_vars=['TRAVEL_MISSION_1', 'TRAVEL_MISSION_2', 'TRAVEL_MISSION_3',
                                        'TRAVEL_MISSION_4', 'TRAVEL_MISSION_5', 'TRAVEL_MISSION_6',
                                        'TRAVEL_MISSION_7', 'TRAVEL_MISSION_8', 'TRAVEL_MISSION_9',
                                        'TRAVEL_MISSION_10', 'TRAVEL_MISSION_11', 'TRAVEL_MISSION_12',
                                        'TRAVEL_MISSION_13', 'TRAVEL_MISSION_14', 'TRAVEL_MISSION_15',
                                        'TRAVEL_MISSION_16', 'TRAVEL_MISSION_17', 'TRAVEL_MISSION_18',
                                        'TRAVEL_MISSION_19', 'TRAVEL_MISSION_20', 'TRAVEL_MISSION_21'],
                            value_name='TRAVEL_MISSION')
mission_melted.head()
mission_melted.query('TRAVEL_ID == "d_d000296"')
mission_melted.drop(['variable'], axis = 1, inplace=True)
mission_melted.columns = ['TRAVEL_ID', 'TRAVEL_MISSION']
mission_melted.head()
mission_melted.info()
mission_melted['TRAVEL_MISSION'].value_counts()

#missing은 드랍한다.
mission_melted = mission_melted[mission_melted['TRAVEL_MISSION'] != 'missing']
mission_melted['TRAVEL_MISSION'].value_counts()
mission_melted.nunique()
mission_melted.shape

#원핫 인코딩을 실시한다.
mission_dummies = pd.get_dummies(mission_melted, columns=['TRAVEL_MISSION']).groupby('TRAVEL_ID').sum().reset_index()
mission_dummies.head()
mission_dummies.info()
mission_dummies.shape
mission_dummies.nunique()

#user_features에 합친다.
user_features.columns
user_features.drop(['TRAVEL_MISSION_1', 'TRAVEL_MISSION_2', 'TRAVEL_MISSION_3',
                    'TRAVEL_MISSION_4', 'TRAVEL_MISSION_5', 'TRAVEL_MISSION_6',
                    'TRAVEL_MISSION_7', 'TRAVEL_MISSION_8', 'TRAVEL_MISSION_9',
                    'TRAVEL_MISSION_10', 'TRAVEL_MISSION_11', 'TRAVEL_MISSION_12',
                    'TRAVEL_MISSION_13', 'TRAVEL_MISSION_14', 'TRAVEL_MISSION_15',
                    'TRAVEL_MISSION_16', 'TRAVEL_MISSION_17', 'TRAVEL_MISSION_18',
                    'TRAVEL_MISSION_19', 'TRAVEL_MISSION_20', 'TRAVEL_MISSION_21'],
                axis=1, inplace=True)

user_features = pd.merge(user_features, mission_dummies, on='TRAVEL_ID', how='left')
user_features.shape
user_features.info()
user_features.nunique()
user_features.head()

#2. TRAVEL_MOTIVE에 대한 get_dummies
user_features.columns
motive = user_features[['TRAVEL_ID', 'TRAVEL_MOTIVE_1', 'TRAVEL_MOTIVE_2', 'TRAVEL_MOTIVE_3']]

motive_melted = motive.melt(id_vars=['TRAVEL_ID'],
                            value_vars=['TRAVEL_MOTIVE_1', 'TRAVEL_MOTIVE_2', 'TRAVEL_MOTIVE_3'],
                            value_name='TRAVEL_MOTIVE')
motive_melted.drop(['variable'], axis = 1, inplace=True)
motive_melted['TRAVEL_MOTIVE'].value_counts()

motive_melted = motive_melted[motive_melted['TRAVEL_MOTIVE'] != 'missing']
motive_melted['TRAVEL_MOTIVE'].value_counts()

motive_dummies = pd.get_dummies(motive_melted, columns=['TRAVEL_MOTIVE']).groupby('TRAVEL_ID').sum().reset_index()
motive_dummies.head()
motive_dummies.nunique()
motive_dummies.shape

user_features.columns
user_features.drop(['TRAVEL_MOTIVE_1', 'TRAVEL_MOTIVE_2', 'TRAVEL_MOTIVE_3'],
                axis=1, inplace=True)
user_features = pd.merge(user_features, motive_dummies, on='TRAVEL_ID', how='left')
user_features.head()
user_features.info()
user_features.nunique()

#user_features를 저장한다.
user_features.to_excel(r'train_data_catboost/user_features.xlsx', index=False)

#%% item_features
item_features_target.columns
ratings.columns

item_features_target.nunique()
ratings.nunique()
ratings.info()

#1. 평균체류시간
residence_time = ratings[['new_spot_id', 'RESIDENCE_TIME_MIN']]
residence_time = residence_time.groupby('new_spot_id').mean().reset_index()
residence_time.head()
residence_time.info()

#2. 방문선택이유
reason = ratings[['new_spot_id', 'VISIT_CHC_REASON_CD']]
reason['VISIT_CHC_REASON_CD'].value_counts()
reason.info()
reason = reason.astype({'VISIT_CHC_REASON_CD': 'int'})
reason = reason.astype({'VISIT_CHC_REASON_CD': 'str'})
reason.info()

code_class = pd.read_csv(r'D:\(중요)추천시스템_업무\01_추천시스템_0910\full_data\Train\tc_codeb_코드B.csv')
code_class = code_class[['cd_a', 'cd_b', 'cd_nm']]
code_class.head()

target_code_class = code_class[code_class['cd_a'] == 'REN']
target_code_class.head()
target_code_class.info()

target_code_class['cd_b'].unique()
reason['VISIT_CHC_REASON_CD'].unique()

reason = pd.merge(reason, target_code_class, left_on='VISIT_CHC_REASON_CD', right_on='cd_b', how='left')
reason.head()
reason.drop(['cd_a','cd_b', 'VISIT_CHC_REASON_CD'], axis=1, inplace=True)
reason.columns = ['new_spot_id', 'VISIT_CHC_REASON']
reason.head()

reason_dummies = pd.get_dummies(reason, columns=['VISIT_CHC_REASON']).groupby('new_spot_id').sum().reset_index()
reason_dummies.head()

def convert_value(val):
    return 1 if val >= 1 else 0

reason_dummies.iloc[:,1:] = reason_dummies.iloc[:,1:].applymap(convert_value)
reason_dummies.head()
reason_dummies.nunique()

#3. 만족도 평균
satisfaction = ratings[['new_spot_id', 'DGSTFN']]
satisfaction = satisfaction.groupby('new_spot_id').mean().reset_index()
satisfaction.head()
satisfaction.info()

#4. 'REVISIT_INTENTION'
revisit = ratings[['new_spot_id', 'REVISIT_INTENTION']]
revisit = revisit.groupby('new_spot_id').mean().reset_index()
revisit.info()

#5.'RCMDTN_INTENTION'
recommend = ratings[['new_spot_id', 'RCMDTN_INTENTION']]
recommend = recommend.groupby('new_spot_id').mean().reset_index()
recommend.info()

#6. VISIT_AREA_TYPE_CD
visit_type = ratings[['new_spot_id', 'VISIT_AREA_TYPE_CD']]
visit_type['VISIT_AREA_TYPE_CD'].value_counts()
visit_type.info()
visit_type = visit_type.astype({'VISIT_AREA_TYPE_CD': 'str'})
visit_type.head()

code_class.head()

target_code_class = code_class[code_class['cd_a'] == 'VIS']
target_code_class.head()
target_code_class.info()

visit_type = pd.merge(visit_type, target_code_class, left_on='VISIT_AREA_TYPE_CD', right_on='cd_b', how='left')
visit_type.head()
visit_type.drop(['cd_a','cd_b', 'VISIT_AREA_TYPE_CD'], axis=1, inplace=True)
visit_type.columns = ['new_spot_id', 'VISIT_AREA_TYPE_CD']
visit_type.head()
visit_type['VISIT_AREA_TYPE_CD'].value_counts()

visit_type_dummies = pd.get_dummies(visit_type, 
                                    columns=['VISIT_AREA_TYPE_CD']).groupby('new_spot_id').sum().reset_index()
visit_type_dummies.head()
visit_type_dummies.nunique()

def convert_value(val):
    return 1 if val >= 1 else 0

visit_type_dummies.iloc[:,1:] = visit_type_dummies.iloc[:,1:].applymap(convert_value)
visit_type_dummies.head()
visit_type_dummies.nunique()

item_features_target.columns

#combine to item_features_target
item_features_target = pd.merge(item_features_target, residence_time, on='new_spot_id', how='left')
item_features_target.info()

item_features_target = pd.merge(item_features_target, reason_dummies, on='new_spot_id', how='left')
item_features_target.info()

item_features_target = pd.merge(item_features_target, satisfaction, on='new_spot_id', how='left')
item_features_target.info()

item_features_target = pd.merge(item_features_target, revisit, on='new_spot_id', how='left')
item_features_target.info()

item_features_target = pd.merge(item_features_target, recommend, on='new_spot_id', how='left')

item_features_target = pd.merge(item_features_target, visit_type_dummies, on='new_spot_id', how='left')

pd.Series(item_features.columns)
item_features_target.iloc[:,15:].isna().sum()

item_features_target.to_excel(r'train_data_catboost/item_features_target.xlsx', index=False)

#%% ratings도 정리한다.
ratings.columns
ratings = ratings[['TRAVEL_ID', 'new_spot_id', 'rating']]
ratings.to_excel(r'train_data_catboost/ratings.xlsx', index=False)





















































































































































































































































