from fastapi.testclient import TestClient
from .main import app
from .config import PEOPLE_API_SUFFIX, API_TOKEN


client = TestClient(app)


def test_get_people():
    response = client.get(url=PEOPLE_API_SUFFIX, headers={"X-Token": API_TOKEN})
    assert response.status_code == 200

def test_get_people_bad_token():
    response = client.get(url=PEOPLE_API_SUFFIX, headers={"X-Token": "test"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid X-Token header"}


def test_post_people():
    data = {"people": [{"name": "Albert","age": 40, "gender": "M", "country": "Germany"}]}
    response = client.post(url=PEOPLE_API_SUFFIX, headers={"X-Token": API_TOKEN}, json=data)
    assert response.status_code == 201

def test_post_people_bad_token():
    data = {"people": [{"name": "Albert","age": 40, "gender": "M", "country": "Germany"}]}
    response = client.post(url=PEOPLE_API_SUFFIX, headers={"X-Token": "test"}, json=data)
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid X-Token header"}


def test_get_gender_repartition():
    response = client.get(url=f"{PEOPLE_API_SUFFIX}/gender-repartition/France", headers={"X-Token": API_TOKEN})
    assert response.status_code == 200

def test_get_gender_repartition_bad_token():
    response = client.get(url=f"{PEOPLE_API_SUFFIX}/gender-repartition/France", headers={"X-Token": "test"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid X-Token header"}