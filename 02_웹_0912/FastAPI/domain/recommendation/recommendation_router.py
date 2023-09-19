from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from domain.view_item import view_item_schema
from domain.recommendation import recommendation_schema, recommendation_crud

router = APIRouter(
    prefix = "/recommend",
    tags = ["recommend"]
)

@router.post('/recommend', response_model = view_item_schema.ItemList)
async def recommend(db : Session = Depends(get_db), new_user_info: recommendation_schema.New_User_Data = dict) :
    new_user = recommendation_crud.make_new_user_data(db, new_user_info)
    rec_result = recommendation_crud.make_recommend(new_user)
    rec_data = recommendation_crud.return_recommendation(db, rec_result)
    return view_item_schema.ItemList(item_list = rec_data)














