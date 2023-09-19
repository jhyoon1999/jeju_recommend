from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_username = "jhyoon"
db_password = "wjdgks7982"
db_endpoint = "traveldb.cbgkna6w4b1r.ap-northeast-2.rds.amazonaws.com"
db_port = 3306
db_name = "jeju_recommend_test1"

db_url = f"mysql+pymysql://{db_username}:{db_password}@{db_endpoint}:{db_port}/{db_name}?charset=utf8"
engine = create_engine(db_url, echo=False)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()