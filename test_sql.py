from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from database import Base
from main import app, get_db

DATABASE_URL = "sqlite://"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

PATTERN_ERROR_MSG = "Invalid name input"
NOT_FOUND_ERROR_MEG = "Person not found"
ALREADY_EXIST_MSG = "Name exist already"


def test_create_person():
    res = client.post("/api", json={"name": "mark essien"})
    data = res.json()
    assert res.status_code == 200
    assert data["name"] == "Mark Essien"
    assert "user_id" in data
    user_id = data["user_id"]
    assert data["user_id"] is not None
    assert res.json() == {
        "name": "Mark Essien",
        "user_id": 1
    }


def test_create_person_invalid():
    res = client.post("/api", json={"name": 8})
    assert res.status_code == 422


def test_create_person_empty():
    res = client.post("/api", json={"name": ""})
    assert res.status_code == 400
    assert res.json() == {
        "detail": PATTERN_ERROR_MSG
    }


def test_create_person_exist():
    res = client.post("/api", json={"name": "mark essien"})
    assert res.status_code == 400
    assert res.json() == {
        "detail": ALREADY_EXIST_MSG
    }


def test_index():
    res = client.get("/")
    assert res.status_code == 200


def test_index_invalid():
    res = client.get("/api")
    assert res.status_code == 422


def test_read_person():
    res = client.get(f"/api/1")
    assert res.status_code == 200
    assert res.json() == {
        "name": "Mark Essien",
        "user_id": 1
    }


def test_read_person_not_found():
    res = client.get("/api/2")
    assert res.status_code == 404
    assert res.json() == {
        "detail": NOT_FOUND_ERROR_MEG
    }


def test_read_person_invalid():
    res = client.get("/api/")
    assert res.status_code == 422


def test_read_person_by_name():
    res = client.get(f"/api?name=mark%20essien")
    assert res.status_code == 200
    assert res.json() == {
        "name": "Mark Essien",
        "user_id": 1
    }


def test_read_person_by_name_not_found():
    res = client.get(f"/api?name=jane%20doe")
    assert res.status_code == 404
    assert res.json() == {
        "detail": NOT_FOUND_ERROR_MEG
    }


def test_read_person_by_name_invalid():
    res = client.get(f"/api/name=jane%20doe")
    assert res.status_code == 422


def test_update_person():
    create_person = client.post("/api", json={"name": "doyin lawal"})
    data = create_person.json()
    assert create_person.status_code == 200
    user_id = data["user_id"]
    assert create_person.json() == {
        "name": "Doyin Lawal",
        "user_id": 2
    }

    res = client.put(f"/api/{user_id}", json={"name": "bisi adekunmi"})
    update_data = res.json()
    assert res.status_code == 200
    assert res.json() == {
        "name": "Bisi Adekunmi",
        "user_id": 2
    }


def test_update_person_empty():
    res = client.put("/api/1", json={"name": "solomon!"})
    assert res.status_code == 400
    assert res.json() == {
        "detail": PATTERN_ERROR_MSG
    }


def test_update_person_not_found():
    res = client.put(f"/api/20", json={"name": "toni pain"})
    assert res.status_code == 404
    assert res.json() == {
        "detail": NOT_FOUND_ERROR_MEG
    }


def test_update_person_name_unchanged():
    res = client.put("/api/1", json={"name": "mark essien"})
    assert res.status_code == 400
    assert res.json() == {
        "detail": "No change in the name"
    }


def test_update_person_exist():
    res = client.put("/api/2", json={"name": "mark essien"})
    assert res.status_code == 400
    assert res.json() == {
        "detail": ALREADY_EXIST_MSG
    }


def test_delete_person():
    create_person = client.post("/api", json={"name": "tosin adeniyo"})
    data = create_person.json()
    assert create_person.status_code == 200
    user_id = data["user_id"]
    assert create_person.json() == {
        "name": "Tosin Adeniyo",
        "user_id": 3
    }

    res = client.delete(f"/api/{user_id}")
    assert res.status_code == 200
    assert res.json() == f"Person with id number: {user_id} was deleted."


def test_delete_person_not_found():
    res = client.delete(f"/api/3")
    assert res.status_code == 404
    assert res.json() == {
        "detail": "Person with id number: 3, not found."
    }
