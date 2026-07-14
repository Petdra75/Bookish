from api.app.models.genre import Genres
from pydantic import BaseModel
import datetime as dt


class AuthorCrate(BaseModel):
    name : str
    birth_date : dt.date
    volumes_published: int