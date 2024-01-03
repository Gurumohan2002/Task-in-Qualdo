from operator import and_
from urllib.parse import quote
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
import sqlalchemy as db 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *

Base = declarative_base()

password = "Guru@6307"
encoded_password = quote(password)

engine = db.create_engine(f"mysql+pymysql://root:{encoded_password}@localhost/sqltask")

class Salesman(Base): 
    __tablename__ = 'salesman'
    salesman_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.VARCHAR(255))
    city = db.Column(db.VARCHAR(255))
    commission = db.Column(db.REAL())

    def __init__(self,salesman_id,name,city,commission):
        self.salesman_id=salesman_id
        self.name=name
        self.city=city
        self.commission=commission
        
Session = sessionmaker(bind=engine)
session = Session()
print("\n")                                        
result = session.query(Salesman).all()

print("salesman_id  |  name   |  city   | commission")
for a in result:
    print(a.salesman_id, "  |", a.name, "         |", a.city, "   |",a.commission)
    
    
print("\n")
result1 = session.query(Salesman).filter(and_(Salesman.commission>=0.10,Salesman.commission<=0.12))

print("SELECT * from salesman where commission BETWEEN 0.10 and 0.12;")
print("salesman_id  |  name   |  city   | commission")  
for a in result1:
     print(a.salesman_id, "  |", a.name, "         |", a.city, "   |",a.commission)

print("\n")
result2=session.query(func.avg(Salesman.commission)).filter(and_(Salesman.commission>=0.12,Salesman.commission<=0.14))
print("SELECT AVG(commission) from salesman where commission BETWEEN 0.12 and 0.14;")
print("Average(commission)")     
for a in result2:
    print(a)

print("\n")