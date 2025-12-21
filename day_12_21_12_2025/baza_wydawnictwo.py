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

# new_author = Author(name="Adam Mickiewicz")
# new_publisher = Publisher(name="Librairie Polonaise")
# new_book = Book(title="Pan Tadeusz", author=new_author, publisher=new_publisher)
#
# session.add_all(
#     [new_author,new_publisher,new_book]
# )


# new_author = Author(name="Jan Kowalski")
# new_publisher = Publisher(name="Wydawnictwo i Spółka")
# new_book = Book(title="Python dla średniozaawansowanych", author=new_author, publisher=new_publisher)
#
# session.add_all(
#     [new_author, new_publisher, new_book]
# )

# odczytac z bazy authorów i publisherów
# z auyora odczytac jego ksiazki
# z wydawcy odczytac ksiazki
# z ksiązek autora


# session.commit()

authors = session.query(Author).all()
print(authors)
for author in authors:
    print(f'Author: {author.name}')
    for book in author.books:
        print(f"Ksiązka: {book.title}, Wydawca: {book.publisher.name}")

# Author: Adam Mickiewicz
# Ksiązka: Pan Tadeusz, Wydawca: Librairie Polonaise
# Author: Adam Mickiewicz
# Ksiązka: Pan Tadeusz, Wydawca: Librairie Polonaise
# Author: Jan Kowalski
# Ksiązka: Python dla średniozaawansowanych, Wydawca: Wydawnictwo i Spółka
session.close()
