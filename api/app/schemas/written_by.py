from pydantic import BaseModel

class WrittenBy(BaseModel):
    book_id : int
    author_id : int
    