
from typing import Optional,List #generic types
"""
https://fastapi.tiangolo.com/python-types/
ta structures that can contain other values, like dict, list, set and tuple. And the internal values can have their own type too.
 declare those types and the internal types, you can use the standard Python module typing.
  Union[SomeType, None]
"""
import fastapi
from fastapi import Depends, HTTPException

from pydantic_schemas.user import UserCreate, User
from db.queries.users_query import get_user, get_user_by_email, get_users, create_user
from db.db_setup import get_db
# this will be referencedin main.py
router = fastapi.APIRouter()
#pydantic librbary for validation user object if it matched with feilds -- DATATYPES

db = get_db()

@router.get("/", response_model=List[User])
async def checkup():
    return {"message":"visit baseurl:docs"}

#http://127.0.0.1:8000/items/?skip=0&limit=10
@router.get("/users",response_model=List[User]) #as it reutns list of dicts
async def read_user():
    users = get_users(db, skip=skip, limit=limit)
    return users
#
@router.post("/users", response_model=User, status_code=201)
async def create_new_user(user: User):
    db_user = get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email is already registered")
    return create_user(db=db, user=user)

'''
PATH variable -- {id} -- gets 1st precedence
Every path variable must match the parameter of a function -- get_user()& rest varible is assumed as a query parameter 
#Because path operations are evaluated in order, you need to make sure that the path for /users/me is declared before the one for /users/{user_id}:
https://fastapi.tiangolo.com/tutorial/query-params/

after path vaiable declared as a parameter of function, rest parameters are conside as normal input to function like for type checking etc
'''

@router.post("/users/{id}")# for PATH parameter adding description and some level of built-in validation
async def get_user(id: int):#= Path(...,description="The id of user you want to retrieve",lt=5)
    return {"user": users[id]}



