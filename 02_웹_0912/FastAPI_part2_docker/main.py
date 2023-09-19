from fastapi import FastAPI
from mangum import Mangum

from src.domain.view_item import view_item_router
from src.domain.recommdation import recommendation_router

app = FastAPI()
handler = Mangum(app)

@app.get('/')
async def home() :
    return {"추천시스템" : "제주도"}

app.include_router(view_item_router.router)
app.include_router(recommendation_router.router)