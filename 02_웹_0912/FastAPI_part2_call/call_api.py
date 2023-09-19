import json
import requests
import pandas as pd

base_url = 'https://bxwzuqauf6jjg4at46bqtygcxa0rsmep.lambda-url.ap-northeast-2.on.aws/'

#%% Home method

response = requests.get(base_url)
print(response.status_code)
print(response.json())


#%% View_Item
view_url = base_url + 'view_item/list/'
params = {'limit' : 3}
response = requests.get(view_url, params=params)
print(response.status_code)
print(response.json()['item_list'])

result_df = pd.DataFrame(response.json()['item_list'])
result_df

#%% Recommend_Item
with open('new_user_info.json', 'r') as file:
    data = json.load(file)

recommend_url = base_url + 'recommend/recommendation/'

response = requests.post(recommend_url, json=data)
response.status_code
response.json()

result_df = pd.DataFrame(response.json())
result_df