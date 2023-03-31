import pandas as pd
from google.cloud import storage
import io
import pytz


def add_column_and_transfer_file(event, context):

    file_name = event['name']
    client = storage.Client()
    bucket = client.get_bucket('source_raw_bucket')
    blob = bucket.blob(file_name)
    content = blob.download_as_string()

    df = pd.read_csv(io.BytesIO(content))
    df['date']= pd.Timestamp.today().strftime('%Y-%m-%d')
    df['date']= pd.to_datetime(df['date'])
    df['date']=df['date'].dt.tz_localize('EST')
    df['date'] = df['date'].dt.date

    mean_value= df['age'].mean()
    df['age'].fillna(value=mean_value, inplace=True)
    df['age']=df['age'].astype('int')

    df['region']=df['region'].fillna(df.region.mode()[0])

    new_file_name = "Cleansed_"+file_name
    destination_bucket=client.get_bucket("destination_curated_bucket")
    new_blob = destination_bucket.blob(new_file_name)
    new_blob.upload_from_string(df.to_csv(index=False), 'text/csv')

