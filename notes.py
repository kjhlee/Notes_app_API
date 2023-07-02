from typing import List
from uuid import uuid4
from fastapi import FastAPI, HTTPException

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

@app.put('/notes/{noteTitle}')
async def updateNote(noteTitle: str, updatedNote: Notes):
    for notes in db:
        if notes.title == noteTitle:
            updatedNote.text = notes.text    
            return {"status": 200}
    raise HTTPException(
        status_code = 404,
        detail=f"Note with title '{noteTitle}' does not exist"
    )