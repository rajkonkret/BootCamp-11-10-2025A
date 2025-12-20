# Na podstawie diagramu wykonac strukture kals odpowiadająca modelowi w bazie danych


from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

# DATABASE_URI = "sqlite:///sprawdzenie.db"
DATABASE_URI = "sqlite:///parents_database.db"
# DATABASE_URI = "postgresql://myuser:mypassword@localhost/mydatabase"

# engine = create_engine(DATABASE_URI)
engine = create_engine(DATABASE_URI, echo=True)
Base = declarative_base()


# relacja jeden do wielu, 1:N
class Parent(Base):
    __tablename__ = 'parents'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))  # maksymalna długosć tekstu
    children = relationship("Child", backref='parent')
    # backref - tworzy pole parent w obiekcie klasy Child


class Child(Base):
    __tablename__ = 'children'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    parent_id = Column(Integer, ForeignKey('parents.id'))

    def __repr__(self):
        return f'id={self.id}, name={self.name}'


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
