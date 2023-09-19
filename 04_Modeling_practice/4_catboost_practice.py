#%% Load Data and Make data for train catboost
import pandas as pd
import numpy as np

user_features = pd.read_excel(r'train_data_catboost\user_features.xlsx')
user_features.columns
user_features.nunique()

item_features = pd.read_excel(r'train_data_catboost\item_features_target.xlsx')
item_features.columns
item_features.drop(['spot_id', 'VISIT_AREA_NM', 'rename', 'address_name',
       'category_name', 'place_name', 'place_url', 'x', 'y', 'category_name_2','category_name_3', 'category_name_4',
       'category_name_5'], axis=1, inplace=True)
item_features.head()
item_features.drop_duplicates(inplace=True)
item_features.shape

ratings = pd.read_excel(r'train_data_catboost\ratings.xlsx')
ratings.columns
ratings.head()

ratings.nunique()
user_features.nunique()
item_features.nunique()

ratings.shape
data = pd.merge(ratings, user_features, on='TRAVEL_ID', how='left')
data.info()
data.isna().sum().sum()
data.shape

data = pd.merge(data, item_features, on='new_spot_id', how='left')
data.columns
data.isna().sum().sum()
data.shape

data.drop(['TRAVEL_ID','new_spot_id'], axis=1, inplace=True)
data.shape

data['rating'] = data['rating'].apply(lambda x: 1 if x >= 4.5 else 0)
data['rating'].value_counts()
#%%
import catboost
from catboost import CatBoostClassifier, Pool
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

data.columns
data.shape
X = data.drop(['rating'], axis=1)
y = data['rating']

X_tv, X_test, y_tv, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_tv, y_tv, test_size=0.2, random_state=42)

#load column information
columns_info = pd.read_excel(r'train_data_catboost/data_columns_info.xlsx')
columns_info.head()
columns_info.shape

#index of categorical value
cat_features = columns_info[columns_info['category'] == 1]['index'].tolist()
cat_features

#Make Pool
train_pool = Pool(X_train, y_train, cat_features=cat_features)
train_pool.get_feature_names()  
X_train.iloc[:,train_pool.get_cat_feature_indices()].columns #오케이 제대로 들어감

valid_pool = Pool(X_val, y_val, cat_features=cat_features)
test_pool = Pool(X_test, y_test, cat_features=cat_features)

model = CatBoostClassifier(iterations=500, 
                        learning_rate=0.05, 
                        depth=7, 
                        verbose=5,
                        custom_loss=['AUC', 'Accuracy'],
                        use_best_model=True)
model.fit(train_pool, 
        plot = True,
        verbose = False,
        eval_set = valid_pool)

print(model.get_params())
print(model.best_iteration_)
print('Tree count: ' + str(model.tree_count_))

#%% Overfitting detector
model_with_early_stop = CatBoostClassifier(
    eval_metric='AUC',
    iterations=200,
    random_seed=63,
    learning_rate=0.5,
    early_stopping_rounds=20
)
model_with_early_stop.fit(
    X_train, y_train,
    cat_features=cat_features,
    eval_set=valid_pool,
    verbose=False,
    plot=True
)

print(model_with_early_stop.tree_count_)

#%% Hyperparameter tuning using hyperopt
from hyperopt import hp, fmin, tpe
import numpy as np
from catboost.utils import eval_metric

def hyperopt_objective(params):
    print(params)
    model = CatBoostClassifier(**params, random_seed=42)
    model.fit(train_pool, verbose=0, eval_set=valid_pool)
    y_pred = model.predict_proba(valid_pool)
    return -eval_metric(valid_pool.get_label(), y_pred[:, 1], 'AUC')[0]

space = {
    'learning_rate': hp.uniform('learning_rate', 0.01, 0.1),
    'depth': hp.randint('depth', 3, 10),
    'l2_leaf_reg': hp.uniform('l2_leaf_reg', 1, 10),
    'boosting_type': hp.choice('boosting_type', ['Ordered', 'Plain']),
    'max_ctr_complexity': hp.randint('max_ctr_complexity', 0, 8),
    'iterations': hp.randint('iterations', 100, 1000),  # 예: 100에서 1000 사이의 정수 값
    'od_type': hp.choice('od_type', ['IncToDec', 'Iter'])  # 가능한 od_type 값
}

best = fmin(hyperopt_objective,
            space=space,
            algo=tpe.suggest,
            max_evals=20)

best_params = best.copy()
best_params
best_params['boosting_type'] = 'Plain' if best['boosting_type'] == 1 else 'Ordered'
best_params['od_type'] = 'Iter' if best['od_type'] == 1 else 'IncToDec'
print(best_params)

#%% Modeling using best_params
best_model = CatBoostClassifier(**best_params, random_seed=42)
best_model.fit(train_pool, verbose=5, eval_set=valid_pool)

#%%Evaluate
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

# 예측
y_pred = best_model.predict(test_pool)
print(y_pred)
y_prob = best_model.predict_proba(test_pool)[:, 1]
print(y_prob)

# 성능 지표 계산
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_prob)

# 결과 출력
print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 Score: {f1:.4f}")
print(f"ROC AUC: {roc_auc:.4f}")

#%% Variable importance
# 변수 중요도 얻기
feature_importances = best_model.get_feature_importance()

# 변수 중요도 출력
for score, name in sorted(zip(feature_importances, best_model.feature_names_), reverse=True):
    print(f'{name}: {score:.4f}')

# 변수 중요도 시각화
plt.figure(figsize=(12, 6))
plt.bar(range(len(model.feature_names_)), feature_importances, tick_label=model.feature_names_)
plt.title('Feature Importances')
plt.show()

#%%Cross-Validation
from catboost import cv
print(best_params)

best_params['loss_function'] = 'Logloss'
best_params['custom_loss'] = ['AUC', 'BalancedAccuracy', 'Accuracy', 'Precision', 'Recall', 'F1']

cv_data = cv(
    params = best_params,
    pool = Pool(X, label=y, cat_features=cat_features),
    fold_count=5,
    shuffle=True,
    partition_random_seed=0,
    plot=True,
    stratified=False,
    verbose=False
)

mean_logloss = np.mean(cv_data['test-Logloss-mean'])
mean_auc = np.mean(cv_data['test-AUC-mean'])
mean_accuracy = np.mean(cv_data['test-Accuracy-mean'])
mean_precision = np.mean(cv_data['test-Precision-mean'])
mean_recall = np.mean(cv_data['test-Recall-mean'])
mean_f1 = np.mean(cv_data['test-F1-mean'])
mean_balanced_accuracy = np.mean(cv_data['test-BalancedAccuracy-mean'])

print(f"Average Logloss: {mean_logloss}")
print(f"Average AUC: {mean_auc}")
print(f"Average Accuracy: {mean_accuracy}")
print(f"Average Precision: {mean_precision}")
print(f"Average Recall: {mean_recall}")
print(f"Average F1 Score: {mean_f1}")
print(f"Average Balanced Accuracy: {mean_balanced_accuracy}")

#%% Make Final Model
final_model = CatBoostClassifier(**best_params, random_seed=42)
final_model.fit(X, y, cat_features=cat_features, verbose=False, plot=True)

#%% Save the model
final_model.save_model('final_model.cbm')

#%% Load the model
loaded_model = CatBoostClassifier()
loaded_model.load_model('final_model.cbm')
loaded_model.get_params()