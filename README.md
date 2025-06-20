# 📝 FastAPI Notes API

REST API for storing notes with sentiment analysis, user registration and JWT login. Built using FastAPI, SQLite and a simple NLP model (TextBlob).

---

## 📦 functions

- ✅ User registration and login (JWT)
- ✅ Creating and downloading notes associated with a user
- ✅ Text sentiment analysis (positive / negative / neutral)
- ✅ Token authorization (Bearer)
- ✅ Swagger documentation (`/docs`)
---

## 🚀 fasy start

### 1. Clone repo:
```bash
git clone addr_of_repo
cd fastapi-notes-api

```

### 2. Create and activate virtul enviroment:
```bash
    python -m venv venv
    source venv/bin/activate   # Linux/macOS
    venv\Scripts\activate      # Windows
```

### 3. Install everything
```bash
  pip install -r requriments.txt
```
or
```bash
    pip install fastapi uvicorn sqlalchemy pydantic textblob python-multipart passlib[bcrypt] python-jose
    python -m textblob.download_corpora
```

### 4. Start app
```bash
    uvicorn main:app --reload
```
### 5. Docs:
 [http://127.0.0.1:8000/docs][http://127.0.0.1:8000/docs]

### 6. Structure
```
.
├── auth.py
├── database.py
├── image.png
├── main.py
├── ml_sentiment.py
├── models.py
├── notes.db
├── README.md
├── requriments.txt
├── routers
│   ├── notes.py
│   └── users.py
└── schemas.py
```



### 🧠 Analize:

Use TextBlob - simple:

    > 0: positive

    < 0: negative

    = 0: neutral

### TEST with curl
```bash
# rejestration
curl -X POST http://localhost:8000/register -H "Content-Type: application/json" -d '{"username":"user1", "password":"secret"}'

# login
curl -X POST http://localhost:8000/token -d "username=user1&password=secret" -H "Content-Type: application/x-www-form-urlencoded"

# add note
curl -X POST http://localhost:8000/notes -H "Authorization: Bearer u_token" -H "Content-Type: application/json" -d '{"text": "I love FastAPI!"}'

# get note
curl -H "Authorization: Bearer u_token" http://localhost:8000/notes
```