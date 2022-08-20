
from typing import Optional,List
import fastapi
from pydantic import BaseModel

# this will be referencedin main.py
router = fastapi.APIRouter()

"""
#pydantic librbary for validation user object if it matched with feilds -- DATATYPES
# data vaildation
class User(BaseModel):
    email:str
    is_active: bool
    bio: Optional[str] #  -- dtype is "str" -- not a mendatory field to insert
    # when u pass it as empty respose it(bio feild)--  null gets assigned-- so db should take null
"""
# for each - / http - get/put/post etc .. route there is a seperate funcname
@router.get("/courses")
async def read_courses():
    return {"courses": []}

@router.post("/courses") #as it reutns list of dicts
async def create_courses(course: str):
    return {"courses": []}

@router.get("/courses/{id}")
async def read_course(id: int):
    return {"courses": []}

@router.delete("/courses/{id}")
async def delete_courses(id: int):
    return {"courses": []}

@router.put("/courses/{id}")
async def delete_courses(id: int,course: str):
    return {"courses": []}


@router.put("/courses/{id}/sections")
async def read_course_section(id: int,course: str):
    return {"courses": []}


'''
PATH variable -- {id} -- gets 1st precedence
Every path variable must match the parameter of a function -- get_user()& rest varible is assumed as a query parameter 
'''



