from app.models.authors import Author
from app.models.books import Book
from pydantic import BaseModel

class WrittenByCreate(BaseModel):
    book_id : int
    author_id : int
