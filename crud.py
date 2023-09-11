from sqlalchemy.orm import Session

import models, schemas


def get_person(db: Session, user_id: int):
    return db.query(models.Person).filter(models.Person.user_id == user_id).first()


def get_person_by_name(db: Session, name: str):
    return db.query(models.Person).filter(models.Person.name == name).first()


def get_persons(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Person).offset(skip).limit(limit).all()


def create_person(db: Session, person: schemas.PersonBase):
    new_person = models.Person(name=person.name)
    db.add(new_person)
    db.commit()
    db.refresh(new_person)
    return new_person


def edit_person(db: Session, user_id: int, edit_person: schemas.PersonBase):
    db_person = db.query(models.Person).filter(
        models.Person.user_id == user_id).first()
    db_person.name = edit_person.name
    db.commit()
    db.refresh(db_person)
    return db_person


def delete_person(db: Session, user_id: int):
    db.query(models.Person).filter(models.Person.user_id == user_id).delete()
    db.commit()
    return f"Person with id number: {user_id} was deleted."
