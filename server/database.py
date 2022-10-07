import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from typing import List
from .model import Note
# firebase_admin.initialize_app()

if not firebase_admin._apps:
  j ="tejunproject-firebase-adminsdk-urm6y-36c021e98d.json"
  cred = credentials.Certificate(j)
  firebase_admin.initialize_app(cred)


db = firestore.client()
ref = db.collection(u'notes')

async def getNotes()->List:
  docs = ref.stream()
  list = []
  for doc in docs:
    list.append(doc.to_dict())
  # for doc in docs:
  #   print(
  #     f"カルテ番号:{doc.get('karuteNo')} "
  #     f"注意ﾘｽﾄ:{doc.get('note')} "
  #     )
  return list

async def addNotes(notes:List[Note]):
  for note in notes:
    await ref.document(note.karuteNo).set(note)
