
from fastapi import APIRouter

post_router = APIRouter()

@post_router.get('/')
def read_root():
    return {"Hello": "World"}
