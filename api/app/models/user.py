from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import Mapped, mapped_column
from typing import List
from sqlalchemy.orm import relationship
import datetime as dt
from app.helpers.database import Base

class User(Base):
    __tablename__ = "users" 
    
    user_id : Mapped[int] = mapped_column(Integer, primary_key = True, autoincrement=True)
    username : Mapped[str] = mapped_column(String(50))
    first_name : Mapped[str] = mapped_column(String(50))
    last_name : Mapped[str] = mapped_column(String(50))
    password : Mapped[str] = mapped_column(String(21))
    
    def __init__(self, username : str, first_name : str, last_name : str, password: str):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        
    def serialize(self):
        return {
            "id" : self.user_id,
            "username" : self.username,
            "first_name" : self.first_name,
            "last_name" : self.last_name,
            "password" : self.password,
        }