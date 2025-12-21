from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

DATABASE_URI = "sqlite:///publishers.db"
Base = declarative_base()


# Author, Book, Publisher

class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    books = relationship("Book", back_populates="author")


class Publisher(Base):
    __tablename__ = 'publishers'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    books = relationship("Book", back_populates='publisher')


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String)

    author_id = Column(Integer, ForeignKey('authors.id'))
    publisher_id = Column(Integer, ForeignKey('publishers.id'))

    author = relationship("Author", back_populates='books')
    publisher = relationship("Publisher", back_populates='books')


engine = create_engine(DATABASE_URI)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
