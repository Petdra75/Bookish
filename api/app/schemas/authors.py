from api.app.models.genre import Genres
from pydantic import BaseModel
from datetime import datetime


class AuthorCreate(BaseModel):
    name : str
    birth_date : datetime
    volumes_published: int
    