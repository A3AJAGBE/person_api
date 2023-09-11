from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
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


@app.post("/api", response_model=schemas.Person)
def add_person(person: schemas.PersonBase, db: Session = Depends(get_db)):
    new_person = crud.get_person_by_name(db, name=person.name)
    if new_person:
        raise HTTPException(status_code=400, detail="Name exist already")
    return crud.create_person(db=db, person=person)


@app.get("/", response_model=list[schemas.Person])
def index(db: Session = Depends(get_db)):
    persons = crud.get_persons(db)
    return persons


@app.get("/api/{user_id}", response_model=schemas.Person)
def read_person(user_id: int, db: Session = Depends(get_db)):
    db_person = crud.get_person(db, user_id=user_id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return db_person


@app.put("/api/{user_id}", response_model=schemas.Person)
def edit_person(user_id: int, edit_person: schemas.PersonBase, db: Session = Depends(get_db)):
    db_person = crud.get_person(db, user_id=user_id) 
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return crud.edit_person(db=db, user_id=user_id, edit_person=edit_person)


@app.delete("/api/{user_id}")
def delete_person(user_id: int, db: Session = Depends(get_db)):
    db_person = crud.get_person(db, user_id=user_id)
    
    if db_person is None:
        raise HTTPException(status_code=404, detail=f"Person with id number: {user_id}, not found.")
    return crud.delete_person(db, user_id=user_id)
    