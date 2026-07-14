from pydantic import BaseModel

class PenaltiesToUsersCreate(BaseModel):
    user_id : int
    penalty_id : int
    