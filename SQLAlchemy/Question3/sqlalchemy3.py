from urllib.parse import quote
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
import sqlalchemy as db 
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

password = "Guru@6307"
encoded_password = quote(password)

engine = db.create_engine(f"mysql+pymysql://root:{encoded_password}@localhost/sqltask")

class Employee_history(Base): 
    __tablename__ = 'employee_history_a'
    id = db.Column(db.Integer(),primary_key=True)
    employee_id = db.Column(db.Integer())
    start_date = db.Column(db.Date())
    end_date = db.Column(db.Date())
    job_id = db.Column(db.VARCHAR(50))
    department_id =db.Column(db.INTEGER())
    
    def __init__(self,id,employee_id,start_date,end_date,job_id,department_id):
        self.id=id
        self.employee_id=employee_id
        self.start_date=start_date
        self.end_date=end_date 
        self.job_id = job_id
        self.department_id=department_id
        
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()                                  
print("\n")                                       
result = session.query(Employee_history).all()
print("employee_id |  start_date  |  end_date  | job_id  | department")
for a in result:
    print(a.employee_id, "  |", a.start_date, "         |", a.end_date, "   |", a.job_id,"  | ", a.department_id)  
    
print("\n")
result1 = session.query(Employee_history.employee_id).group_by(Employee_history.employee_id).having(func.count(distinct(Employee_history.job_id))>1)

print("SELECT * from salesman where commission BETWEEN 0.10 and 0.12;")
print("employee_id ")  
for a in result1:
     print(a.employee_id)

print("\n")
