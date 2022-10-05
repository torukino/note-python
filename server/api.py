from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:3000",
    "note-next-git-master-torukino.vercel.app",
    "note-next-torukino.vercel.app",
    "note-next.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def noteList():
    output={"100001":"HCV", "100002":"MRI禁"}
    return output