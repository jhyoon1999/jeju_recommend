import pandas as pd
import numpy as np
import os

#%% load item features
searched = pd.read_excel(r'separate_first_clean\item_features_research_fifth.xlsx')
not_searched = pd.read_excel(r'separate_first_clean\item_features_not_search_seventh.xlsx')

searched.shape
searched.nunique()
searched.info()

not_searched.shape
not_searched.nunique()
not_searched.info()

#%% merge searched and not searched
item_features = pd.concat([searched, not_searched])
item_features.shape
item_features.nunique()
item_features.info()
item_features.to_excel(r'sepaeate_second_clean/0_item_features.xlsx', index=False)

#%% Load empty
no_data = pd.read_excel(r'separate_first_clean\검색_불가_드랍_목록.xlsx')
no_data.shape
no_data.head()

#%% make category columns
item_features = pd.read_excel(r'sepaeate_second_clean/0_item_features.xlsx')
item_features.shape
item_features.head()

category_data = item_features[['spot_id', 'category_name']]
category_data.head()

cateogry_expanded = category_data['category_name'].str.split(' > ', expand=True)
cateogry_expanded.shape
cateogry_expanded.columns =['category_name_1', 'category_name_2', 'category_name_3',
                            'category_name_4', 'category_name_5']

category_data = pd.concat([category_data, cateogry_expanded], axis=1)
category_data.head()
category_data.nunique()
category_data.drop(['category_name'], axis=1, inplace=True)

item_features = pd.merge(item_features, category_data, on='spot_id', how='left')
item_features.shape
item_features.head()

item_features.to_excel(r'sepaeate_second_clean/1_item_features_expanded.xlsx', index=False)























































































































































