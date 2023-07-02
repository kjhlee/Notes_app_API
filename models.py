from enum import Enum
from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, Field

class authorModel(BaseModel):
    username: str
    name: str
    email: str
    state: str

class Notes(BaseModel):
    title: str
    text: str
    locked: bool = False
    author: authorModel


class changeNotes(BaseModel):
    title: str
    text: str
    locked: bool
    author: authorModel
    
    



    