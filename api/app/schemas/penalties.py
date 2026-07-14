from pydantic import BaseModel

class PenaltyCrate(BaseModel):
    title : str
    reason : str
    number_of_weeks : int
    