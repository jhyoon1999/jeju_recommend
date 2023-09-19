import pandas as pd
import numpy as np
import os

print(os.getcwd())

#%% Load Data
spot_train = pd.read_csv(r'full_data\Train\tn_visit_area_info_방문지정보_D.csv', low_memory=False)
spot_train.head()
spot_train.nunique()
spot_train.info()

spot_valid = pd.read_csv(r'full_data\Validation\tn_visit_area_info_방문지정보_D.csv',low_memory=False)
spot_valid.nunique()

spot = pd.concat([spot_train, spot_valid])
spot.head()
spot.info()
spot.nunique()
spot.shape

#%% 방문지 유형으로 spot 데이터 거르기
code_class = pd.read_csv(r'full_data\Validation\tc_codeb_코드B.csv', low_memory=False)
code_class.head() #'cd_a'로 코드명을 검색해본다.
code_class = code_class[['cd_nm', 'cd_a', 'cd_b']]
code_class.query('cd_a == "VIS"')

target_vis_code = [1,2,3,4,5,6,7,8,13]

spot.columns
spot = spot.query('VISIT_AREA_TYPE_CD in @target_vis_code') #query에서 @는 외부변수 참조를 의미
spot.nunique()
spot['VISIT_AREA_TYPE_CD'].unique()

#%% 중요변수만 남기기
spot.columns
important_variable_list = ['VISIT_AREA_ID', 'TRAVEL_ID', 'VISIT_ORDER', 'VISIT_AREA_NM',
                        'RESIDENCE_TIME_MIN', 'VISIT_AREA_TYPE_CD', 'REVISIT_YN',
                        'VISIT_CHC_REASON_CD','DGSTFN', 'REVISIT_INTENTION',
                        'RCMDTN_INTENTION']
len(important_variable_list)

spot_important = spot[important_variable_list]
spot_important.nunique()

#%% spot_id 부여하기
spot_id_to_VISIT_AREA_NM = {original: 'spot_' + str(idx) for idx, original in enumerate(spot_important['VISIT_AREA_NM'].unique())}
len(spot_id_to_VISIT_AREA_NM)

spot_important['spot_id'] = spot_important['VISIT_AREA_NM'].map(spot_id_to_VISIT_AREA_NM)
change_order_columns = ['spot_id'] + list(spot_important.columns[:-1])
change_order_columns
len(change_order_columns)
spot_important = spot_important[change_order_columns]
spot_important.head()

#spot_id로 그루핑하고 방문지 유형이 몇개씩 존재하는지 확인점
spot_important.groupby('spot_id')['VISIT_AREA_TYPE_CD'].nunique().sort_values(ascending=False)
spot_important.query('spot_id == "spot_69"')
#흠... 이건 나중에 체크해봐야겠는데? 

spot_important.to_excel(r'separate_first_clean/item_rating_data.xlsx', index=False)

#%% 이제 아이템 데이터를 만들 것임
#이를 기반으로 검색이 가능하도록 수정이 가해질 것임

#1. item_feature 데이터를 만든다.
item_features = spot_important[['spot_id', 'VISIT_AREA_NM']]
item_features.drop_duplicates(inplace=True)
item_features.shape

#2. 공간정보를 불러와서 합친다.
spot_geo = pd.read_excel(r'separate_first_clean\spot_geo\spot_geo.xlsx')
spot_geo.shape
spot_geo.head()
spot_geo.nunique()

#3. spot_id와 이름의 조합이 완벽히 일치하는지 확인해본다.
item_features['keys'] = item_features['spot_id'] + '_' + item_features['VISIT_AREA_NM']
spot_geo['keys'] = spot_geo['spot_id'] + '_' + spot_geo['area_name_record']

not_in_features = [x for x in spot_geo['keys'].unique() if x not in item_features['keys'].unique()]
len(not_in_features)
not_in_spot_geo = [x for x in item_features['keys'].unique() if x not in spot_geo['keys'].unique()]
len(not_in_spot_geo)
#오케이 완벽히 일치한다.

#합치기 전에 기준이 아니면서 겹치는 것들은 제외해준다.
spot_geo.drop(['spot_id', 'area_name_record'], axis=1, inplace=True)
spot_geo.columns

item_features_geo = pd.merge(item_features, spot_geo, on='keys', how='inner')
item_features_geo.shape
item_features_geo.info()

#이제 변수를 정리해준다.
item_features_geo.drop(['keys', 'road_address_name'], axis=1, inplace=True)
item_features_geo.shape
item_features_geo.info()
item_features_geo.nunique()

item_features_geo.to_excel(r'separate_first_clean/item_features_geo_first.xlsx', index=False)

#%% 제주도가 아닌 관광지를 삭제한다.
item_features_geo.head()

import numpy as np
def detect_geo_jeju(x):
    address = x['address_name']
    if pd.isna(address) or not address:
        return True
    elif "제주특별자치도" in address:
        return True
    else:
        return False

item_features_geo['geo_jeju'] = item_features_geo.apply(detect_geo_jeju, axis=1)
item_features_geo.query('geo_jeju == True')
item_features_geo.query('geo_jeju == False')
item_features_geo_jeju = item_features_geo.query('geo_jeju == True')
item_features_geo_jeju.shape
item_features_geo_jeju.info()
item_features_geo_jeju.nunique()
item_features_geo_jeju.drop('geo_jeju', axis=1, inplace=True)
item_features_geo_jeju.head()
item_features_geo_jeju.to_excel(r'separate_first_clean/item_features_geo_jeju_second.xlsx', index=False)

#%% 검색된 곳과 그렇지 않은 곳을 분리한다.
item_features_searched = item_features_geo_jeju.dropna()
item_features_searched.shape
item_features_searched.info()

item_features_not_searched = item_features_geo_jeju[item_features_geo_jeju['address_name'].isna()]
item_features_not_searched.shape
item_features_not_searched.info()
item_features_not_searched.to_excel(r'separate_first_clean/item_features_not_searched_third.xlsx', index=False)

#%% 첫번째 내가 작업한 것들을 불러온다.
first_geo_modify = pd.read_excel(r'separate_first_clean\spot_geo\same_place_1.xlsx')
first_geo_modify.shape
first_geo_modify.info()
first_geo_modify.nunique()

not_in_item_features_searched = [x for x in first_geo_modify['spot_id'].unique() if x not in item_features_searched['spot_id'].unique()]
len(not_in_item_features_searched)
not_in_first_geo_modify = [x for x in item_features_searched['spot_id'].unique() if x not in first_geo_modify['spot_id'].unique()]
len(not_in_first_geo_modify)

first_geo_modify.drop(['place_name', 'area_name_record'], axis=1, inplace=True)

item_features_searched = pd.merge(item_features_searched, first_geo_modify, on='spot_id', how='inner')
item_features_searched.shape
item_features_searched.head()
item_features_searched.columns

change_order_columns = ['spot_id', 'address_name', 
                        'x', 'y','place_url','category_name',
                        'place_name','VISIT_AREA_NM',
                        'rename', 'drop', '사유']
item_features_searched = item_features_searched[change_order_columns]
item_features_searched.head()
item_features_searched.shape
item_features_searched.to_excel(r'separate_first_clean/item_features_searched_third.xlsx', index=False)
























































































































































































































































































































































































































