import pandas as pd
from google.cloud import storage
import io
import numpy as np

def csv_to_json(event, context):

    file_name = event['name']
    client = storage.Client()
    bucket = client.get_bucket('source_cleansed_bucket')
    blob = bucket.blob(file_name)
    content = blob.download_as_string()

    df = pd.read_csv(io.BytesIO(content))

    condition=[(df['age'] <= 14),
    (df['age'] >= 14) & (df['age'] <= 24),
    (df['age'] >= 25) & (df['age'] < 60),
    (df['age'] >=60)]

    values = ["child", "youth", "adult", "senior"]
    
    df['age_category'] = np.select(condition, values)

    new_file_name = "Curated_"+ file_name.split('.')[0]
    destination_bucket=client.get_bucket("destination_curated_bucket")
    new_blob = destination_bucket.blob(new_file_name)
    new_blob.upload_from_string(df.to_json(orient = 'records'), 'application/json')
