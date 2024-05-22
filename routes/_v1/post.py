import logging

from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from core.database import get_db
from core.models import Posts
from models.post_model import CreatePost
from service.post_service import PostService

post_router = APIRouter()

@post_router.get('/')
def read_root(db: Session = Depends(get_db)):
    logging.info("Hello World")
    item = db.query(Posts).all()
    logging.error("error")

    return {"Hello": "World", "item": item}

@post_router.post('/')
async def create_post(request: Request, data: CreatePost, db: Session = Depends(get_db)):
    post_service = PostService(request, db)  # PostService 인스턴스 생성
    post = post_service.create_post(data)
    return {"Hello": "World", "post": post}
