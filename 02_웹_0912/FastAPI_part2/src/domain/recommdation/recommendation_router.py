from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.connection import get_db
from src.domain.recommdation import recommendation_crud, recommendation_schema
from src.domain.view_item import view_item_schema

router = APIRouter(
    prefix = "/recommend",
    tags = ["recommend"]
)

@router.post('/recommendation', response_model = view_item_schema.ItemList)
async def recommendation(db: Session = Depends(get_db), 
                        new_user_info: recommendation_schema.New_User_Data = None):
    recommended_item = recommendation_crud.make_recommendation(db, new_user_info)
    recommended_item_info = recommendation_crud.return_recommendation(db, recommended_item)
    return recommended_item_info


