# Jeden-do-jednego (1:1): Jeden rekord w tabeli A jest powiązany z maksymalnie jednym rekordem w tabeli B
# (np. pracownik i jego samochód służbowy, jeśli ma tylko jeden).
# ----
# Jeden-do-wielu (1:N): Jeden rekord w tabeli A może być powiązany z wieloma rekordami w tabeli B
# (np. jeden klient ma wiele zamówień).
# ----
# Wiele-do-wielu (N:M): Wiele rekordów z tabeli A może być powiązanych z wieloma rekordami z tabeli B
# (np. wiele produktów może występować w wielu zamówieniach).
# Wymaga to często dodatkowej tabeli pośredniczącej (tabeli łączącej)

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

DATABASE_URI = "sqlite:///adress_book.db"
# engine = create_engine(DATABASE_URI, echo=True)
engine = create_engine(DATABASE_URI, echo=False)

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(String)

    addresses = relationship(
        'Address',
        back_populates='person',
        order_by='Address.email',
        cascade='all, delete-orphan'
    )

    # jak zmienie w Person to i w adress zmiany pojda automatycznie
    # delete-orphan - usuwanie sierot

    def __repr__(self):
        return f"{self.name} (id={self.id})"


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    person_id = Column(ForeignKey('person.id'))
    person = relationship("Person", back_populates="addresses")

    def __repr__(self):
        return self.email


Base.metadata.create_all(engine)  # Stworzenie tabel w bazie danych

Session = sessionmaker(bind=engine)
session = Session()

anakin = Person(name='Anakin', age=38)

session.add(anakin)

anakin1 = Person(name="Anakin Anakin", age=38)
anakin1.addresses = [Address(email='anakin@wp.pl')]

# dodanie anakin1
# cascade=all - zapisało i obiekt Person i obiekt Adress przypisane do tego Person
session.add(anakin1)

obi = Person(name="Obi Wan Kenobi", age=45)
obi.addresses = [
    Address(email='obik@wp.pl'),
    Address(email='waaka@wp.pl')
]

# dodanie anakin1
# cascade=all - zapisało i obiekt Person i obiekt Adress przypisane do tego Person
session.add(obi)

chewee = Person(name="Chewbacca", age=190)
chewee.addresses = [
    Address(email='chewbacca@wp.pl'),
    Address(email='chewee@wp.pl')
]

# dodanie anakin1
# cascade=all - zapisało i obiekt Person i obiekt Adress przypisane do tego Person
session.add(chewee)

session.commit()

all_ = session.query(Person).all()
print(all_)
# [Anakin (id=1), Anakin (id=2), Anakin Anakin (id=3), Anakin (id=4), Anakin Anakin (id=5),
# Obi Wan Kenobi (id=6), Anakin (id=7), Anakin Anakin (id=8), Obi Wan Kenobi (id=9),
# Chewbacca (id=10), Anakin (id=11), Anakin Anakin (id=12), Obi Wan Kenobi (id=13),
# Chewbacca (id=14), Anakin (id=15), Anakin Anakin (id=16), Obi Wan Kenobi (id=17), Chewbacca (id=18)]

first = session.query(Person).first()
print(first)  # Anakin (id=1)
print(type(first))  # <class '__main__.Person'>
print(first.name, first.age)  # Anakin 38

# SELECT person.id AS person_id, person.name AS person_name, person.age AS person_age
# FROM person
# WHERE person.name LIKE ?
obi_list = session.query(Person).filter(
    Person.name.like('Obi%')  # WHERE person.name LIKE ?
).all()
print(obi_list)

chwee_list = session.query(Person).filter(
    Person.name.like('Che%')
).all()
print(chwee_list)
# [Chewbacca (id=10), Chewbacca (id=14), Chewbacca (id=18), Chewbacca (id=22),
# Chewbacca (id=26), Chewbacca (id=30), Chewbacca (id=34)]

for chewee in chwee_list:
    print(f"{chewee.id=}, {chewee.name=}, {chewee.addresses=}")
session.close()
# chewee.id=10, chewee.name='Chewbacca', chewee.addresses=[chewbacca@wp.pl, chewee@wp.pl]
# chewee.id=14, chewee.name='Chewbacca', chewee.addresses=[chewbacca@wp.pl, chewee@wp.pl]
# chewee.id=18, chewee.name='Chewbacca', chewee.addresses=[chewbacca@wp.pl, chewee@wp.pl]
# chewee.id=22, chewee.name='Chewbacca', chewee.addresses=[chewbacca@wp.pl, chewee@wp.pl]
# chewee.id=26, chewee.name='Chewbacca', chewee.addresses=[chewbacca@wp.pl, chewee@wp.pl]
# chewee.id=30, chewee.name='Chewbacca', chewee.addresses=[chewbacca@wp.pl, chewee@wp.pl]
# chewee.id=34, chewee.name='Chewbacca', chewee.addresses=[chewbacca@wp.pl, chewee@wp.pl]
# chewee.id=38, chewee.name='Chewbacca', chewee.addresses=[chewbacca@wp.pl, chewee@wp.pl]
