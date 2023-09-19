import pandas as pd
import tensorflow as tf
import tqdm

#%% Load Data and column information
data = pd.read_excel(r'train_data.xlsx')
data.shape
data.info()
data.head()
data.nunique()

column_info = pd.read_excel(r'column_info.xlsx')
column_info.shape
column_info.head()
column_info.nunique()

target_columns = ['user', 'item', 'label'] + column_info['column_name'].tolist()
print(target_columns)
data = data[target_columns]
data.info()
data.shape

#%% Drop User with less than 2 ratings
drop_user = data['user'].value_counts().reset_index()
drop_user.columns = ['user', 'count']
drop_user['count'].value_counts()
drop_user_id = drop_user[drop_user['count'] < 2]['user'].tolist()
len(drop_user_id)

data = data[~data['user'].isin(drop_user_id)]
data.shape
data.nunique()

#%% Drop Item with less than 2 ratings
drop_item = data['item'].value_counts().reset_index()
drop_item.columns = ['item', 'count']
drop_item['count'].value_counts()

drop_item_id = drop_item[drop_item['count'] < 2]['item'].tolist()
len(drop_item_id)

data = data[~data['item'].isin(drop_item_id)]
data.nunique()

data.to_excel('new_train_data/train_data_new.xlsx', index=False)
#%% Make Explicit Feedback to Implicit Feedback
data['label'] = data['label'].apply(lambda x : 1 if x == 5 else 0)
data['label'].value_counts()

#%%Data Preprocessing
from libreco.data import random_split
from libreco.data import DatasetFeat
from libreco.evaluation import evaluate

train_set, eval_set = random_split(data, test_size= 0.1, seed = 42)
train_set.nunique()

#변수 정보 지정
user_col = list(column_info[column_info['feature1'] == 'user_col']['column_name'])
item_col = list(column_info[column_info['feature1'] == 'item_col']['column_name'])

sparse_col = list(column_info[column_info['feature2'] == 'sparse_col']['column_name'])
dense_col = list(column_info[column_info['feature2'] == 'dense_col']['column_name'])
multi_sparse_1 = list(column_info[column_info['feature2'] == 'multi_sparse_1']['column_name'])
multi_sparse_2 = list(column_info[column_info['feature2'] == 'multi_sparse_2']['column_name'])
multi_sparse_3 = list(column_info[column_info['feature2'] == 'multi_sparse_3']['column_name'])

len(user_col) + len(item_col) == len(sparse_col) + len(dense_col) + len(multi_sparse_1) + len(multi_sparse_2) + len(multi_sparse_3)

train_data, data_info = DatasetFeat.build_trainset(train_data=data,
                                                    user_col= user_col,
                                                    item_col = item_col,
                                                    sparse_col= sparse_col,
                                                    dense_col= dense_col,
                                                    multi_sparse_col= [multi_sparse_1, multi_sparse_2, multi_sparse_3],
                                                    pad_val= ["missing", "missing", "missing"])

#%%check dataset
DatasetFeat.multi_sparse_unique_vals

#%%check data_info
data_info.sparse_col
data_info.dense_col

data_info.user_col
data_info.item_col

data_info.n_items
data_info.n_users

data_info.item2id
data_info.user2id
#%% check train_data
train_data.sparse_interaction.todense()
print(train_data)

#%%Modeling
from libreco.algorithms import DeepFM

metrics = [
        "loss",
        "balanced_accuracy",
        "roc_auc",
        "pr_auc"
    ]


tf.compat.v1.reset_default_graph() # reset the default computational graph

model = DeepFM(
    "ranking",
    data_info,
    loss_type='cross_entropy',
    embed_size=50,
    n_epochs=20,
    lr=1e-4,
    lr_decay=False,
    reg=1e-2,
    batch_size=256,
    use_bn=False,
    dropout_rate=0.2,
    hidden_units=(128, 64, 32, 16),
    tf_sess_config=None,
    multi_sparse_combiner='sqrtn'
)

model.fit(
    train_data,
    neg_sampling=False,
    verbose = 2,
    shuffle=True,
    metrics = metrics
)

#%% Save Model
data_info.save('model_path', model_name = 'DeepFM')
model.save('model_path', model_name = 'DeepFM')









