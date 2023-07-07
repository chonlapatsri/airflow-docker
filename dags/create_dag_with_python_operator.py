from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime, timedelta




default_args={
        'owner': 'admin',
        'retries': 5,
        'retry_delay': timedelta(minutes=5)
}

def greet():
    print("Hello World!")

def present_me(name, age, ti):
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
    print(f"my name is {name} {first_name} {last_name}, and I am {age} years old")

def get_name(ti):
    ti.xcom_push(key='first_name', value='Chonlapat')
    ti.xcom_push(key='last_name', value='Srisuwan')

with DAG(
    dag_id='our_dag_with_python_operator_v4',
    default_args=default_args,
    description='This is my dag with python operator',
    start_date=datetime(2021, 10, 6, 2),
    schedule_interval='@daily'        
) as dag:
    
    task1=PythonOperator(
        task_id='greet_1',
        python_callable=greet
    )

    task2=PythonOperator(
        task_id='greet_2',
        python_callable=present_me,
        op_kwargs={'name': default_args['owner'], 'age': 32}
    )

    task3=PythonOperator(
        task_id='get_name',
        python_callable=get_name,
        op_kwargs={'name': default_args['owner'], 'age': 32}
    )


    task1>>task3
    task3>>task2