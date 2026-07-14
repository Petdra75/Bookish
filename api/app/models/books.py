from app.models.written_by import WrittenBy
from app.models.authors import Author
from app.models.genre import Genre
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import Mapped, mapped_column
from typing import List
from sqlalchemy.orm import relationship
from datetime import datetime
from app.helpers.database import Base

class Book(Base):
    __tablename__ = "book"
    
    book_id : Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    title : Mapped[str] = mapped_column(String(50), nullable=False) 
    isbn : Mapped[str] = mapped_column(String(13), nullable=False) 
    edition : Mapped[str] = mapped_column(String(20), nullable=False)
    number_of_copies : Mapped[int] = mapped_column(Integer, nullable=False)
    publication_date : Mapped[datetime] = mapped_column(Date, nullable=True)
    
    def __init__(self, title : str, isbn : str, edition : str, number_of_copies: int, publication_date: datetime):
        
        self.title = title
        self.isbn = isbn
        self.edition =edition
        self.number_of_copies = number_of_copies
        self.publication_date = publication_date
    
    def serialize(self):
        return {
            "id": self.book_id,
            "title": self.title,
            "isbn": self.isbn,
            "edition": self.edition,
            "number_of_copies": self.number_of_copies,
            "publication_date": self.publication_date
        }