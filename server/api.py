from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import getNotes, addNotes
from .model import Note
from typing import List

app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://note-next-git-master-torukino.vercel.app",
    "https://note-next-torukino.vercel.app",
    "https://note-next.vercel.app"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_note()->List[Note]:
  notes = await getNotes()
  return notes

@app.post("/")
async def write_notes(notes:List[Note])->List[Note]:
    notes = addNotes(notes)
    return notes
  