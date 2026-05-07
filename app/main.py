from fastapi import FastAPI
from app.routes.article_routes import router as article_router

app = FastAPI()

app.include_router(article_router)


@app.get("/")
def home():
    return {"message": "AI Podcast Generator Running"}