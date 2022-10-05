from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


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
def noteList():
    output=[{"karteNo":"100001","content":"注意リスト1"},
            {"karteNo":"100002","content":"注意リスト2"},
            {"karteNo":"100003","content":"注意リスト3"} ]
    return output