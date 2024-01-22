from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime, timedelta

#default arguments for DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 5),
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

#Creating the DAG which runs every 4 min
dag = DAG(
    dag_id='Purchase_details_insert',
    default_args=default_args,
    description='DAG to insert rows into tables every 4 minutes',
    schedule_interval='*/4 * * * *',  
    catchup=False,
)

# SQL query to insert total_orders and total_returns in "purchase_details" table
task_for_purchase_details_insert = """
Insert into purchase_details ( customer_id, total_orders, total_returns, created_time)
    Select o.customer_id,o.total_orders,pr.total_returns,NOW() as created_time
    from (SELECT customer_id,count(distinct order_id) as total_orders from orders group by customer_id) o 
    left join 
    (Select customer_id,count(distinct return_id) as total_returns from product_returns group by customer_id) pr 
    on o.customer_id = pr.customer_id; 
"""

# PostgresOperator for inserting rows to purchase_details
task_for_purchase_details= PostgresOperator(
    task_id='Purchase_details_update',
    postgres_conn_id='PostgresConnection',
    sql=task_for_purchase_details_insert,
    dag=dag,
)

# DAG flow
task_for_purchase_details

