import os
import sys
import pandas as pd
from etls.reddit_etl import transform_data, load_data_to_csv

# Add both the root and 'etl' directories to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.constants import CLIENT_ID, OUTPUT_PATH, SECRET
from etls.reddit_etl import connect_to_reddit, extract_posts

def reddit_pipeline(filename: str, subreddit: str, time_filter='day', limit=None):
    instance = connect_to_reddit(CLIENT_ID, SECRET, 'Green-Tap2784')
    posts = extract_posts(instance, subreddit, time_filter, limit)
    
    post_df = pd.DataFrame(posts)
    post_df = transform_data(post_df)

    output_path = f'{OUTPUT_PATH}/{filename}.csv'
    load_data_to_csv(post_df, output_path)

    return output_path 




