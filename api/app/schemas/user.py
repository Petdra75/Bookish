from pydantic import BaseModel

class UserCreate(BaseModel):
    username : str
    first_name : str
    last_namee : str
    password : str
    