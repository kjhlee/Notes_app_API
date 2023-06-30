from enum import Enum
from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel

class authorModel(BaseModel):
    username: str
    name: str
    email: str
    state: str

class Notes(BaseModel):
    id: Optional[UUID] = uuid4()
    title: str
    text: str
    locked: bool = False
    author: authorModel
    
    



    