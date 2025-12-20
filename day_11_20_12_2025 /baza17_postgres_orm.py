# Mapowanie obiektowo-relacyjne (ang. Object-Relational Mapping – ORM)
# – sposób odwzorowania obiektowej architektury systemu informatycznego na bazę danych
# (lub inny element systemu) o relacyjnym charakterze.

# sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URI = "sqlite:///sprawdzenie.db"

engine = create_engine(DATABASE_URI)
Base = declarative_base()


class User(Base):
    __tablename__ = "new_users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


Base.metadata.create_all(engine)
