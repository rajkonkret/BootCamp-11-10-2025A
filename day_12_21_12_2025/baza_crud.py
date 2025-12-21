# CRUD - CREATE, READ, UPDATE, DELETE
# Działanie	Instrukcja  SQL	    HTTP	            DDS
# Create	            INSERT	PUT / POST	        write
# Read (Retrieve)	    SELECT	GET	                read / take
# Update	            UPDATE	POST / PUT / PATCH	write
# Delete (Destroy)	    DELETE	DELETE	            dispose

# od wersji 2.0 sqlalchemy podejście deklaratywny
from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
import sqlalchemy

print(sqlalchemy.__version__)  # 2.0.44

DB_URL = "sqlite:///example_orm.db"


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"user(id={self.id}, name={self.name!r}, email={self.email!r}"

# tworzenie tabel
engine = create_engine(DB_URL, echo=False)
Base.metadata.create_all(engine)
