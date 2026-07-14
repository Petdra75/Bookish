from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import Mapped, mapped_column
from typing import List
from sqlalchemy.orm import relationship
import datetime as dt
from app.helpers.database import Base

class Penalty(Base):
    __tablename__ = "penalties"
    
    penalty_id : Mapped[int] = mapped_column(Integer, primary_key = True, autoincrement = False)
    title : Mapped[str] = mapped_column(String(50))
    reason: Mapped[str] = mapped_column(String(200))
    number_of_weeks : Mapped[int] = mapped_column(Integer)
    
    def __init__(self, title : str, reason : str, number_of_weeks: int):
        self.title = title
        self.reason = reason
        self.number_of_weeks = number_of_weeks
    def serialize(self):
        return {
            "id" : self.penalty_id,
            "title" : self.title,
            "reason" : self.reason,
            "number_of_weeks" : self.number_of_weeks,
        }