from pydantic import BaseModel

class Note(BaseModel):
  karuteNo: str
  note: str