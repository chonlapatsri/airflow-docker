# airflow-docker
Codes can be found in the dags folder. They are Python codes to orchestrate airflow to automatically perform simple tasks following defined work processes.

create_dag_with_python_operator.py

dag_with_catchup_and_backfill.py - 

dag_with_cron_expression.py - an airflow that runs some tasks on schedule set by cron expression

dag_with_minio_s3.py - an airflow that connects with min.io (cloud storage) via AMS S3 connection

dag_with_postgres_hook.py - an airflow that downloads and uploads data from/to postgres

dag_with_postgres_operator.py - an airflow that downloads dataset from postgres with SQL

dag_with_python_dependencies.py - an airflow with requirement of dependencies in the Docker image

dag_with_taskflow_api.py - an airflow with simple task flows

my_first_dag.py - a simple airflow demonstration without any taskflow
