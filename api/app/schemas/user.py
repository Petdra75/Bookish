from pydantic import BaseModel

class UserCrate(BaseModel):
    username : str
    first_name : str
    last_namee : str
    password : str