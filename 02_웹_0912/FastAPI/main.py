from fastapi import FastAPI
from domain.view_item import view_item_router
from domain.recommendation import recommendation_router

app = FastAPI()

@app.get("/")
async def home() :
    return {"Hello" : "World"}

app.include_router(view_item_router.router)
app.include_router(recommendation_router.router)
