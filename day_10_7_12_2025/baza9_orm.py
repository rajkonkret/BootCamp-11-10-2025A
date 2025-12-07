# ORM - ORM (Object-Relational Mapping,
# czyli mapowanie obiektowo-relacyjne) to technika programowania pozwalająca
# na komunikację między obiektowymi językami programowania (jak C#, Java, Python),
# a relacyjnymi bazami danych, przekształcając dane w obiekty,
# które programista może łatwo manipulować bez pisania skomplikowanych zapytań SQL

# pip install sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, text
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


# klasy odwzorowujące tabele - encja (model)
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):  # sposób wypisywania obiektu
        return f"<User(name={self.name}, age={self.age}"


engine = create_engine('sqlite:///my_database.db', echo=True)

# Tworzenie tabel w bazie danych
Base.metadata.create_all(engine)
# CREATE TABLE users (
# 	id INTEGER NOT NULL,
# 	name VARCHAR,
# 	age INTEGER,
# 	PRIMARY KEY (id)
# )

# tworzenie sesji
# za pomocą sesji łaczymy się i porozumiewamy z bazą danych
Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name="Jan Kowalski", age=30)
# INSERT INTO users (name, age) VALUES (?, ?)
# session.add(new_user)

session.commit()
session.close()

users = session.query(User).all()
# SELECT users.id AS users_id, users.name AS users_name, users.age AS users_age
# FROM users
for user in users:
    print(user)
    # <User(name=Jan Kowalski, age=30
    # <User(name=Jan Kowalski, age=30
    print(f"Imię: {user.name}, wiek: {user.age}")
    # <User(name=Jan Kowalski, age=30
    # Imię: Jan Kowalski, wiek: 30
    # <User(name=Jan Kowalski, age=30
    # Imię: Jan Kowalski, wiek: 30
    # <User(name=Jan Kowalski, age=30
    # Imię: Jan Kowalski, wiek: 30

result = session.execute(text("SELECT * FROM users;"))
print(result)  # <sqlalchemy.engine.cursor.CursorResult object at 0x107a85550>
for row in result:
    print(row)
    print(type(row))  # <class 'sqlalchemy.engine.row.Row'>
    # (1, 'Jan Kowalski', 30)
    # (2, 'Jan Kowalski', 30)
    # (3, 'Jan Kowalski', 30)

stmt = text("SELECT * FROM users;")
users = session.query(User).from_statement(stmt).all()

for user in users:
    print(type(user))
    print(user.name)
    # <class '__main__.User'>
    # Jan Kowalski
    # <class '__main__.User'>
    # Jan Kowalski
    # <class '__main__.User'>
    # Jan Kowalski
# w wyniku mamy obiekty a nie krotki
