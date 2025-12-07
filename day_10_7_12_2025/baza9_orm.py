# ORM - ORM (Object-Relational Mapping,
# czyli mapowanie obiektowo-relacyjne) to technika programowania pozwalająca
# na komunikację między obiektowymi językami programowania (jak C#, Java, Python),
# a relacyjnymi bazami danych, przekształcając dane w obiekty,
# które programista może łatwo manipulować bez pisania skomplikowanych zapytań SQL

# pip install sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.orm import sessionmaker, declarative_base
