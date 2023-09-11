from fastapi import FastAPI, Response
from pydantic import BaseModel

app = FastAPI()

persons = [
    {
        "name": "tola",
        "user_id": 1
    },
    {
        "name": "ngozi",
        "user_id": 2
    },
    {
        "name": "simi",
        "user_id": 3
    }
]

class Person(BaseModel):
    name: str


@app.get("/")
async def index():
    return persons


@app.post("/api")
async def add_person(new_person: Person, res: Response):
    person = new_person.model_dump()
    person["user_id"] = len(persons) + 1
    persons.append(person)
    res.status_code = 201
    return "Person added successfully"


@app.get("/api/{user_id}")
async def get_person(user_id: int, res: Response):
    for person in persons:
        if person["user_id"] == user_id:
            res.status_code = 200
            return person
        else:
            res.status_code = 404
            return "Person not found"
            
