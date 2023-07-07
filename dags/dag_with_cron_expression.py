from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'admin',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='dag_with_cron_expression_v6',
    default_args=default_args,
    start_date=datetime(2021, 11, 1),
    # go to crontab.guru to find cron expression
    schedule_interval='0 3 * * Tue,Wed'
) as dag:
    
    task1 = BashOperator(
        task_id='task_1',
        bash_command='echo This is a simple bash command!'
    )