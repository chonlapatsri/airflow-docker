
from airflow.decorators import dag, task
from datetime import datetime, timedelta


default_args = {
    'owner': 'admin',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

@dag(dag_id='dag_with_taskflow_api_v4', 
     default_args=default_args, 
     start_date=datetime(2021, 10, 26), 
     schedule_interval='@daily')
def hello_world_etl():

    @task(multiple_outputs=True)
    def get_name():
        return {
            'first_name': 'Chonlapat',
            'last_name': 'Srisuwan'
        }

    @task()
    def get_age():
        return 32

    @task()
    def greet(first_name, last_name, age):
        print(f"Hello World! My name is {first_name} {last_name} "
              f"and I am {age} years old!")
    
    name_dict = get_name()
    first_name = name_dict['first_name']
    last_name = name_dict['last_name']
    age = get_age()
    greet(first_name=first_name, 
          last_name=last_name,
          age=age)

greet_dag = hello_world_etl()