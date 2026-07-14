from app.models.genre import Genre
from pydantic import BaseModel
from datetime import datetime

class BookCreate(BaseModel):
    title : str  
    isbn : str 
    edition : str
    number_of_copies : int 
    publication_date : datetime
    