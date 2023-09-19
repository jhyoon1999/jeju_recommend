import pandas as pd

#%%Load data

#1. item_features 
item_features = pd.read_excel(r'cleaning_all\item_features.xlsx')
item_features.shape
item_features.head()

#2. ratings
ratings = pd.read_excel(r'cleaning_all\ratings.xlsx')
ratings.shape
ratings.head()

#3. user_features
user_features = pd.read_excel(r'cleaning_all\user_features.xlsx')
user_features.shape
user_features.head()

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

#%% 필요한 정보들만 남긴다.
ratings.columns
ratings = ratings[['new_spot_id','TRAVEL_ID','rating']]
ratings.columns = ['item', 'user', 'label']
ratings.head()

#librecommender는 자동으로 user, item, label 순으로 데이터를 읽어들이므로 순서를 바꾼다.
ratings = ratings[['user', 'item', 'label']]
ratings.head()

#%% User 들이 몇개씩 rating을 했는지 카운트 해보자
ratings_user_count = ratings['user'].value_counts().reset_index()
ratings_user_count.columns = ['user', 'count']

plt.hist(ratings_user_count['count'], bins=10)
plt.show()

ratings_user_count['count'].value_counts()

#%% Sparsity index를 계산해보자
sparsity = 1 - (len(ratings) / (len(ratings['user'].unique()) * len(ratings['item'].unique())))
sparsity

ratings.to_excel('train_data_pure/ratings.xlsx', index=False)












































































































































































































