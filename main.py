from typing import Optional,List
from fastapi import FastAPI
from pydantic import BaseModel

from api import users,sections,courses


app = FastAPI(    
    title="Fast API LMS",
    description="LMS for managing students and courses.",
    version="0.0.1",
    contact={
        "name": "sk",
        "email": "sk@example.com",
    },
    license_info={
        "name": "MIT",
    }
)

app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router)