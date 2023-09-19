import pandas as pd
import numpy as np

item_features_not = pd.read_excel(r'separate_first_clean\item_features_not_searched_modify_sixth.xlsx')
item_features_not.shape
item_features_not.info()

item_features_not.dropna(subset=['rename'], inplace=True)
item_features_not.shape
item_features_not.columns
item_features_not.info()
item_features_not.drop(['area_name_record_modify', 'drop', 'drop_reason'], axis=1, inplace=True)
item_features_not.head()
item_features_not.columns = ['spot_id', 'VISIT_AREA_NM', 'rename']

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

item = item_features_not

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
item_research.to_excel(r'separate_first_clean/item_features_not_search_seventh.xlsx', index=False)

#%% 드랍 아이템 합치기
dat1 = pd.read_excel(r'separate_first_clean\item_features_searched_third.xlsx')
dat1.shape
dat1.info()
dat1.nunique()

dat1 = dat1[dat1['drop'] == 1]
dat1.shape
dat1.columns
dat1.info()

dat1 = dat1[["spot_id", "VISIT_AREA_NM", "drop", "사유"]]
dat1.columns = ['spot_id', 'VISIT_AREA_NM', 'drop', 'drop_reason']

dat2 = pd.read_excel(r'separate_first_clean\item_features_not_searched_modify_sixth.xlsx')
dat2.shape
dat2.nunique()
dat2['drop_reason'].value_counts()
dat2 = dat2[dat2['drop_reason'] == "검색"]
dat2.shape
dat2.columns

dat2 = dat2[['spot_id', 'area_name_record', 'drop', 'drop_reason']]
dat2.columns = ['spot_id', 'VISIT_AREA_NM', 'drop', 'drop_reason']

drop_item = pd.concat([dat1, dat2])
drop_item.info()
drop_item.to_excel(r'검색_불가_드랍_목록.xlsx', index=False)

















