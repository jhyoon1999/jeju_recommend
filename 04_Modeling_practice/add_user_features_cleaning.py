import pandas as pd
import os
import numpy as np

print(os.getcwd())

#%%Load cleaned user data
user_features = pd.read_excel(r'cleaning_all\user_features.xlsx')
user_features.columns
user_features.query('TRAVEL_ID == "d_d003179"')
user_features.drop(['TRAVEL_MISSION_1',
       'TRAVEL_MISSION_2', 'TRAVEL_MISSION_3', 'TRAVEL_MISSION_4',
       'TRAVEL_MISSION_5', 'TRAVEL_MISSION_6', 'TRAVEL_MISSION_7',
       'TRAVEL_MISSION_8', 'TRAVEL_MISSION_9', 'TRAVEL_MISSION_10',
       'TRAVEL_MISSION_11', 'TRAVEL_MISSION_12', 'TRAVEL_MISSION_13',
       'TRAVEL_MISSION_14', 'TRAVEL_MISSION_15', 'TRAVEL_MISSION_16',
       'TRAVEL_MISSION_17', 'TRAVEL_MISSION_18', 'TRAVEL_MISSION_19',
       'TRAVEL_MISSION_20', 'TRAVEL_MISSION_21'], axis=1, inplace=True)

#%% Load full data
dat1 = pd.read_csv(r'D:\(중요)추천시스템_업무\03_데이터분석_0915\full_data\Train\tn_travel_여행_D.csv')
dat1.shape
dat1.columns
dat1 = dat1[['TRAVEL_ID', 'TRAVEL_MISSION']]
dat1.query('TRAVEL_ID == "d_d003179"')

dat2 = pd.read_csv(r'D:\(중요)추천시스템_업무\03_데이터분석_0915\full_data\Validation\tn_travel_여행_D.csv')
dat2.shape
dat2.columns
dat2 = dat2[['TRAVEL_ID', 'TRAVEL_MISSION']]

dat = pd.concat([dat1, dat2])
dat.shape
dat.head()

dat.query('TRAVEL_ID == "d_d003179"')
dat2.query('TRAVEL_ID == "d_d003179"')

#%% User Features에 통합하자
user_features = pd.merge(user_features, dat, on='TRAVEL_ID', how='left')
user_features.shape
user_features.head()

#%% Mission 변수를 정리하자
mission = user_features[['TRAVEL_ID', 'TRAVEL_MISSION']]
mission.set_index('TRAVEL_ID', inplace=True)
mission.head()

mission = mission['TRAVEL_MISSION'].str.split(';')
mission = mission.explode()
mission = mission.str.strip()
mission = mission[mission != '']
mission = mission.reset_index()
mission.head()
mission.shape

#(1). 각 의미를 알기위해!
code_class = pd.read_csv(r'D:\(중요)추천시스템_업무\03_데이터분석_0915\full_data\Validation\tc_codeb_코드B.csv')
code_class.head()

target_code = code_class[code_class['cd_a'] == 'MIS']
target_code.head() #cd_b하고 cd_nm
target_code = target_code[['cd_b','cd_nm']]
target_code.shape
target_code.head()

#(2). 이제 붙이자.
mission['TRAVEL_MISSION'].unique()
target_code['cd_b'].unique()

len(mission['TRAVEL_MISSION'].unique())
len(target_code['cd_b'].unique())

mission.shape
mission = pd.merge(mission, target_code, left_on= 'TRAVEL_MISSION',right_on='cd_b', how='left')
mission.shape
mission.drop(['cd_b', 'TRAVEL_MISSION'], axis=1, inplace=True)
mission.columns = ['TRAVEL_ID', 'TRAVEL_MISSION']
mission.head()
mission.shape

#중복을 제거한다.
mission.drop_duplicates(inplace=True)
mission.shape
mission.head()

#(3). 이제 옆으로 늘려보자.
mission.shape
mission_copy = mission.copy()
mission_copy['count'] = mission_copy.groupby('TRAVEL_ID').cumcount() + 1
mission_copy.head()

mission_copy_pivot = mission_copy.pivot_table(index='TRAVEL_ID', columns='count', values='TRAVEL_MISSION', aggfunc='first')
mission_copy_pivot.head()

mission_copy_pivot.columns = [f'TRAVEL_MISSION_{i}' for i in mission_copy_pivot.columns]
mission_copy_pivot.head()

mission_copy_pivot.reset_index(inplace=True)
mission_copy_pivot.head()
mission_copy_pivot.tail()

#검증
mission[mission['TRAVEL_ID'] == 'd_d012487']
mission[mission['TRAVEL_ID'] == 'd_d003179']

mission.query('TRAVEL_ID == "d_d003179"')

#NA를 "missing"으로 바꿔주자
mission_copy_pivot.fillna('missing', inplace=True)
mission_copy_pivot.head()

#%%원데이터에 합치고, 저장한다.
user_features.columns
user_features = pd.merge(user_features, mission_copy_pivot, on='TRAVEL_ID', how='left')
user_features.shape
user_features.head()
user_features.columns
user_features.drop(['TRAVEL_MISSION'], axis = 1, inplace=True)
user_features.to_excel(r'cleaning_all/user_features_recleaning.xlsx', index=False)































































































































































































































































































































































































































































































































































































































































































































