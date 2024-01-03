import datetime
from flask import Flask,Blueprint
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote

app = Flask(__name__)

password = "Guru@2607"
encoded_password = quote(password)

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://postgres:{encoded_password}@localhost:5433/studentsdetails"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

uploads = Blueprint('uploads', __name__)

db = SQLAlchemy(app)

    
with app.app_context():
    db.create_all()


class attribute_issue_count(db.Model):
    __tablename__ = 'attribute_issue_count'
    issue_count_id = db.Column(db.Integer(), primary_key=True)
    tenant_id=db.Column(db.Integer())
    integration_id = db.Column(db.Integer())
    meta_data_id = db.Column(db.Integer())
    created_month = db.Column(db.Datetime())
    issue_count =db.Column(db.Integer()) 
    issue_details=db.Column(db.JSON())  
    data_set_id=db.Column(db.Integer())
    env_id=db.Column(db.Integer())

    def __init__(self,issue_count_id,tenant_id,integration_id,meta_data_id,created_month,issue_count,issue_details,data_set_id,env_id):
        self.issue_count_id=issue_count_id
        self.tenant_id=tenant_id
        self.integration_id=integration_id
        self.meta_data_id=meta_data_id
        self.created_month=created_month
        self.issue_count=issue_count
        self.issue_details=issue_details
        self.data_set_id=data_set_id
        self.env_id=env_id


att_iss_cou_1=attribute_issue_count(tenant_id=1664,
    integration_id=2566,
    meta_data_id=322384,
    created_month=datetime.datetime(2023, 11, 1, 0, 0, 0),
    issue_count=1,
    issue_details={"44961": 1},
    data_set_id=55396,
    env_id=1485)

db.session.add(att_iss_cou_1)

att_iss_cou_2=attribute_issue_count(tenant_id=1664,
    integration_id=2566,
    meta_data_id=322386,
    created_month=datetime.datetime(2023, 11, 1, 0, 0, 0),
    issue_count=2,
    issue_details={{"44961": 1},{"44982":1}},
    data_set_id=55396,
    env_id=1485)

db.session.add(att_iss_cou_2)

att_iss_cou_3=attribute_issue_count(tenant_id=1664,
    integration_id=2566,
    meta_data_id=322388,
    created_month=datetime.datetime(2023, 11, 1, 0, 0, 0),
    issue_count=1,
    issue_details={"44961": 1},
    data_set_id=55396,
    env_id=1485)

db.session.add(att_iss_cou_3)

att_iss_cou_4=attribute_issue_count(tenant_id=1664,
    integration_id=2566,
    meta_data_id=322382,
    created_month=datetime.datetime(2023, 11, 1, 0, 0, 0),
    issue_count=1,
    issue_details={"44967": 1},
    data_set_id=55396,
    env_id=1485)

db.session.add(att_iss_cou_4)

att_iss_cou_5=attribute_issue_count(tenant_id=1664,
    integration_id=2566,
    meta_data_id=322383,
    created_month=datetime.datetime(2023, 11, 1, 0, 0, 0),
    issue_count=1,
    issue_details={"44961": 1},
    data_set_id=55397,
    env_id=1485)

db.session.add(att_iss_cou_5)

att_iss_cou_6=attribute_issue_count(tenant_id=1664,
    integration_id=2566,
    meta_data_id=322385,
    created_month=datetime.datetime(2023, 11, 1, 0, 0, 0),
    issue_count=2,
    issue_details={{"44961": 1},{"44982":1}},
    data_set_id=55397,
    env_id=1485)

db.session.add(att_iss_cou_6)

att_iss_cou_7=attribute_issue_count(tenant_id=1664,
    integration_id=2566,
    meta_data_id=322387,
    created_month=datetime.datetime(2023, 11, 1, 0, 0, 0),
    issue_count=1,
    issue_details={"44961": 1},
    data_set_id=55397,
    env_id=1485)

db.session.add(att_iss_cou_7)

att_iss_cou_8=attribute_issue_count(tenant_id=1664,
    integration_id=2566,
    meta_data_id=322393,
    created_month=datetime.datetime(2023, 11, 1, 0, 0, 0),
    issue_count=1,
    issue_details={"44961": 1},
    data_set_id=55397,
    env_id=1485)

db.session.add(att_iss_cou_8)

# Commit the session to the database
db.session.commit()

# Records to be inserted:
#   (1664,2566,322384,TIMESTAMP '2023-11-01 00:00:00.000000',1,cast('{"44961": 1}' as json),55396,1485),
#   (1664,2566,322386,TIMESTAMP '2023-11-01 00:00:00.000000',2,cast('{"44961": 1, "44982": 1}' as json),55396,1485),
#   (1664,2566,322388,TIMESTAMP '2023-11-01 00:00:00.000000',1,cast('{"44961": 1}' as json),55396,1485),
#   (1664,2566,322382,TIMESTAMP '2023-11-01 00:00:00.000000',1,cast('{"44967": 1}' as json),55396,1485),
#   (1664,2566,322383,TIMESTAMP '2023-11-01 00:00:00.000000',1,cast('{"44961": 1}' as json),55397,1485),
#   (1664,2566,322385,TIMESTAMP '2023-11-01 00:00:00.000000',2,cast('{"44961": 1, "44982": 1}' as json),55397,1485),
#   (1664,2566,322387,TIMESTAMP '2023-11-01 00:00:00.000000',1,cast('{"44961": 1}' as json),55397,1485),
#   (1664,2566,322393,TIMESTAMP '2023-11-01 00:00:00.000000',1,cast('{"44967": 1}' as json),55397,1485);

 

    
class dataset_issue_count(db.Model):
    __tablename__ = 'dataset_issue_count'
    issue_count_id = db.Column(db.Integer(), primary_key=True)
    tenant_id=db.Column(db.Integer())
    integration_id = db.Column(db.Integer())
    data_set_id = db.Column(db.Integer())
    created_month = db.Column(db.Datetime())
    issue_count =db.Column(db.Integer()) 
    issue_details=db.Column(db.JSON())  
    env_id=db.Column(db.Integer())
    
    def __init__(self,issue_count_id,tenant_id,integration_id,data_set_id,created_month,issue_count,issue_details,env_id):
        self.issue_count_id=issue_count_id
        self.tenant_id=tenant_id
        self.integration_id=integration_id
        self.data_set_id=data_set_id
        self.created_month=created_month
        self.issue_count=issue_count
        self.issue_details=issue_details
        self.env_id=env_id
        
# Records to be inserted:
#   (1664,2566,55396,TIMESTAMP '2023-11-01 00:00:00.000000',3,cast('{"44961": 1, "44967": 1, "44982": 1}' as json),1485),
#   (1664,2566,55397,TIMESTAMP '2023-11-01 00:00:00.000000',3,cast('{"44961": 1, "44967": 1, "44982": 1}' as json),1485);
