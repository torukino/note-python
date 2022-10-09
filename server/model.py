from ast import TypeIgnore
from pydantic import BaseModel
from typing import Union



class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None


class UserInDB(User):
    hashed_password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    username: Union[str, None] = None

# カルテ番号,氏名,フリガナ,性別コード,年号,生年,月,日,住所１,住所２,TEL,郵便番号,職業,メモ
class Note(BaseModel):
  karuteNo: str
  note: Union[str, None] = None # メモ
  name: Union[str, None] = None # 氏名
  kana: Union[str, None] = None # カナ
  gender: Union[str, None] = None # 性別コード 
  nengo: Union[str, None] = None # 年号
  birthYear: Union[str, None] = None # 誕生年
  birthMonth: Union[str, None] = None # 誕生月
  birthDay: Union[str, None] = None #　誕生日
  address1:Union[str, None] = None #住所1
  address2: Union[str, None] = None # 住所2
  tel: Union[str, None] = None # TEL
  zipcode: Union[str, None] = None #郵便番号
        