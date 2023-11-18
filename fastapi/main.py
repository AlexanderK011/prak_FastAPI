from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from routers import films,news

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(films.filmsRouter)
app.include_router(news.newsRouter)