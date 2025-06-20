from fastapi import FastAPI
import models
from database import engine
from routers import users, notes

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(notes.router)
