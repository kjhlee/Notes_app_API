from fastapi import FastAPI
from notes import *
from models import Notes, authorModel
import asyncio
import uvicorn

mainApp = FastAPI()

mainApp.mount("/", app)

async def createNewNote():
    newText = input("this is a new note that I would like to add: ")
    newNote = Notes(
        title = "text2",
        text = newText,
        locked = True,
        author = authorModel(
            username = "pipin",
            name = "KJ",
            email = "urmom@gmail.com",
            state = "active"
        )
    )
    await createNote(newNote)


async def main():
    var = input("What would you like to do? ")
    if var == "create_new":
        await createNewNote()

asyncio.run(main())
uvicorn.run(mainApp)