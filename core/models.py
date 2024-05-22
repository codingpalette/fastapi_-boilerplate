from sqlalchemy import Column, Integer, String, Text, Enum, ForeignKey, Index, text, DateTime, Date, Time, Boolean, BIGINT, UniqueConstraint
from typing import List
from core.database import Base

class Posts(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
