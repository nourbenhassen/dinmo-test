from sqlalchemy import func, Integer
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, APIRouter, Header
from .database import get_db
from .config import API_TOKEN
from . import schemas, models


router = APIRouter()

@router.get('/', response_model = schemas.ResponseGetPeople)
def get_people(db: Session=Depends(get_db), x_token: str = Header()):
    if x_token != API_TOKEN:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")

    people = db.query(
            func.count(models.Person.age).label('count_people'), 
            func.cast(func.avg(models.Person.age), Integer).label('avg_age'), 
            models.Person.country
        ).group_by(models.Person.country).all()

    return schemas.ResponseGetPeople(
        count_countries=len(people),
        data=people
    )


@router.post('/', response_model = schemas.ResponsePost, status_code=status.HTTP_201_CREATED)
def create_people(payload: schemas.ListPersonSchema, x_token: str = Header(), db: Session = Depends(get_db)):
    if x_token != API_TOKEN:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")

    payload = list(payload.people)
    items = [models.Person(**person.dict()) for person in payload]
    db.add_all(items)
    db.commit()
    return schemas.ResponsePost(message=f"{len(payload)} items were ingested")


@router.get('/gender-repartition/{country}', response_model = schemas.ResponseGet)
def get_gender_repartition(country: str, db: Session = Depends(get_db), x_token: str = Header()):
    #TODO: optimization => one query instead of two.
    if x_token != API_TOKEN:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")

    count_total_gender = func.count(models.Person.gender)
    count_males = db.query(
        count_total_gender.label('count_males')
        ).filter(models.Person.gender == 'M'
        ).filter(models.Person.country == country
        ).all()[0]["count_males"]

    gender_repartition = db.query(
            func.round(100 * count_males / count_total_gender)
            .label('male_percentage'),
            func.round(100 * (count_total_gender - count_males) / count_total_gender)
            .label('female_percentage'),
            models.Person.country
        ).filter(models.Person.country == country).group_by(models.Person.country).all()
    return schemas.ResponseGet(data=gender_repartition)
