from optparse import Option
from unicodedata import numeric
from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Optional, List
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    admin = "admin"
    user = "student"
    student = "student"

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    roles: List[Role]

class UserUpateRequest(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    roles: Optional[List[Role]]


class AddItem(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None