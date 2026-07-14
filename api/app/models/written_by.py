from sqlalchemy import Date, Column, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from typing import List
import datetime as dt
from app.helpers.database import Base

class WrittenBy(Base):
    __tablename__ = "written_by"
    
    writtenby_id : Mapped[int] = mapped_column(Integer, primary_key = True, autoincrement=True)
    book_id : Mapped[int] = mapped_column(Integer, ForeignKey('books.book_id', ondelete="CASCADE"), nullable=False)
    author_id : Mapped[int] = mapped_column(Integer, ForeignKey('authors.author_id', ondelete="CASCADE"), nullable=False)
    
    def __init__(self, book_id, author_id):
        self.book_id = book_id
        self.author_id = author_id
    
    def serialize(self):
        return {
            "id" : self.writtenby_id,
            "book_id" : self.book_id,
            "author_id" : self.author_id,
    
    }