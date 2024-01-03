from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP, JSON
from sqlalchemy.ext.declarative import declarative_base
from urllib.parse import quote
from sqlalchemy.orm import sessionmaker
import psycopg2

Base = declarative_base()

password = "Guru@2607"
encoded_password = quote(password)

class attribute_issue_count(Base):
    __tablename__ = 'attribute_issue_count'
    issue_count_id = Column(Integer, primary_key=True)
    tenant_id = Column(Integer, nullable=False)
    integration_id = Column(Integer, nullable=False)
    meta_data_id = Column(Integer, nullable=False)
    created_month = Column(TIMESTAMP, nullable=False)
    issue_count = Column(Integer, nullable=False)
    issue_details = Column(JSON, nullable=False)
    data_set_id = Column(Integer, nullable=False)
    env_id = Column(Integer, nullable=False)

class dataset_issue_count(Base):
    __tablename__ = 'dataset_issue_count'
    issue_count_id = Column(Integer, primary_key=True)
    tenant_id = Column(Integer, nullable=False)
    integration_id = Column(Integer, nullable=False)
    data_set_id = Column(Integer, nullable=False)
    created_month = Column(TIMESTAMP, nullable=False)
    issue_count = Column(Integer, nullable=False)
    issue_details = Column(JSON, nullable=False)
    env_id = Column(Integer, nullable=False)

class datasource_issue_count(Base):
    __tablename__ = 'datasource_issue_count'
    issue_count_id = Column(Integer, primary_key=True)
    tenant_id = Column(Integer, nullable=False)
    env_id = Column(Integer, nullable=False)
    integration_id = Column(Integer, nullable=False)
    created_month = Column(TIMESTAMP, nullable=False)
    issue_count_dataset_level = Column(Integer, nullable=False)
    issue_details_dataset_level = Column(JSON, nullable=False)
    issue_count_attribute_level = Column(Integer, nullable=False)
    issue_details_attribute_level = Column(JSON,nullable=False)
      
DATABASE_URL = f"postgresql+psycopg2://postgres:{encoded_password}@localhost:5433/studentsdetails"
engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

records_attribute = [
    (1664,2566,322384,'2023-11-01 00:00:00.000000',1,'{"44961": 1}',55396,1485),
    (1664,2566,322386,'2023-11-01 00:00:00.000000',2,'{"44961": 1, "44982": 1}' ,55396,1485),
    (1664,2566,322388,'2023-11-01 00:00:00.000000',1,'{"44961": 1}',55396,1485),
    (1664,2566,322382,'2023-11-01 00:00:00.000000',1,'{"44967": 1}',55396,1485),
    (1664,2566,322383,'2023-11-01 00:00:00.000000',1,'{"44961": 1}',55397,1485),
    (1664,2566,322385,'2023-11-01 00:00:00.000000',2,'{"44961": 1, "44982": 1}',55397,1485),
    (1664,2566,322387,'2023-11-01 00:00:00.000000',1,'{"44961": 1}',55397,1485),
    (1664,2566,322393,'2023-11-01 00:00:00.000000',1,'{"44967": 1}',55397,1485)
]

records_dataset=[
    (1664,2566,55396,'2023-11-01 00:00:00.000000',3,'{"44961": 1, "44967": 1, "44982": 1}' ,1485),
    (1664,2566,55397,'2023-11-01 00:00:00.000000',3,'{"44961": 1, "44967": 1, "44982": 1}',1485)
    ]

for record in records_attribute:
    issue = attribute_issue_count(
        tenant_id=record[0],
        integration_id=record[1],
        meta_data_id=record[2],
        created_month=record[3],
        issue_count=record[4],
        issue_details=record[5],
        data_set_id=record[6],
        env_id=record[7]
    )
    session.add(issue)

session.commit()
session.close()

for record in records_dataset:
    issue = dataset_issue_count(
        tenant_id=record[0],
        integration_id=record[1],
        data_set_id=record[2],
        created_month=record[3],
        issue_count=record[4],
        issue_details=record[5],
        env_id=record[6]
    )
    session.add(issue)
    
session.commit()
session.close()

