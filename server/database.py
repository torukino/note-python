import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from typing import List
# firebase_admin.initialize_app()

if not firebase_admin._apps:
  j ="tejunproject-firebase-adminsdk-urm6y-36c021e98d.json"
  cred = credentials.Certificate(j)
  firebase_admin.initialize_app(cred)




async def getNotes()->List:
  db = firestore.client()
  ref = db.collection('notes')
  docs = ref.stream()
  for doc in docs:
    print(
      f"カルテ番号:{doc.get('karuteNo')} "
      f"禁止:{doc.get('note')} "
      )
  return docs
