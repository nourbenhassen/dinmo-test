from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import models, people
from .database import engine
from .config import PEOPLE_API_SUFFIX, HEALTHCHECKER_API_SUFFIX

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(people.router, tags=['People'], prefix=PEOPLE_API_SUFFIX)


@app.get(HEALTHCHECKER_API_SUFFIX)
def root():
    return {"message": "Welcome to DinMo App"}