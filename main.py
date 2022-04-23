from this import d
from unicodedata import name
from fastapi import FastAPI
from typing import List
from models import User, Gender, Role, AddItem, UserUpateRequest
from http.client import HTTPException
from uuid import UUID, uuid4
from pydantic import BaseModel
from typing import Optional, List

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
    AddItem(
        id=uuid4(),
        name="Some item name",
        price=2.3,
        is_offer=True
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

@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id {user_id} does not exist"
    )

@app.post("/api/v1/users/{item_id}")
async def add_item(item_id: UUID):
    db.append(item_id)
    return {"item_id" : item_id}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}