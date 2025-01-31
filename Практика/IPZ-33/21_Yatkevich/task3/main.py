from typing import List, Optional
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import Boolean, Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

app = FastAPI()
DATABASE_URL = "sqlite:///./library.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class BookDB(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    genre = Column(String, index=True)
    year = Column(Integer)
    is_available = Column(Boolean, default=True)


Base.metadata.create_all(bind=engine)


class Book(BaseModel):
    id: int
    title: str
    author: str
    genre: str
    year: int
    is_available: bool

    class Config:
        from_attributes = True


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/books", response_model=List[Book])
def get_books(
    genre: Optional[str] = None,
    author: Optional[str] = None,
    available: Optional[bool] = None,
    db: Session = Depends(get_db),
):
    query = db.query(BookDB)
    if genre:
        query = query.filter(BookDB.genre == genre)
    if author:
        query = query.filter(BookDB.author == author)
    if available is not None:
        query = query.filter(BookDB.is_available == available)
    return query.all()


@app.post("/books", response_model=Book)
def add_book(book: Book, db: Session = Depends(get_db)):
    db_book = db.query(BookDB).filter(BookDB.id == book.id).first()
    if db_book:
        raise HTTPException(status_code=400, detail="Book ID already exists")
    new_book = BookDB(**book.model_dump())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book, db: Session = Depends(get_db)):
    db_book = db.query(BookDB).filter(BookDB.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    for key, value in updated_book.model_dump().items():
        setattr(db_book, key, value)
    db.commit()
    db.refresh(db_book)
    return db_book


@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(BookDB).filter(BookDB.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(db_book)
    db.commit()
    return {"message": "Book deleted successfully"}
