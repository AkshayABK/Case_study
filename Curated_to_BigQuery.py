import pandas as pd
from pandas.io import gbq
from google.cloud import bigquery


def hello_gcs(event, context):
  file_name = event['name']
  table_name = file_name.split('.')[0]
  df_data = pd.read_json('gs://' + event['bucket'] + '/' + file_name)
  df_data.to_gbq('file_name.Dataset' + table_name, 
                  project_id='file_name', 
                  if_exists='append',
                  location='us')