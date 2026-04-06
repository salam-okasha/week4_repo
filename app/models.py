from sqlalchemy import MetaData, Table, Column, Integer, String

metadata = MetaData()

students = Table(
   "students",
   metadata,
   Column("student_id", Integer, primary_key=True),
   Column("student_name", String(100)),
)

from db import engine
from models import students
from sqlalchemy import insert, select
from sqlalchemy.exc import SQLAlchemyError


def insert_student():
   with engine.connect() as conn:
       try:
           stmt = insert(students).values(student_name="Haya")
           result = conn.execute(stmt)
           conn.commit()
           return result.inserted_primary_key[0]

       except SQLAlchemyError:
           conn.rollback()
           raise


def get_all_students():
   with engine.connect() as conn:
       try:
           query = select(students)
           result = conn.execute(query)

           data = [dict(row._mapping) for row in result]
           return data

       except SQLAlchemyError:
           conn.rollback()
           raise
