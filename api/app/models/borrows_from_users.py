from sqlalchemy import Date, Column, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from typing import List
from datetime import datetime
from app.helpers.database import Base

class BorrowFromUsers(Base):
    __tablename__ = "borrow_from_user"
    
    borrow_id : Mapped[int] = mapped_column(Integer, primary_key = True, autoincrement=True)
    book_id : Mapped[int] = mapped_column(Integer, ForeignKey('book.book_id', ondelete="CASCADE"), nullable=False)
    user_id : Mapped[int] = mapped_column(Integer, ForeignKey('user.user_id', ondelete="CASCADE"), nullable=False)
    borrowed_from : Mapped[datetime] = mapped_column(Date, nullable = False)
    borrowed_until : Mapped[datetime] = mapped_column(Date, nullable = False)

def __init__(self, book_id : int, user_id: int, borrowed_from : int, borrowed_until : int):
    self.book_id = book_id
    self.user_id = user_id
    self.borrowed_from = borrowed_from
    self.borrowed_until = borrowed_until
      
def serialize(self):
    return {
        "id" : self.borrow_id,
        "book_id" : self.book_id,
        "self_id" : self.self_id,
        "user_id" : self.user_id,
        "borrowed_from" : self.borrowed_from,
        "borrowed_until" : self.borrowed_until
    }