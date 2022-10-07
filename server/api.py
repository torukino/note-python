from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .database import getNotes
from .model import Note
from typing import List, Dict

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

# mongodb+srv://admin:nozomi0131@cluster0.bxr9z8p.mongodb.net/?retryWrites=true&w=majority


# App object
app = FastAPI()

origins = [
  'http://localhost:3000',
  'http://localhost',
  ]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.get("/")
async def read_root()->List[Note]:
  docs = await getNotes()
  return {"test":"hello"}
