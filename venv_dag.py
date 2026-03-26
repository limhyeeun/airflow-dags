from airflow import DAG
from airflow.operators.python import PythonVirtualenvOperator
from datetime import datetime


def use_pandas():
    import pandas as pd

    df = pd.DataFrame({"name": ["Alice", "Bob"], "score": [90, 85]})
    print(df.to_string())
    return df.to_dict()


def use_requests():
    import requests

    resp = requests.get("https://httpbin.org/get")
    print(resp.json())
    return resp.status_code


with DAG("venv_example", start_date=datetime(2024, 1, 1), schedule=None) as dag:

    pandas_task = PythonVirtualenvOperator(
        task_id="pandas_task",
        python_callable=use_pandas,
        requirements=["pandas==2.2.3"],
    )

    requests_task = PythonVirtualenvOperator(
        task_id="requests_task",
        python_callable=use_requests,
        requirements=["requests==2.32.3"],
    )

    pandas_task >> requests_task
