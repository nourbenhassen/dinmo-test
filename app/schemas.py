from datetime import datetime
from typing import List
from pydantic import BaseModel


class PersonSchema(BaseModel):
    id: str = None
    name: str
    age: int
    gender: str
    country: str
    createdAt: datetime = None
    updatedAt: datetime = None


class ListPersonSchema(BaseModel):
    people: List[PersonSchema]

class Response(BaseModel):
    status: str = "success"

class ResponsePost(Response):
    message: str

class ResponseGet(Response):
    data: list

class ResponseGetPeople(ResponseGet):
    count_countries: int