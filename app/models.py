from sqlalchemy import MetaData, Table, Column, Integer, String
from app.db import engine
from sqlalchemy import insert, select
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

metadata = MetaData()

students = Table(
   "students",
    metadata,
    Column("student_id", Integer, primary_key=True),
    Column("student_name", String(100)),
    Column("email",String(120),unique=True)
)

def insert_student(student_name,email):
   with engine.connect() as conn:
       try:
           stmt = insert(students).values(student_name=student_name, email= email)
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
       
insert_student(student_name="sara",email="sara155@gmail.com")



