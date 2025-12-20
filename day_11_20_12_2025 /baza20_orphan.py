# Jeden-do-jednego (1:1): Jeden rekord w tabeli A jest powiązany z maksymalnie jednym rekordem w tabeli B
# (np. pracownik i jego samochód służbowy, jeśli ma tylko jeden).
# ----
# Jeden-do-wielu (1:N): Jeden rekord w tabeli A może być powiązany z wieloma rekordami w tabeli B
# (np. jeden klient ma wiele zamówień).
# ----
# Wiele-do-wielu (N:M): Wiele rekordów z tabeli A może być powiązanych z wieloma rekordami z tabeli B
# (np. wiele produktów może występować w wielu zamówieniach).
# Wymaga to często dodatkowej tabeli pośredniczącej (tabeli łączącej)

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

DATABASE_URI = "sqlite:///adress_book.db"
# engine = create_engine(DATABASE_URI, echo=True)
engine = create_engine(DATABASE_URI, echo=False)

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(String)

    addresses = relationship(
        'Address',
        back_populates='person',
        order_by='Address.email',
        cascade='all, delete-orphan'
    )

    # jak zmienie w Person to i w adress zmiany pojda automatycznie
    # delete-orphan - usuwanie sierot

    def __repr__(self):
        return f"{self.name} (id={self.id})"


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    person_id = Column(ForeignKey('person.id'))
    person = relationship("Person", back_populates="addresses")

    def __repr__(self):
        return self.email


Base.metadata.create_all(engine)  # Stworzenie tabel w bazie danych

Session = sessionmaker(bind=engine)
session = Session()

session.close()
