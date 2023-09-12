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
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_create_person():
    res = client.post("/api", json={"name": "Mark Essien"})
    data = res.json()
    assert res.status_code == 200
    assert data["name"] == "Mark Essien"
    assert "user_id" in data
    user_id = data["user_id"]
    assert data["user_id"] is not None

    # res = client.get(f"/api/{user_id}")
    # data = res.json()
    # assert res.status_code == 200
    # assert data["name"] == "Mark Essien"
    # assert data["user_id"] == user_id

def test_create_person_invalid():
    res = client.post("/api", json={"name": 8})
    assert res.status_code == 422
    

def test_create_person_empty():
    res = client.post("/api", json={"name": ""})
    assert res.status_code == 400
    

def test_create_person_exist():
    res = client.post("/api", json={"name": "Mark Essien"})
    assert res.status_code == 400
    

