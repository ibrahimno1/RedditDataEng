import configparser
import os

parser = configparser.ConfigParser()
CONFIG_PATH = os.path.join(os.path.dirname(__file__), '../config/config.conf')
parser.read(os.path.abspath(CONFIG_PATH))

SECRET = parser.get('api_keys', 'reddit_secret_key')
CLIENT_ID = parser.get('api_keys', 'reddit_client_id')

DATABASE_HOST = parser.get('database', 'database_host')
DATABASE_PORT = parser.get('database', 'database_port')
DATABASE_USER = parser.get('database', 'database_username')
DATABASE_PASSWORD = parser.get('database', 'database_password')
DATABASE_NAME = parser.get('database', 'database_name')

AWS_ACCESS_KEY = parser.get('aws', 'AWS_ACCESS_KEY')
AWS_SECRET_KEY = parser.get('aws', 'AWS_SECRET_KEY')
AWS_REGION = parser.get('aws', 'AWS_REGION')
AWS_BUCKET_NAME = parser.get('aws', 'AWS_BUCKET_NAME')


INPUT_PATH= parser.get('file_paths', 'input_path')
OUTPUT_PATH = parser.get('file_paths', 'output_path')

POST_FIELDS = (
    'id',
    'title',
    'score',
    'num_comments',
    'author',
    'created_utc',
    'url',
    'over_18',
    'edited',
    'spoiler',
    'stickied',
)
