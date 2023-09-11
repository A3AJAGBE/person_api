from fastapi import FastAPI, Response
from pydantic import BaseModel

app = FastAPI()

persons = []

class Person(BaseModel):
    id: int
    name: str


@app.get("/")
def index():
    return persons


@app.post("/api")
async def add_person(new_person: Person, res: Response):
    person = new_person.model_dump()
    persons.append(person)
    res.status_code = 201
    return "Person added successfully"
