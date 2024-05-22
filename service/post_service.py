from fastapi import Request
from core.database import db_session
from core.models import Posts


class PostService():
    def __init__(self, request: Request, db: db_session):
        self.request = request
        self.db = db

    def create_post(self, data) -> Posts:
        post = Posts(**data.__dict__)

        self.db.add(post)
        self.db.commit()
        self.db.refresh(post)  # 새로 추가된 데이터를 포함하여 객체를 갱신

        return post
