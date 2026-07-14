from pydantic import BaseModel

class PenaltiesToUsers(BaseModel):
    user_id : int
    penalty_id : int