from airflow import DAG
from datetime import datetime
import os
import sys
from airflow.operators.python import PythonOperator
sys.path.insert(0, '/opt/airflow')
from pipelines.aws_s3_pipeline import upload_s3_pipeline
from pipelines.reddit_pipeline import reddit_pipeline



sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

default_args = {
    'owner': 'Ibrahim',
    'start_date': datetime(2022, 5, 13),
}

file_postfix = datetime.now().strftime("%Y-%m-%d")

with DAG(
    dag_id='etl_reddit_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['reddit', 'pipeline', 'etl'],
) as dag:

    extract = PythonOperator(
        task_id='extract_reddit',
        python_callable=reddit_pipeline,
        op_kwargs={
            'filename': f'reddit_{file_postfix}',
            'subreddit': 'dataengineering',
            'time_filter': 'day',
            'limit': 100
        }
    )
    upload_s3 = PythonOperator(
        task_id='upload_s3',
        python_callable=upload_s3_pipeline,
        provide_context=True)

    extract >> upload_s3