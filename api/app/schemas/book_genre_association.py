from pydantic import BaseModel

class BookGenreAssociationCreate(BaseModel):
    book_id : int
    genre_id : int
    