from pydantic import BaseModel

class ExampleCreate(BaseModel):
    example_field_1: str
    example_field_2: int
    
