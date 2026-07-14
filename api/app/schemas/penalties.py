from pydantic import BaseModel

class PenaltyCreate(BaseModel):
    title : str
    reason : str
    number_of_weeks : int
    