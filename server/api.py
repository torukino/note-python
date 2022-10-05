from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://drug-simulator-torukino.vercel.app",
    "https://drug-simulator.vercel.app",
    "https://drug-simulator-git-main-torukino.vercel.app",
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