from pydantic import BaseModel
from datetime import datetime

class BorrowToUsersCreate(BaseModel):
    book_id : int
    user_id : int
    borrowed_from : datetime
    borrowed_until : datetime
    