from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from models.post_model import Posts

post_router = APIRouter()

@post_router.get('/')
def read_root(db: Session = Depends(get_db)):
    item = db.query(Posts).all()

    return {"Hello": "World", "item": item}
