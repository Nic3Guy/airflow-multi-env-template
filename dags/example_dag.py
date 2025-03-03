from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime

with DAG('example_dag', schedule_interval='@daily', start_date=datetime(2025, 3, 1), catchup=False) as dag:
    start = DummyOperator(task_id='start')
    end = DummyOperator(task_id='end')
    start >> end
