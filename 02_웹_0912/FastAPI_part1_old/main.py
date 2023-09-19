from fastapi import FastAPI
from mangum import Mangum
from schema import New_User
from crud import make_recommend

app = FastAPI()
handler = Mangum(app)

@app.post("/get_recommend")
async def recommend_item(new_user_dict : New_User) :
    rec_result = make_recommend(new_user_dict)
    return rec_result





