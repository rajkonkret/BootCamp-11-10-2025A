# Relacja wiele do wielu M:N

from asyncpg.cluster import Cluster
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

DATABASE_URI = 'sqlite:///kursy.db'

Base = declarative_base()

# definicja tabeli asocjacyjnej
# konieczna w relacji wiele do wielu
# nazwa tabeli: student_course
# kolumny: student_id, course_id
student_course_table = Table(
    'student_course',
    Base.metadata,
    Column("student_id", Integer, ForeignKey('students.id'), primary_key=True),
    Column("course_id", Integer, ForeignKey('courses.id'), primary_key=True)
)


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    courses = relationship("Course", secondary=student_course_table, back_populates="students")


class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    students = relationship("Student", secondary=student_course_table, back_populates="courses")


engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)
