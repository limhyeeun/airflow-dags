from airflow import DAG
from datetime import datetime

with DAG("simple_test", start_date=datetime(2024,1,1), schedule=None) as dag:
    pass