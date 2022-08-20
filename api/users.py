
from typing import Optional,List
import fastapi
from pydantic import BaseModel

# this will be referencedin main.py
router = fastapi.APIRouter()

users = []
#pydantic librbary for validation user object if it matched with feilds -- DATATYPES
# data vaildation
class User(BaseModel):
    email:str
    is_active: bool
    bio: Optional[str] #  -- dtype is "str" -- not a mendatory field to insert
    # when u pass it as empty respose it(bio feild)--  null gets assigned-- so db should take null

@router.get("/", response_model=List[User])
async def get_users():
    return {"message":"visit baseurl:docs"}

@router.get("/users",response_model=List[User]) #as it reutns list of dicts
async def get_user():
    return users

@router.post("/users")
async def create_user(user: User):
    users.append(user)
    return "success"

'''
PATH variable -- {id} -- gets 1st precedence
Every path variable must match the parameter of a function -- get_user()& rest varible is assumed as a query parameter 
'''

@router.post("/users/{id}")# for PATH parameter adding description and some level of built-in validation
async def get_user(id: int):#= Path(...,description="The id of user you want to retrieve",lt=5)
    return {"user": users[id]}



