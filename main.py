from fastapi import FastAPI
from typing import List
from models import User, Gender, Role
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
    )
]

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;