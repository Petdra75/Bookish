from sqlalchemy import Date, Column, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from typing import List
import datetime as dt
from app.helpers.database import Base

class BookGenreAssociation(Base):
    __tablename__ = "book_genre_associations"
    
    book_genre_id : Mapped[int] = mapped_column(Integer, primary_key = True, autoincrement=True)
    book_id : Mapped[int] = mapped_column(Integer, ForeignKey('books.book_id', ondelete="CASCADE"), nullable=False)
    genre_id : Mapped[int] = mapped_column(Integer, ForeignKey('genres.genre_id', ondelete="CASCADE"), nullable=False)
    
    def __init__(self, book_id : int, genre_id :int):
        self.book_id = book_id
        self.genre_id = genre_id
    
    def serialize(self):
        return {
            "id": self.book_genre_id,
            "book_id": self.book_id,
            "genre_id": self.genre_id
        }