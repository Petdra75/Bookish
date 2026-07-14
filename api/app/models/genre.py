from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import Mapped, mapped_column
from typing import List
from sqlalchemy.orm import relationship
import datetime as dt
from app.helpers.database import Base


class Genre(Base):
    __tablename__ = "genres"

    genre_id  : Mapped[int] = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title : Mapped[str] = mapped_column(String, nullable = False)

    def __init__(self, title:str):
        self.title = title
    def serialize(self):
        return {
            "id": self.id,
            "title" : self.title
        }