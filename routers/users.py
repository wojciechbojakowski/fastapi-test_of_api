from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import UserCreate, Token
from models import User
from auth import hash_password, verify_password, create_access_token, get_db
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.username == user.username).first():
        raise HTTPException(status_code=400, detail="Użytkownik już istnieje")
    new_user = User(username=user.username, hashed_password=hash_password(user.password))
    db.add(new_user)
    db.commit()
    return {"msg": "Zarejestrowano"}

@router.post("/token", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Nieprawidłowe dane logowania")
    token = create_access_token(data={"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}
