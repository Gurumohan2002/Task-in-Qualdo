from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime, timedelta

#default arguments for DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 4),
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

#Creating the DAG which runs every 2 min
dag = DAG(
    dag_id='Postgres',
    default_args=default_args,
    description='DAG to insert rows into tables every 2 minutes',
    schedule_interval='*/2 * * * *',  
    catchup=False,
)

# SQL query to insert rows into the "Orders" table

insert_into_orders = """
INSERT INTO orders (customer_id, order_date)
VALUES (2, NOW()),
       (4, NOW());
"""

# SQL query to insert rows into the "Product_returns" table
insert_into_product_returns = """
INSERT INTO product_returns (customer_id, return_date)
VALUES (3, NOW()),
       (4, NOW());
"""

# PostgresOperator for inserting rows to orders
task_insert_into_orders = PostgresOperator(
    task_id='insert_orders_task',
    postgres_conn_id='PostgresConnection',
    sql=insert_into_orders,
    dag=dag,
)

# PostgresOperator for inserting rows to product_returns
task_insert_into_product_returns = PostgresOperator(
    task_id='insert_returns_task',
    postgres_conn_id='PostgresConnection',
    sql=insert_into_product_returns,
    dag=dag,
)

# DAG flow
task_insert_into_orders >> task_insert_into_product_returns

