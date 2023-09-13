import re
PATTERN = re.compile("^([a-z]{2,}\s[a-z]{1,}'?-?[a-z]{2,}\s?([a-z]{1,})?)")

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

PATTERN_ERROR_MSG = "Characters must include lowercase characters and space. Apostrophe and hyphen allowed"
NOT_FOUND_ERROR_MEG = "Person not found"
ALREADY_EXIST_MSG = "Name exist already"


@app.post("/api", response_model=schemas.Person)
def create_person(person: schemas.PersonBase, db: Session = Depends(get_db)):
    
    if not PATTERN.match(person.name):
        raise HTTPException(
            status_code=400, detail=PATTERN_ERROR_MSG)

    new_person = crud.get_person_by_name(db, name=person.name)

    if new_person:
        raise HTTPException(status_code=400, detail=ALREADY_EXIST_MSG)

    return crud.create_person(db=db, person=person)
    

@app.get("/", response_model=list[schemas.Person])
def index(db: Session = Depends(get_db)):
    persons = crud.get_persons(db)
    return persons


@app.get("/api/{user_id}", response_model=schemas.Person)
def read_person(user_id: int, db: Session = Depends(get_db)):
    db_person = crud.get_person(db, user_id=user_id)
    
    if db_person is None:
        raise HTTPException(status_code=404, detail=NOT_FOUND_ERROR_MEG)
    
    return db_person


@app.get("/api", response_model=schemas.Person)
def read_person_by_name(name: str, db: Session = Depends(get_db)):
    db_person = crud.get_person_by_name(db, name=name)
    
    if db_person is None:
        raise HTTPException(status_code=404, detail=NOT_FOUND_ERROR_MEG)
    
    return db_person


@app.put("/api/{user_id}", response_model=schemas.Person)
def update_person(user_id: int, edit_person: schemas.PersonBase, db: Session = Depends(get_db)):
    if not PATTERN.match(edit_person.name):
        raise HTTPException(
            status_code=400, detail=PATTERN_ERROR_MSG)

    db_person = crud.get_person(db, user_id=user_id)
    
    if db_person is None:
        raise HTTPException(status_code=404, detail=NOT_FOUND_ERROR_MEG)
    
    if db_person.name == edit_person.name:
        raise HTTPException(
            status_code=400, detail="No change in the name")
    
    get_edit_name = crud.get_person_by_name(db, name=edit_person.name)
        
    if get_edit_name:
        raise HTTPException(status_code=400, detail=ALREADY_EXIST_MSG)

    return crud.edit_person(db=db, user_id=user_id, edit_person=edit_person)


@app.delete("/api/{user_id}")
def delete_person(user_id: int, db: Session = Depends(get_db)):
    db_person = crud.get_person(db, user_id=user_id)

    if db_person is None:
        
        raise HTTPException(
            status_code=404, detail=f"Person with id number: {user_id}, not found.")
        
    return crud.delete_person(db, user_id=user_id)
