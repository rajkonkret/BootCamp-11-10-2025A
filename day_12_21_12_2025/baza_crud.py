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
        return f"user(id={self.id}, name={self.name!r}, email={self.email!r})"


# tworzenie tabel
engine = create_engine(DB_URL, echo=False)
Base.metadata.create_all(engine)


# create
def create_user(session: Session, name: str, email: str):
    session.add(User(name=name, email=email))


# read
def get_users(session: Session):
    return session.query(User).all()


# update
def update_email(session: Session, user_id: int, new_email: str):
    user = session.get(User, user_id)
    if user:
        user.email = new_email


# delete
def delete_user(session: Session, user_id: int):
    user = session.get(User, user_id)
    if user:
        session.delete(user)


def main():
    with Session(engine) as session:
        # create
        # create_user(session, "Margaret Hamilton", "margaret@nasa.gov")
        # create_user(session, "Linus Tornvalds", "linus@kernel.org")
        #
        # session.commit()

        # read
        print("== All users ==")
        print(get_users(session))

        # update
        update_email(session, 1, "margaret@pollo.guide")
        session.commit()
        print("\n== After email update ==")
        print(get_users(session))

        #delete
        delete_user(session, 2)
        session.commit()
        print("\n== After delete ==")
        print(get_users(session))


if __name__ == '__main__':
    main()
# == All users ==
# [user(id=1, name='Margaret Hamilton', email='margaret@pollo.guide'), user(id=2, name='Linus Tornvalds', email='linus@kernel.org')]
#
# == After email update ==
# [user(id=1, name='Margaret Hamilton', email='margaret@pollo.guide'), user(id=2, name='Linus Tornvalds', email='linus@kernel.org')]
#
# == After delete ==
# [user(id=1, name='Margaret Hamilton', email='margaret@pollo.guide')]