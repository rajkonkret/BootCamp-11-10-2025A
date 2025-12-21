from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from day_12_21_12_2025.baza_dodatkowe.baza_krok1 import User, Post

# docker run -d --name mysql_db1 -e MYSQL_ROOT_PASSWORD=abc123 -e MYSQL_DATABASE=baza -p 3306:3306 mysql:8.0

# pip install pymysql - musimy doinstalowac pymysql
# pip install cryptography - mysql wymaga szyfrowania haseł
DATABASE_URI = "mysql+pymysql://root:abc123@localhost:3306/baza"

engine = create_engine(DATABASE_URI, echo=True)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

try:
    new_user = User(name="Jan kowalski", email="jan.kowalski@wp.pl")
    session.add(new_user)
    # print(5 / 0)
    new_post = Post(title="Pierwszy post", content="To jest treść pierwszego posta", user=new_user)
    session.add(new_post)

    session.commit()
except Exception as e:
    print("Bład:", e)
    session.rollback()  # wycofanie zmian w przypadku błedu

finally:
    session.close()
