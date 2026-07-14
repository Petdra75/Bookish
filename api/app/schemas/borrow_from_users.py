from pydantic import BaseModel
import datetime as dt

class BorrowFromUsers(BaseModel):
    book_id : int
    user_id : int
    borrowed_from : dt.date
    borrowed_until : dt.date