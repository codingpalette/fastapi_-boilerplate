from sqlalchemy import Column, String, Integer, DateTime, func
from sqlalchemy.orm import relationship
from db.database import Base

class Posts(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
