from etls.aws_s3_etl import (
    connect_to_s3,
    create_bucket_if_not_exists,
    upload_file_to_s3
)
from utils.constants import AWS_BUCKET_NAME

def upload_s3_pipeline(**kwargs):
    ti = kwargs['ti']
    file_name = ti.xcom_pull(task_ids='extract_reddit', key='return_value')
    
    if not file_name:
        raise ValueError("❌ No file name returned from extract_reddit")

    s3 = connect_to_s3()
    create_bucket_if_not_exists(s3, AWS_BUCKET_NAME)
    upload_file_to_s3(s3, file_name, AWS_BUCKET_NAME, file_name.split('/')[-1])

