import pandas as pd
from database import SessionLocal
from models import ItemFeatures, Ratings

session = SessionLocal()

item_info = pd.read_excel(r'train_data_catboost\item_features_target.xlsx')
item_info.nunique()
item_info.info()

item_info.fillna("-",inplace=True)
item_info.shape

session.bulk_insert_mappings(ItemFeatures, item_info.to_dict(orient='records'))
session.commit()
session.close()

session = SessionLocal()

ratings = pd.read_excel(r'train_data_catboost\ratings.xlsx')
ratings.shape
ratings.nunique()
ratings.info()

session.bulk_insert_mappings(Ratings, ratings.to_dict(orient='records'))
session.commit()
session.close()







































