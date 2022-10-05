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
    output=[{"karteNo":"100001","content":"HCV"},
            {"karteNo":"100012","content":"MRI禁"},
            {"karteNo":"100023","content":"あーだこーだ"} ]
    return output