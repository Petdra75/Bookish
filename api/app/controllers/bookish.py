
from app.models.book_genre_association import BookGenreAssociation
from app.models.genre import Genre
from app.models.penalties import Penalty
from app.models.written_by import WrittenBy
from app.schemas.book_genre_association import BookGenreAssociationCreate
from app.schemas.written_by import WrittenByCreate
from app.models.authors import Author
from app.schemas.borrow_to_users import BorrowToUsersCreate
from app.models.user import User
from app.models.borrows_to_users import BorrowToUsers
from app.schemas.genres import GenreCreate
from app.schemas.user import UserCreate
from app.schemas.authors import  AuthorCreate
from app.schemas.penalties import PenaltyCreate
from app.models.books import Book
from app.schemas.books import BookCreate, BookDisplay
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session as SessionType

from app.dependencies import get_db
from app.schemas.example import ExampleCreate
from app.models.example import Example
from typing import List, Optional
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

@router.get("/books/", response_model=List[BookDisplay])
def get_books(isbn : str = "", db : SessionType = Depends(get_db)):
    if isbn:
        return db.query(Book).filter(Book.isbn == isbn)
    else:
        return db.query(Book).all()

@router.get("/books/recommended/", response_model=List[BookDisplay])
async def get_available_books(genre: Optional[str] = None, db : SessionType = Depends(get_db)):
    recommended = []
    if genre != None :
        books_by_genre = db.query(Book).join(BookGenreAssociation).join(Genre).filter(Genre.title == genre)
        recommended += books_by_genre
    return recommended

@router.get("/books/available/", response_model=BookDisplay)
async def get_available_books(isbn: Optional[str] = None, title:Optional[str] = None, db : SessionType = Depends(get_db)):
    if isbn == None and title == None:
        raise HTTPException(status_code=400, detail="must provide title or isbn")

    targeted_book : Book = db.query(Book).filter(Book.isbn == isbn).first() if isbn else \
                            db.query(Book).filter(Book.title == title).first()
    
    times_borrowed : int = db.query(BorrowToUsers).filter(BorrowToUsers.book_id == targeted_book.book_id).count()
    book_available: bool = targeted_book.number_of_copies > times_borrowed
    
    if book_available:
        return targeted_book
    else:
        raise HTTPException(status_code=404, detail="Book not available")

@router.post("/books", response_model=BookDisplay)
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

@router.post("/books/borrow", response_model=BorrowToUsersCreate)
def borrow_book(borrow : BorrowToUsersCreate,  db: SessionType = Depends(get_db)):
    db_borrow = BorrowToUsers(book_id=borrow.book_id, user_id=borrow.user_id, borrowed_from = borrow.borrowed_from, borrowed_until=borrow.borrowed_until)
    db.add(db_borrow)
    db.commit()
    db.refresh(db_borrow)
    return db_borrow    

@router.get("/authors/", response_model= List[AuthorCreate])
def get_author(name :Optional[str] = None, db: SessionType = Depends(get_db)):
    if name is None:
        return db.query(Author).all()
    else:
        return db.query(Author).filter(Author.name == name).all()

@router.post("/authors", response_model= AuthorCreate)
def create_author(author: AuthorCreate, db: SessionType = Depends(get_db)):
    db_author = Author(name=author.name, birth_date=author.birth_date, volumes_published=author.volumes_published)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author    

@router.get("/penalty/", response_model= PenaltyCreate)
def get_penalty(db: SessionType = Depends(get_db)):
    return db.query(Penalty).all()

@router.post("/penalty", response_model= PenaltyCreate)
def create_penalty(penalty: PenaltyCreate, db: SessionType = Depends(get_db)):
    db_penalty : Penalty = Penalty(
        title=penalty.title,
        reason=penalty.reason,
        number_of_weeks=penalty.number_of_weeks
        )
    db.add(db_penalty)
    db.commit()
    db.refresh(db_penalty)
    return db_penalty

@router.get("/genre/", response_model= GenreCreate)
def get_genre(db: SessionType = Depends(get_db)):
    return db.query(Genre).all()

@router.post("/genre", response_model= GenreCreate)
def create_genre(genre: GenreCreate, db: SessionType = Depends(get_db)):
    db_genre : Genre = Genre(
        title=genre.title
        )
    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)
    return db_genre

@router.get("/user/", response_model= UserCreate)
def get_user(db: SessionType = Depends(get_db)):
    return db.query(Genre).all()

@router.post("/user", response_model= UserCreate)
def create_user(user: UserCreate, db: SessionType = Depends(get_db)):
    db_user : User = User(
        username=user.username, 
        first_name=user.first_name,
        last_name=user.last_name,
        password=user.password,
        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/author_book_association", response_model= WrittenByCreate)
def create_author_book_association(writtenby: WrittenByCreate, db: SessionType = Depends(get_db)):
    if len(db.query(Book).filter(Book.book_id == writtenby.book_id).all()) ==0 :
        raise HTTPException(status_code=404, detail="No book with that id")
    if len(db.query(Author).filter(Author.author_id == writtenby.author_id).all()) ==0 :
        raise HTTPException(status_code=404, detail="No author with that id")
    
    db_writtenby = WrittenBy(book_id=writtenby.book_id, author_id=writtenby.author_id)
    db.add(db_writtenby)
    db.commit()
    db.refresh(db_writtenby)
    return db_writtenby
