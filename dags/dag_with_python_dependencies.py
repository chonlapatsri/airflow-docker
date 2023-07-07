from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'admin',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def get_sklearn():
    import sklearn
    print(f"scikit-learn with version: {sklearn.__version__}")

def get_mlp():
    import matplotlib
    print(f"matplotlib with version: {matplotlib.__version__}")

with DAG(
    dag_id='dag_with_python_dependencies_v5',
    default_args=default_args,
    start_date=datetime(2021, 12, 19),
    schedule_interval='@daily'
) as dag:
    
    get_sklearn = PythonOperator(
        task_id='get_sklearn',
        python_callable=get_sklearn
    )

    get_mlp = PythonOperator(
    task_id='get_mlp',
    python_callable=get_mlp
    )



    get_sklearn >> get_mlp