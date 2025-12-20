# Mapowanie obiektowo-relacyjne (ang. Object-Relational Mapping – ORM)
# – sposób odwzorowania obiektowej architektury systemu informatycznego na bazę danych
# (lub inny element systemu) o relacyjnym charakterze.

# sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URI = "sqlite:///sprawdzenie.db"

# engine = create_engine(DATABASE_URI)
engine = create_engine(DATABASE_URI, echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = "new_users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

user1 = User(name="Anna", age=25)
user2 = User(name="Tomek", age=35)

session.add_all([user1, user2])
# INSERT INTO new_users (name, age) VALUES (?, ?) RETURNING id
session.commit()

users = session.query(User).all()
# SELECT new_users.id AS new_users_id, new_users.name AS new_users_name, new_users.age AS new_users_age
# FROM new_users
for user in users:
    print(f"id: {user.id}, name: {user.name}, age: {user.age}")
# id: 1, name: Anna, age: 25
# id: 2, name: Tomek, age: 35
# id: 3, name: Anna, age: 25
# id: 4, name: Tomek, age: 35
# id: 5, name: Anna, age: 25
# id: 6, name: Tomek, age: 35

# update
user_to_update = session.query(User).filter_by(name="Anna").first() # pierwszy element
user_to_update.age = 27
session.commit()

session.close()
