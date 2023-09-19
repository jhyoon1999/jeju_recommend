from src.database.models import ItemInfo

from sqlalchemy.orm import Session
from sqlalchemy import func

#1. 랜덤하게 3개 질문 받아오기
def get_random_item_list(db: Session, limit: int):
    items = db.query(ItemInfo).order_by(func.random()).limit(limit).all()
    data = [item.__dict__ for item in items]
    data = [{k: v for k, v in item.items() if k != "_sa_instance_state"} for item in data]
    return data
