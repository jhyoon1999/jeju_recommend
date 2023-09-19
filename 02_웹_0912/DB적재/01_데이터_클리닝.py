import pandas as pd
import numpy as np

data = pd.read_excel(r'new_train_data\train_data.xlsx')
data.shape
data.nunique()

item_features = pd.read_csv(r'이전작업데이터\spot_searching_need\item_features.csv')
item_features.shape
item_features.nunique()

item_features2 = pd.read_csv(r'이전작업데이터\train_data\item_features.csv')
item_features2.shape
item_features2.nunique()


not_in_data = [x for x in item_features2['new_spot_id'].unique() if x not in data['item'].unique()]
len(not_in_data)
not_in_item_features2 = [x for x in data['item'].unique() if x not in item_features2['new_spot_id'].unique()]
len(not_in_item_features2)

#%%Make item_information
item_info = item_features2[['new_spot_id', 'rename', 'RESIDENCE_TIME_MIN', 'VISIT_AREA_TYPE_CD_1',
       'VISIT_AREA_TYPE_CD_2', 'VISIT_AREA_TYPE_CD_3', 'VISIT_AREA_TYPE_CD_4',
       'VISIT_AREA_TYPE_CD_5', 'VISIT_AREA_TYPE_CD_6', 'VISIT_AREA_TYPE_CD_7',
       'VISIT_AREA_TYPE_CD_8', 'REVISIT_INTENTION', 'RCMDTN_INTENTION']]

item_info.nunique()
item_info.columns = ['item', 'name', 'RESIDENCE_TIME_MIN', 'VISIT_AREA_TYPE_CD_1',
       'VISIT_AREA_TYPE_CD_2', 'VISIT_AREA_TYPE_CD_3', 'VISIT_AREA_TYPE_CD_4',
       'VISIT_AREA_TYPE_CD_5', 'VISIT_AREA_TYPE_CD_6', 'VISIT_AREA_TYPE_CD_7',
       'VISIT_AREA_TYPE_CD_8', 'REVISIT_INTENTION', 'RCMDTN_INTENTION']
item_info.head()

place_info = pd.read_excel(r'이전작업데이터\spot_searching_need\same_place_2.xlsx')
place_info.shape
place_info.nunique()

place_id = [x for x in place_info['new_spot_id'].unique() if x in item_info['item'].unique()]
len(place_id)

place_info = place_info[place_info['new_spot_id'].isin(place_id)]
place_info.shape
place_info.nunique()
place_info.info()

place_info['com'] = place_info['new_spot_id'] + '_' + place_info['rename']
item_info['com'] = item_info['item'] + '_' + item_info['name']

not_in_item_info = [x for x in place_info['com'].unique() if x not in item_info['com'].unique()]
len(not_in_item_info)
not_in_place_info = [x for x in item_info['com'].unique() if x not in place_info['com'].unique()]
len(not_in_place_info)

item_info.drop('com', axis=1, inplace=True)
place_info.drop(['com', 'drop', 'road_address_name'], axis=1, inplace=True)

item_info.info()
place_info.info()

place_info.columns = ['item', 'place_name', 'name', 'address_name', 'category_name',
                    'place_url', 'x', 'y']
place_info.nunique()

item_info = pd.merge(item_info, place_info, on=['item', 'name'], how='inner')
item_info.shape
item_info.head()
item_info.info()

item_info.columns
item_info_columns_order = ['item', 'name', 'place_name', 'address_name', 'category_name', 'place_url', 'x', 'y',
                        'RESIDENCE_TIME_MIN', 'VISIT_AREA_TYPE_CD_1',
                        'VISIT_AREA_TYPE_CD_2', 'VISIT_AREA_TYPE_CD_3', 'VISIT_AREA_TYPE_CD_4',
                        'VISIT_AREA_TYPE_CD_5', 'VISIT_AREA_TYPE_CD_6', 'VISIT_AREA_TYPE_CD_7',
                        'VISIT_AREA_TYPE_CD_8', 'REVISIT_INTENTION', 'RCMDTN_INTENTION']
len(item_info_columns_order)

item_info = item_info[item_info_columns_order]
item_info.info()
item_info.to_excel(r'new_train_data/item_info.xlsx', index=False)

#%%new_train_data에 맞추기
import pandas as pd

item_info = pd.read_excel(r'new_train_data\item_info.xlsx')
train_data = pd.read_excel(r'new_train_data\train_data.xlsx')
new_train_data = pd.read_excel(r'new_train_data\train_data_new.xlsx')

item_info.nunique()
train_data.nunique()
new_train_data.nunique()

item_info = item_info[item_info['item'].isin(new_train_data['item'].unique())]
item_info.nunique()
item_info.info()

item_info.to_excel(r'cleaned_data/item_info.xlsx', index=False)












