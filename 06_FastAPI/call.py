import json
import requests
import pandas as pd

url = 'http://127.0.0.1:8000'

response = requests.get(url)
print(response.status_code)
print(response.json())

recommend_url = url + '/recommend/recommend'
with open('user_example.json', 'r') as f:
    user_example = json.load(f)

user_example
response = requests.post(recommend_url, json=user_example)
response.status_code
response.json()



item = pd.read_excel(r'train_data_catboost\item_features_target.xlsx')
item.head()
item['category_name_1'].unique()









