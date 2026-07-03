from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session as SessionType

from app.dependencies import get_db
from app.schemas.example import ExampleCreate
from app.models.example import Example
 
router = APIRouter(tags=["health"])

@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.post("/example", response_model=ExampleCreate)
def create_example(example: ExampleCreate, db: SessionType = Depends(get_db)):
    db_example = Example(example_field_1=example.example_field_1, example_field_2=example.example_field_2)
    db.add(db_example)
    db.commit()
    db.refresh(db_example)
    return db_example