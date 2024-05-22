from sqlalchemy import Column, String, Integer
from core.database import Base
from pydantic import BaseModel


class CreatePost(BaseModel):
    title: str
    content: str


# class PostResponse(BaseModel):
#     id: int
#     title: str
#     content: str
#
#     class Config:
#         orm_mode = True
