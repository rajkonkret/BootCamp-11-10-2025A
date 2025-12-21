from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

# docker run -d --name mysql_db1 -e MYSQL_ROOT_PASSWORD=abc123 -e MYSQL_DATABASE=baza -p 3306:3306 mysql:8.0

# pip install pymysql - musimy doinstalowac pymysql
# pip install cryptography - mysql wymaga szyfrowania haseł
DATABASE_URI = "mysql+pymysql://root:abc123@localhost:3306/baza"

engine = create_engine(DATABASE_URI, echo=True)
Base = declarative_base()


# model, encja

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True)

    posts = relationship("Post", back_populates="user")


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(String(500))
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates='posts')


# tworzenie tabel
Base.metadata.create_all(engine)
