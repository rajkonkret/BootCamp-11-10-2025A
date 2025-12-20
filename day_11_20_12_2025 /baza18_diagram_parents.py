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

# parent = Parent(name="Rodzic")
# child1 = Child(name="Dziecko 1", parent=parent)
# child2 = Child(name="Dziecko 2", parent=parent)
#
# session.add_all(
#     [parent, child1, child2]
# )

# session.commit()

our_parent = session.query(Parent).all()
print(our_parent)  # [<__main__.Parent object at 0x108cbc440>]

our_parent_filtered = session.query(Parent).filter_by(name="Rodzic").first()
print(f"Rodzic: {our_parent_filtered.name}")  # Rodzic: Rodzic
# session.close()

children = our_parent_filtered.children
for child in children:
    print(f'Dziecko: {child.name}')
    print(f"Rodzic: {child.parent.name}")
session.close()
# 2025-12-20 13:47:30,404 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-20 13:47:30,405 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("parents")
# 2025-12-20 13:47:30,405 INFO sqlalchemy.engine.Engine [raw sql] ()
# 2025-12-20 13:47:30,405 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("children")
# 2025-12-20 13:47:30,405 INFO sqlalchemy.engine.Engine [raw sql] ()
# 2025-12-20 13:47:30,405 INFO sqlalchemy.engine.Engine COMMIT
# 2025-12-20 13:47:30,407 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2025-12-20 13:47:30,407 INFO sqlalchemy.engine.Engine SELECT parents.id AS parents_id, parents.name AS parents_name
# FROM parents
# 2025-12-20 13:47:30,407 INFO sqlalchemy.engine.Engine [generated in 0.00005s] ()
# [<__main__.Parent object at 0x108f20440>]
# 2025-12-20 13:47:30,408 INFO sqlalchemy.engine.Engine SELECT parents.id AS parents_id, parents.name AS parents_name
# FROM parents
# WHERE parents.name = ?
#  LIMIT ? OFFSET ?
# 2025-12-20 13:47:30,408 INFO sqlalchemy.engine.Engine [generated in 0.00006s] ('Rodzic', 1, 0)
# Rodzic: Rodzic
# 2025-12-20 13:47:30,409 INFO sqlalchemy.engine.Engine SELECT children.id AS children_id, children.name AS children_name, children.parent_id AS children_parent_id
# FROM children
# WHERE ? = children.parent_id
# 2025-12-20 13:47:30,409 INFO sqlalchemy.engine.Engine [generated in 0.00005s] (1,)
# Dziecko: Dziecko 1
# Rodzic: Rodzic
# Dziecko: Dziecko 2
# Rodzic: Rodzic
# 2025-12-20 13:47:30,409 INFO sqlalchemy.engine.Engine ROLLBACK
