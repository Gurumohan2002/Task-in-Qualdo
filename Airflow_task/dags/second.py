from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from funct import adding_two_values,subtracting_two_values,multiplying_two_values

#default arguments for DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 4),
    'depends_on_past': False,
    'retries': 1,
}

#Creating the DAG
dag = DAG(
    dag_id='Mathematical_Operations',
    default_args=default_args,
    description='DAG for mathematical operations',
    schedule_interval=timedelta(hours=1),
)

# Values for the mathematical operations 
a, b = 1000, 1001
c, d = 200, 34
e, f = 20, 20

#Adding two values a and b
task_add = PythonOperator(
    task_id='adding_two_values',
    python_callable=adding_two_values,
    op_args=[a, b],
    dag=dag,
)

#Subtracting two values c and d
task_subtract = PythonOperator(
    task_id='subtracting_two_values',
    python_callable=subtracting_two_values,
    op_args=[c, d],
    dag=dag,
)

#Multiplying two values e and f
task_multiply = PythonOperator(
    task_id='multiplying_two_values',
    python_callable=multiplying_two_values,
    op_args=[e, f],
    dag=dag,
)

# DAG flow For Sequential execution 
task_add >> task_subtract >> task_multiply

# DAG flow For Parallel execution
[task_add,task_subtract, task_multiply]