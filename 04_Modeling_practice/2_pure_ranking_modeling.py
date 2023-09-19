import pandas as pd
import numpy as np
import tensorflow as tf
import tqdm

#%%Load Data
ratings = pd.read_excel(r'train_data_pure\ratings.xlsx')
ratings.nunique()
ratings.shape
ratings.head()

ratings['label'].value_counts()

#4점을 기준으로 0과 1로 바꾼다.
def change_explicit_to_implicit(x):
    if x['label'] <= 4:
        return 0
    else:
        return 1

ratings['label'] = ratings.apply(change_explicit_to_implicit, axis=1)
ratings['label'].value_counts()

#%%1. 그냥해보기
from libreco.data import random_split
from libreco.data import DatasetPure
from libreco.evaluation import evaluate

train_set, valid_set = random_split(ratings, test_size= 0.1, seed= 23)
train_set.shape
train_set.nunique()
valid_set.shape

#1. NCF
from libreco.algorithms import NCF

train_data, data_info = DatasetPure.build_trainset(train_set)
valid_data = DatasetPure.build_testset(valid_set)

train_data.labels

metrics = [
        "loss",
        "balanced_accuracy",
        "roc_auc",
        "pr_auc",
        "precision",
        "recall",
        "map",
        "ndcg",
    ]

#Modeling
tf.compat.v1.reset_default_graph() # reset the default computational graph

model = NCF(
    task = 'ranking',
    data_info = data_info,
    embed_size= 50,
    n_epochs = 30,
    lr = 0.001,
    lr_decay=False,
    reg = None,
    batch_size = 256,
    use_bn = True,
    hidden_units=(128, 64, 32, 16)
)

model.fit(train_data = train_data,
        neg_sampling= False,
        verbose = 2,
        shuffle= True,
        metrics= metrics,
        eval_data= valid_data,
        eval_batch_size= 256
        )

evaluation = evaluate(model = model, data = valid_data, 
                    neg_sampling=False, metrics=metrics)
evaluation

#%% 딱 5개까지만 rating을 준 user들 삭제하기
ratings_drop_5 = ratings.copy()
ratings_user_count = ratings_drop_5['user'].value_counts().reset_index()
ratings_user_count.columns = ['user', 'user_count']
ratings_user_count.sort_values(by='user_count', ascending=False)

drop_user = list(ratings_user_count[ratings_user_count['user_count'] < 5]['user'])
len(drop_user)

ratings_drop_5 = ratings_drop_5[ratings_drop_5['user'].isin(drop_user)==False]
ratings_drop_5.nunique()
ratings_drop_5.shape
ratings_drop_5['user'].value_counts().sort_values(ascending=False)

#sparsity_index를 계산해본다.
sparsity_index = 1 - (len(ratings_drop_5) / (len(ratings_drop_5['user'].unique()) * len(ratings_drop_5['item'].unique())))
sparsity_index

from libreco.data import random_split
from libreco.data import DatasetPure
from libreco.evaluation import evaluate

train_set, valid_set = random_split(ratings_drop_5, test_size= 0.1, seed= 23)
train_set.shape
train_set.nunique()
valid_set.shape

train_data, data_info = DatasetPure.build_trainset(train_set)
valid_data = DatasetPure.build_testset(valid_set)

train_data
data_info.data_size

metrics = [
        "loss",
        "balanced_accuracy",
        "roc_auc",
        "pr_auc",
        "precision",
        "recall",
        "map",
        "ndcg",
    ]

#Modeling
tf.compat.v1.reset_default_graph() # reset the default computational graph

model = NCF(
    task = 'ranking',
    data_info = data_info,
    embed_size= 50,
    n_epochs = 30,
    lr = 0.001,
    lr_decay=False,
    reg = None,
    batch_size = 256,
    use_bn = True,
    hidden_units=(128, 64, 32, 16)
)

model.fit(train_data = train_data,
        neg_sampling= False,
        verbose = 2,
        shuffle= True,
        metrics= metrics,
        eval_data= valid_data,
        eval_batch_size= 256
        )

evaluation = evaluate(model = model, data = valid_data, 
                    neg_sampling=False, metrics=metrics)
evaluation

#%% 딱 10개까지만 rating을 준 user들 삭제하기
ratings_drop_10 = ratings.copy()
ratings_user_count = ratings_drop_10['user'].value_counts().reset_index()
ratings_user_count.columns = ['user', 'user_count']
ratings_user_count.sort_values(by='user_count', ascending=False)

drop_user = list(ratings_user_count[ratings_user_count['user_count'] < 10]['user'])
len(drop_user)

ratings_drop_10 = ratings_drop_10[ratings_drop_10['user'].isin(drop_user)==False]
ratings_drop_10.nunique()
ratings_drop_10.shape
ratings_drop_10['user'].value_counts().sort_values(ascending=False)

#sparsity_index를 계산해본다.
sparsity_index = 1 - (len(ratings_drop_10) / (len(ratings_drop_10['user'].unique()) * len(ratings_drop_10['item'].unique())))
sparsity_index

from libreco.data import random_split
from libreco.data import DatasetPure
from libreco.evaluation import evaluate

train_set, valid_set = random_split(ratings_drop_10, test_size= 0.1, seed= 23)

train_set.shape
train_set.nunique()
valid_set.shape

train_data, data_info = DatasetPure.build_trainset(train_set)
valid_data = DatasetPure.build_testset(valid_set)

data_info.data_size

metrics = [
        "loss",
        "balanced_accuracy",
        "roc_auc",
        "pr_auc",
        "precision",
        "recall",
        "map",
        "ndcg",
    ]

#Modeling
tf.compat.v1.reset_default_graph() # reset the default computational graph

model = NCF(
    task = 'ranking',
    data_info = data_info,
    embed_size= 50,
    n_epochs = 30,
    lr = 0.001,
    lr_decay=False,
    reg = None,
    batch_size = 256,
    use_bn = True,
    hidden_units=(128, 64, 32, 16)
)

model.fit(train_data = train_data,
        neg_sampling= False,
        verbose = 2,
        shuffle= True,
        metrics= metrics,
        eval_data= valid_data,
        eval_batch_size= 256
        )

evaluation = evaluate(model = model, data = valid_data, 
                    neg_sampling=False, metrics=metrics)
evaluation