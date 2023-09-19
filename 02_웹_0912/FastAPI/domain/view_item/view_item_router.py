from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from domain.view_item import view_item_crud, view_item_schema

router = APIRouter(
    prefix="/view_item",
    tags=["view_item"]
)

@router.get("/list", response_model = view_item_schema.ItemList)
def item_random_list(db : Session = Depends(get_db), limit: int = 3):
    item_list = view_item_crud.get_random_item_list(db, limit)
    return view_item_schema.ItemList(item_list = item_list)






































