from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from airflow.models import Variable
from funct import get_user_input,print_word_lengths

#default arguments for DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 4),
    'depends_on_past': False,
    'retries': 1,
}

#Creating the DAG
dag = DAG(
    dag_id='first_task',
    default_args=default_args,
    description='DAG for finding length of given variables by user',
    schedule_interval=timedelta(minutes=1), 
    catchup=False,
)

# creating an airflow variable with user given input.
input_list = ["DAGID", "variablename", "presentations"]

task_get_user_input = PythonOperator(
    task_id='Getting_user_input',
    python_callable=get_user_input,
    op_args=[input_list],
    dag=dag,
)

# Printing the length of the words in the user input
task_print_word_lengths = PythonOperator(
    task_id='Print_word_lengths',
    python_callable=print_word_lengths,
    op_args=[input_list],
    dag=dag,
)

# DAG flow
task_get_user_input >> task_print_word_lengths
