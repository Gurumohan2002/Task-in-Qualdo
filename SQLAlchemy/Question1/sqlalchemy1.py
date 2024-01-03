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
        
Session = sessionmaker(bind=engine)
session = Session()
print("\n")                                        
result = session.query(Orders).all()

print("Ord_No  |  Purch_amt   |  Ord_date     |  Customer_id   |  Salesman_id")
for a in result:
    print(a.ord_no, "  |", a.purch_amt, "         |", a.ord_date, "   |",a.customer_id, "          |",a.salesman_id)
    
    
print("\n")
result1 = session.query(Orders.salesman_id).filter(Orders.purch_amt<2000).group_by(Orders.salesman_id).order_by(func.max(Orders.purch_amt).desc()).limit(5)

print("Select salesman_id from orders where purch_amt<2000 group by salesman_id order by max(purch_amt) desc limit 5;")
print("Salesman_id")     
for a in result1:
    print(a.salesman_id)

print("\n")
result2=session.query(Orders.salesman_id).filter(Orders.purch_amt<2000).group_by(Orders.salesman_id).order_by(func.max(Orders.purch_amt).asc()).limit(5)
print("Select salesman_id from orders where purch_amt<2000 group by salesman_id order by max(purch_amt) asc limit 5;")
print("Salesman_id")     
for a in result2:
    print(a.salesman_id)

print("\n")