from fastapi import FastAPI
from mangum import Mangum
import uvicorn

from src.schema import New_User_Dict_List
from src.function import make_recommend

app = FastAPI()
handler = Mangum(app)

@app.get('/')
async def root():
    return {"추천시스템으로부터 추천아이템을 받아내는 API입니다."}

@app.post('/recommend')
async def recommend(new_user_dict_list : New_User_Dict_List) :
    rec_result = make_recommend(new_user_dict_list)
    return rec_result


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0.', port=9000)

