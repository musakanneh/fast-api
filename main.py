from fastapi import FastAPI
from typing import List
from models import User, Gender, Role
from http.client import HTTPException
from uuid import UUID, uuid4

app = FastAPI()

db:List[User] = [
    User(
        id=uuid4(),
        first_name="Musa",
        last_name="Kanneh",
        gender=Gender.male,
        roles=[Role.admin]
    ),
     User(
        id=uuid4(),
        first_name="Fatu",
        last_name="Kanneh",
        gender=Gender.female,
        roles=[Role.admin, Role.user]
    ),
    User(
        id=uuid4(),
        first_name="John",
        last_name="Paul",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def remove_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
    raise HTTPException(
        status_code=404,
        detail=f"user with id {user_id} does not exist"
    )