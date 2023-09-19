import pandas as pd
from database import SessionLocal
from models import ItemInfo

session = SessionLocal()

item_info = pd.read_excel(r'cleaned_data\item_info.xlsx')
item_info.nunique()
item_info.info()

session.bulk_insert_mappings(ItemInfo, item_info.to_dict(orient='records'))
session.commit()
session.close()














































