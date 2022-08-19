from cgitb import reset
from re import S
from typing import Optional,List
from fastapi import FastAPI,Path, Query
from pydantic import BaseModel

app = FastAPI()

users = []

#pydantic librbary for validation user object if it matched with feilds -- DATATYPES
# data vaildation
class User(BaseModel):
    email:str
    is_active: bool
    bio: Optional[str] # not a mendatory feild to insrt -- dtype is "str"
    #when u pass it as empty respose it null-- db should take null



@app.get("/users",response_model=List[User])
async def get_user():
    return users#{"message": "Hello World"}

@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return "success"


@app.post("/users/{id}")# for PATH parameter adding description and some level of built-in validation
async def get_user(
    #... mandatory
    id: int = Path(...,description="The id of user you want to retrieve",lt=5),
    # QUERY paramaetr
    # none - not mandatory
    q: str = Query(None, max_lenght=4)
):
    return {"user": users[id], "query": q}

'''
path vataible gets 1st precedence
Every path variable must match the parameter of a function & rest varible is assumed as a query parameter '''