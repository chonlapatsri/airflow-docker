import csv
import logging
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.providers.postgres.hooks.postgres import PostgresHook
from tempfile import NamedTemporaryFile

default_args = {
    'owner': 'admin',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def postgres_to_s3(prev_start_date_success, ds_nodash):
    # query data from postgress db and save into a text file
    hook = PostgresHook(postgres_conn_id="postgres_localhost")
    conn = hook.get_conn()
    cursor = conn.cursor()
    cursor.execute("select * from orders where date >= %s and date < %s",
                   (ds_nodash, prev_start_date_success))
    
    with NamedTemporaryFile(mode='w', suffix=f"{ds_nodash}") as f:
    # with open(f"dags/get_orders_{ds_nodash}.txt", "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([i[0] for i in cursor.description])
        csv_writer.writerows(cursor)
        f.flush()
        cursor.close()
        conn.close()
        logging.info("Saved orders data in text file: %s", f"dags/get_orders_{ds_nodash}.txt")
    
        # upload text file to s3
        s3_hook = S3Hook(aws_conn_id="minio_conn")
        s3_hook.load_file(
            # filename=f"dags/get_orders_{ds_nodash}.txt",
            filename=f.name, 
            key=f"oders/{ds_nodash}.txt",
            bucket_name="airflow",
            replace=True
        )
        logging.info("Order file %s has been pushed to S3!", f.name)

with DAG(
    dag_id='dag_with_postgres_hook_v6',
    default_args=default_args,
    start_date=datetime(2022, 2, 12),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id = "postgres_to_s3",
        python_callable=postgres_to_s3
    )