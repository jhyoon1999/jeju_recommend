from fastapi import FastAPI
from mangum import Mangum

from src.domain.recommend import recommend_router

app = FastAPI()
handler = Mangum(app)

@app.get('/')
async def home() :
    return {"추천시스템" : "제주도"}

app.include_router(recommend_router.router)