import pandas as pd
import os
import numpy as np

item = pd.read_excel(r'separate_first_clean\item_features_searched_third.xlsx')
item.shape
item.info()
item.head()

#%% 첫번째) matching == True 이면서 rename이 비어있는 경우 VISIT_AREA_NM으로 rename을 채워준다.

def rename_VISIT_AREA_NM(x):
    rename = x['rename']
    matching = x['matching']
    
    if matching == True :
        if pd.isna(rename) or not rename:
            return x['VISIT_AREA_NM']
        else : 
            return rename
    else :
        return rename

item['rename'] = item.apply(rename_VISIT_AREA_NM, axis=1)
item.info()

item = item[item['drop'] != 1]
item.shape
item.nunique()

item.to_excel(r'separate_first_clean/item_features_searched_fourth.xlsx', index=False)

#%% 필요없어진 열들은 삭제한다.
item = pd.read_excel(r'separate_first_clean/item_features_searched_fourth.xlsx')
item = item[item['drop'] != 1]
item.info()
item.drop(['drop', '사유', 'matching'], axis=1, inplace=True)
item.columns
item.shape

#다시 카카오지도 검색을 할 것이기 때문에 카카오지도 정보도 삭제한다.
kakao_columns = ['address_name', 'x', 'y', 'place_url', 'category_name','place_name']
item.drop(kakao_columns, axis=1, inplace=True)
item.columns
item.info()

#%% 재탐색
spot_id = []
visit_area_nm = []
rename = []
address_name =[]
category_name = []
place_name = []
place_url = []
x = []
y = []

import requests
import time

for i in range(item.shape[0]) :
    print(i)
    target_dat = item.iloc[i]

    spot_id.append(target_dat['spot_id'])
    visit_area_nm.append(target_dat['VISIT_AREA_NM'])
    rename.append(target_dat['rename'])

    target_keyword = target_dat['rename']

    url = 'https://dapi.kakao.com/v2/local/search/keyword.json'
    rest_api_key = '18052e6cd7e4e3344d3fccdce18499e0'
    header = {'Authorization': 'KakaoAK ' + rest_api_key}
    params = {'query': target_keyword,'size': 15}
    places = requests.get(url, params=params, headers=header).json()['documents']
    len(places)
    
    target_address_name = None 
    target_category_name = None
    target_place_name = None
    target_place_url = None
    target_x = None
    target_y = None

    for place in places :
        if '제주특별자치도' in place['address_name'] :
            if target_keyword == place['place_name'] :
                target_address_name = place['address_name']
                target_category_name = place['category_name']
                target_place_name = place['place_name']
                target_place_url = place['place_url']
                target_x = place['x']
                target_y = place['y']

    if target_place_name is None :
        print("warning")
        print(target_keyword)
        time.sleep(3)
        target_address_name = np.NaN
        target_category_name = np.NaN
        target_place_name = np.NaN
        target_place_url = np.NaN
        target_road_address_name =np.NaN
        target_x = np.NaN
        target_y = np.NaN

    address_name.append(target_address_name)
    category_name.append(target_category_name)
    place_name.append(target_place_name)
    place_url.append(target_place_url)
    x.append(target_x)
    y.append(target_x)

item_research = pd.DataFrame({'spot_id': spot_id,
                            'VISIT_AREA_NM': visit_area_nm,
                            'rename': rename,
                            'address_name': address_name,
                            'category_name': category_name,
                            'place_name': place_name,
                            'place_url': place_url,
                            'x': x,
                            'y': y})
item_research.shape
item_research.info()
item_research.to_excel(r'separate_first_clean/item_features_research_fifth.xlsx', index=False)
















































































































































