from fastapi.testclient import TestClient
from .main import app
from .config import PEOPLE_API_SUFFIX, API_TOKEN


client = TestClient(app)


def test_get_people():
    response = client.get(url=PEOPLE_API_SUFFIX, headers={"X-Token": API_TOKEN})
    assert response.status_code == 200


def test_post_people():
    response = client.post(url=PEOPLE_API_SUFFIX, headers={"X-Token": API_TOKEN})
    assert response.status_code == 200


def test_get_gender_repartition():
    response = client.get(url=f"{PEOPLE_API_SUFFIX}/gender-repartition/france", headers={"X-Token": API_TOKEN})
    assert response.status_code == 200