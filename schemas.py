from pydantic import BaseModel

class PersonBase(BaseModel):
    name: str
    
class Person(PersonBase):
    user_id: int
