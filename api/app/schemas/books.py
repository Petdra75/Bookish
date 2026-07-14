from app.models.genre import Genre
from pydantic import BaseModel
import datetime as dt

class BookCreate(BaseModel):
    title : str  
    isbn : str 
    edition : str
    number_of_copies : int 
    publication_date : dt.datetime

    
