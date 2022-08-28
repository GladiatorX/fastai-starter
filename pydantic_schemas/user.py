from datetime import datetime
from pydantic import BaseModel


# 1.41 hrs
# User db -  id,email,role, is_active, profile, created_at, updated_at
# reklation --->  owner --> profile
# Profile db -  id, first_name, last_name, bio , user_id,
class UserBase(BaseModel):
    email : str
    role: int


class UserCreate(UserBase):
    #password: str
    ...#pass empty Ellipses

class User(UserBase):
    id: int
    is_active:  bool
    created_at: datetime
    updated_at: datetime

    '''
    # To be used when we are using pydantic with sqlalchmy like ORM
    # heps in converting object returned from ORM to py Dicts- saves manual effort
    class Config:
        orm_mode = True
    '''