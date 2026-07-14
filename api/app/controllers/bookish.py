from api.app.schemas.authors import  AuthorCreate
from app.models.books import Book
from app.schemas.books import BookCreate
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session as SessionType

from app.dependencies import get_db
from app.schemas.example import ExampleCreate
from app.models.example import Example
from typing import List
from datetime import datetime

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

@router.get("/books/", response_model=List[BookCreate])
def get_books(isbn : str = "", db : SessionType = Depends(get_db)):
    if isbn:
        return db.query(Book).filter(Book.isbn == isbn)
    else:
        return db.query(Book).all()
     

@router.post("/books", response_model=BookCreate)
def create_book(book: BookCreate, db : SessionType = Depends(get_db)):
    db_book : Book = Book(
        title=book.title, 
        isbn=book.isbn,
        edition=book.edition,
        number_of_copies=book.number_of_copies,
        publication_date=book.publication_date
        )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
# @router.get("/authors", response_model=AuthorCreate)
# @router.post("/create_author", reponse)