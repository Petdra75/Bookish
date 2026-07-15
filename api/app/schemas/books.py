from typing import List, Optional

from app.models.authors import Author
from app.models.genre import Genre
from pydantic import BaseModel
from datetime import datetime

class BookCreate(BaseModel):
    title : str  
    isbn : str 
    edition : str
    number_of_copies : int 
    publication_date : datetime

class BookDisplay(BaseModel):
    book_id : int
    title : str  
    isbn : str 
    edition : str
    number_of_copies : int 
    publication_date : datetime
