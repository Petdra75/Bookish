from pydantic import BaseModel

class GenreCreate(BaseModel):
    title : str
