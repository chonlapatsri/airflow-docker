from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args={
        'owner': 'admin',
        'retries': 5,
        'retry_delay': timedelta(minutes=2)

}

with DAG(
    dag_id='my_first_dag_v5',
    default_args=default_args,
    description='This is my first dag on airflow',
    start_date=datetime(2021, 7, 29, 2),
    schedule_interval='@daily'        
) as dag:
        task1 = BashOperator(
                task_id='first_task',
                bash_command="echo hello world, this is my first task!"
        )

        task2 = BashOperator(
                task_id='second_task',
                bash_command="echo this is task 2, running after task 1"
        )

        task3 = BashOperator(
                task_id='third_task',
                bash_command="echo Sorry task 3, running after task 1 at the same time as task 2"
        )

        # This is where we set the schedule
        # task1.set_downstream(task2)
        # task1.set_downstream(task3)
        # task1 >> task2
        # task1 >> task3
        task1 >> [task2, task3]

        
