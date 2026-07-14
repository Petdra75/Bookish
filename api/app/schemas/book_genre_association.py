from pydantic import BaseModel

class BookGenreAssociationCrate(BaseModel):
    book_id : int
    genre_id : int