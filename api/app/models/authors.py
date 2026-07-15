from app.models.genre import Genre
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import Mapped, mapped_column
from typing import List
from sqlalchemy.orm import relationship
from datetime import datetime
from app.helpers.database import Base

class Author(Base):
    __tablename__ = "author"
    
    author_id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name : Mapped[str] = mapped_column(String(30))
    birth_date : Mapped[datetime] = mapped_column(Date)
    volumes_published : Mapped[int] = mapped_column(Integer)
    
    def __int__(self, name : str, birth_date: datetime, volumes_published : int):
        self.name = name
        self.birth_date = birth_date
        self.volumes_published = volumes_published
    
    def serialize(self):
        return {
            "id": self.author_id,
            "name": self.name,
            "birth_date": self.birth_date,
            "volumes_published": self.volumes_published
        }