from typing import List
from uuid import uuid4
from fastapi import FastAPI, HTTPException

from src.models import Notes, authorModel

#setting app to FastAPI library 
app = FastAPI()

db: List[Notes] = [
    Notes(
        title = "newTitle",
        text = "closed",
        locked = False,
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

#fetches all the notes 
@app.get('/notes')
def allNotes():
    return db

#creates a new note and adds it to our "database"
@app.post('/notes')
async def createNote(note: Notes):
    db.append(note)
    return {"status": 200}

#deltes a note if it exists
@app.delete('/notes/{noteTitle}')
async def deleteNote(noteTitle: str):
    for titles in db:
        if titles.title == noteTitle:
            db.remove(titles)
            return {"status": 200}
    #raises an exception if the note does not exist
    raise HTTPException(
        status_code = 404,
        detail=f"Note with title '{noteTitle}' does not exist"
    )

@app.put('/notes')
async def updateNote(noteTitle: str, updatedText: str):
    print(db)
    #need a way to make sure the account thats changing is the same and make sure the document is locked 
    for notes in db:
        if notes.title == noteTitle:
            notes.text = updatedText    
            return {"status": 200}
    raise HTTPException(
        status_code = 404,
        detail=f"Note with title '{noteTitle}' does not exist"
    )
