from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import (
  fetch_one_todo,
  fetch_all_todos,
  create_todo,
  update_todo,
  remove_todo,
)
from model import Todo

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
def read_root():
    
  return {"Hello world"}

@app.get("/api/todo")
async def get_todo():
  response = await fetch_all_todos()
  return response

@app.get("/api/todo{title}", response_model=Todo)
async def get_todo_by_title(title):
  response = await fetch_one_todo(title)
  if response:
    return response
  raise HTTPException(404, f"there is no Todo item with this title {title}")

@app.post("/api/todo", response_model=Todo)
async def post_todo(todo:Todo):
  response = await create_todo(todo.dict())
  if response:
    return response
  raise HTTPException(400, "Sometheng went wrong / Bad Request")
