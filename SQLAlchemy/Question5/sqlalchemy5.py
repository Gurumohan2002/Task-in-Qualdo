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

class Employee(Base): 
    __tablename__ = 'employee'
    emp_idno = db.Column(db.Integer(),primary_key=True)
    emp_fname = db.Column(db.VARCHAR(255))
    emp_lname = db.Column(db.VARCHAR(255))
    emp_dept =db.Column(db.INTEGER())
    
    def __init__(self,emp_idno,emp_fname,emp_lname,emp_dept):
        self.emp_idno=emp_idno
        self.emp_fname=emp_fname
        self.emp_lname=emp_lname
        self.emp_dept=emp_dept

class Department(Base): 
    __tablename__ = 'department'
    dpt_code = db.Column(db.Integer(),primary_key=True)
    dpt_name = db.Column(db.VARCHAR(255))
    dpt_allotment =db.Column(db.INTEGER())
    
    def __init__(self,dpt_code,dpt_name,dpt_allotment):
        self.dpt_name=dpt_name
        self.dpt_allotment=dpt_allotment
        self.dpt_code=dpt_code

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()                                  
print("\n")                                       
result = session.query(Employee).all()
print("emp_idno |  emp_fname  |  emp_lname  | dpt_allotment")
for a in result:
    print(a.emp_idno, "  |", a.emp_fname, "    |", a.emp_lname, "   |", a.emp_dept)  
    
print("\n")

result=session.query(Department).all()
print("dpt_code      |   dpt_name   | dpt_allotment")
for a in result:
    print(a.dpt_code,"   |   " , a.dpt_name, "  |  " , a.dpt_allotment)

print("\n")
result1 = session.query(Employee.emp_fname,Employee.emp_lname).filter(Employee.emp_dept==Department.dpt_code).filter(Department.dpt_allotment>50000)

print("Select e.emp_fname,e.emp_lname from employee as e join department as d on e.emp_dept=d.dpt_code where dpt_allotment>50000;")
print("emp_fname   |    emp_lname  ")  
for a in result1:
     print(a.emp_fname, "    | " , a.emp_lname)

print("\n")

subquery1 = (session.query(func.min(Department.dpt_allotment)).scalar_subquery())
subquery2 = (session.query(func.min(Department.dpt_allotment)).filter(Department.dpt_allotment > subquery1).scalar_subquery())
query = session.query(Employee.emp_fname, Employee.emp_lname).filter(Employee.emp_dept == Department.dpt_code).filter(Department.dpt_allotment.in_(session.query(subquery2)))

for a in query:
    print(a.emp_fname, "    | " , a.emp_lname)

print("\n")