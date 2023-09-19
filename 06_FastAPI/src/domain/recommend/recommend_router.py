from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.connection import get_db
from src.domain.recommend import recommend_crud, recommend_schema

router = APIRouter(
    prefix = "/recommend",
    tags = ["recommend"]
)

@router.post('/making_new_user_data', response_model= recommend_schema.Recommend_Data_List)
async def making_new_user_data(db : Session = Depends(get_db),
                            new_user_data : recommend_schema.New_User_Data = None,
                            filter : recommend_schema.Filter = None):
    new_user_data_dict = recommend_crud.make_new_user_data(db, new_user_data)
    item_info_collect = recommend_crud.call_item_info(db, filter)
    recommend_data_input = recommend_crud.make_recommend_data(new_user_data_dict, item_info_collect)
    return recommend_data_input
