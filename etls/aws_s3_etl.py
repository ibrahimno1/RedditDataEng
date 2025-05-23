from utils.constants import AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_BUCKET_NAME
import s3fs

def connect_to_s3():
    try:
        s3 = s3fs.S3FileSystem(anon=False, 
                               key=AWS_ACCESS_KEY,
                              secret=AWS_SECRET_KEY)
        return s3
    except Exception as e:
        print(f"Error connecting to S3: {e}")
        return None
def create_bucket_if_not_exists(s3: s3fs.S3FileSystem, AWS_BUCKET_NAME):
    try:
        if not s3.exists(f's3://{AWS_BUCKET_NAME}'):
            s3.mkdir(f's3://{AWS_BUCKET_NAME}')
            print(f"Bucket {AWS_BUCKET_NAME} created.")
        else:
            print(f"Bucket {AWS_BUCKET_NAME} already exists.")
    except Exception as e:
        print(f"Error creating bucket: {e}")
def upload_file_to_s3(s3: s3fs.S3FileSystem, file_name: str, bucket: str, s3_file_name: str):
    try:
        s3.put(file_name, bucket + '/raw/' + s3_file_name)
        print(f"File {file_name} uploaded to {bucket}/{s3_file_name}.")
    except Exception as e:
        print(f"Error uploading file: {e}")