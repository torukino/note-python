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
  return list

def addNotes(notes:List[Note])->List[Note]:
    for note in notes:
        note_ = {"karuteNo":note.karuteNo, 
                 "note":note.note if note.note != None else '',
                 "name":note.name if note.name != None else '',
                 "kana":note.kana if note.kana != None else '',
                 "gender":note.gender if note.gender != None else '',
                 "nengo":note.nengo if note.nengo != None else '',
                 "birthYear":note.birthYear if note.birthYear != None else '',
                 "birthMonth":note.birthMonth if note.birthMonth != None else '',
                 "birthDay":note.birthDay if note.birthDay != None else '',
                 "address1":note.address1 if note.address1 != None else '',
                 "address2":note.address2 if note.address2 != None else '',
                 "tel":note.tel if note.tel != None else '',
                 "zipcode":note.zipcode if note.zipcode != None else '',
                 }
        ref.document(note.karuteNo).set(note_)
    return notes
