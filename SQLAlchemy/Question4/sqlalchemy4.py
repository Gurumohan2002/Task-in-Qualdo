from urllib.parse import quote
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
import sqlalchemy as db 
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

password = "Guru@6307"
encoded_password = quote(password)

engine = db.create_engine(f"mysql+pymysql://root:{encoded_password}@localhost/sqltask")

class Orders(Base): 
    __tablename__ = 'orders'
    ord_no = db.Column(db.Integer(), primary_key=True)
    purch_amt = db.Column(db.Numeric())
    ord_date = db.Column(db.Date())
    customer_id = db.Column(db.Integer())
    salesman_id = db.Column(db.Integer())  

    def __init__(self,ord_no,purch_amt,ord_date,customer_id,salesman_id):
        self.ord_no=ord_no
        self.purch_amt=purch_amt
        self.ord_date=ord_date
        self.customer_id=customer_id
        self.salesman_id=salesman_id
        

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
        
class customer(Base):
    __tablename__='customer'
    customer_id = db.Column(db.Integer(),primary_key=True)
    cust_name= db.Column(db.VARCHAR(255))
    city = db.Column(db.VARCHAR(255))
    grade = db.Column(db.Integer())    
    salesman_id = db.Column(db.Integer())
    
    def __init__(self,customer_id,cust_name,city,grade,salesman_id):
        self.salesman_id=salesman_id
        self.cust_name=cust_name
        self.city=city
        self.customer_id=customer_id
        self.grade=grade
                
Session = sessionmaker(bind=engine)
session = Session()
print("\n")                                        
result = session.query(Orders).all()

print("Ord_No  |  Purch_amt   |  Ord_date     |  Customer_id   |  Salesman_id")
for a in result:
    print(a.ord_no, "  |", a.purch_amt, "         |", a.ord_date, "   |",a.customer_id, "          |",a.salesman_id)


print("\n")                                        
result = session.query(Salesman).all()

print("salesman_id  |  name   |  city   | commission")
for a in result:
    print(a.salesman_id, "  |", a.name, "         |", a.city, "   |",a.commission)
    
    
print("\n")

result = session.query(customer).all()

print("customer_id |  cust_name         |   city         |  grade      |   salesman_id")
for a in result:
    print(a.customer_id, "    |  ",a.cust_name,"      |   " , a.city,"  |   " , a.grade, "     |  " ,a.salesman_id )

print("\n")
result1 = session.query(customer.cust_name,customer.city,customer.grade,Salesman.name,Orders.ord_no,Orders.ord_date,Orders.purch_amt).filter(Salesman.salesman_id ==customer.salesman_id).filter(customer.customer_id==Orders.customer_id).filter(Orders.purch_amt>2000).having(customer.grade.isnot(None))
print("Select c.cust_name,c.city,c.grade,s.name,o.ord_no,o.ord_date,o.purch_amt from salesman as s inner join  customer as c on s.salesman_id=c.salesman_id inner join orders as o on c.customer_id=o.customer_id having c.grade is not null and o.purch_amt>2000;")
   
for a in result1:
    print(a.cust_name,"   " , a.city,  "   " , a.grade,"   " ,a.name, "    " ,a.ord_no,"    " , a.ord_date, "   ",a.purch_amt)  


print("\n")
result2 = session.query(customer.cust_name,customer.city,Orders.ord_no,Orders.ord_date,Orders.purch_amt.label("Order_Amount")).filter(customer.customer_id==Orders.customer_id).filter(customer.grade.isnot(None))
print("SELECT c.cust_name, c.city, o.ord_no, o.ord_date, o.purch_amt as Order_Amount FROM customer AS c INNER JOIN orders AS o ON c.customer_id = o.customer_id where c.grade is not null;")
   
for a in result2:
    print(a.cust_name,"   " , a.city,  "   ",a.ord_no,"    " , a.ord_date, "   ",a.Order_Amount)  