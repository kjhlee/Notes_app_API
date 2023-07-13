from fastapi import FastAPI
from src.notes import *
from src.models import Notes, authorModel
import asyncio



async def createNewNote():
    newText = input("this is a new note that I would like to add: ")
    newNote = Notes(
        title = "text2",
        text = newText,
        locked = False,
        author = authorModel(
            username = "pipin",
            name = "KJ",
            email = "urmom@gmail.com",
            state = "active"
        )
    )
    await createNote(newNote)

async def changeNote(noteTitle):
    newText = input("New text: ")
    await updateNote(noteTitle, newText)

async def main():
    print(db[0].title)
    var = input("What would you like to do? ")
    if var == "create_new":
        await createNewNote()
    if var == "change":
        titleCheck = db[0].title
        await changeNote(titleCheck)

asyncio.run(main())