from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import NoteCreate, NoteOut
from models import Note
from auth import get_db, get_current_user
from ml_sentiment import analyze_sentiment
from typing import List

router = APIRouter()

@router.post("/notes", response_model=NoteOut)
def create_note(note: NoteCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    sentiment = analyze_sentiment(note.text)
    new_note = Note(text=note.text, sentiment=sentiment, owner_id=user.id)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note

@router.get("/notes", response_model=List[NoteOut])
def get_notes(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(Note).filter(Note.owner_id == user.id).all()
