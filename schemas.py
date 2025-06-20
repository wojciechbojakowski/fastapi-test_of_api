from pydantic import BaseModel
from typing import Optional, List

class UserCreate(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    class Config:
        from_attributes = True

class NoteBase(BaseModel):
    text: str

class NoteCreate(NoteBase):
    pass

class NoteOut(NoteBase):
    id: int
    sentiment: str
    owner_id: int
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
