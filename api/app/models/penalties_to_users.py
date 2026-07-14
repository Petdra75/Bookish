from sqlalchemy import Date, Column, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from typing import List

import datetime as dt
from app.helpers.database import Base

class PenaltiesToUsers(Base):
    __tablename__ = "penalties_to_user"
    
    user_penalty_id : Mapped[int] = mapped_column(Integer, primary_key = True, autoincrement=True)
    user_id : Mapped[int] = mapped_column(Integer, ForeignKey('user.user_id', ondelete="CASCADE"), nullable=False)
    penalty_id : Mapped[int] = mapped_column(Integer, ForeignKey('penalty.penalty_id', ondelete="CASCADE"), nullable=False)
    
def __init__(self, user_id : int, penalty_id : int):
    self.user_id = user_id
    self.penalty_id = penalty_id
  
        
def serialize(self):
    return {
        "id" : self.borrow_id,
        "book_id" : self.book_id,
        "self_id" : self.self_id,
        "user_id" : self.user_id,
        "borrowed_from" : self.borrowed_from,
        "borrowed_until" : self.borrowed_until
    }