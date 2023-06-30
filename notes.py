from typing import List
from uuid import uuid4
from fastapi import FastAPI

from models import Notes, authorModel

#setting app to FastAPI library 
app = FastAPI()

db: List[Notes] = [
    Notes(
        title = "newTitle",
        text = "closed",
        locked = True,
        author = authorModel(
            username = "pipin",
            name = "KJ",
            email = "urmom@gmail.com",
            state = "active"
        )
    )
]

@app.get('/')
def main():
    return {"ur": "mom"}

@app.get('/notes')
def allNotes():
    return db
