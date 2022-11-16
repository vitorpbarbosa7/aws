import pandas as pd
import boto3
from io import BytesIO, StringIO

def dataframe_to_s3(input_datafame, bucket_name, filepath, format, s3_client):
    '''
    https://stackoverflow.com/questions/53416226/how-to-write-parquet-file-from-pandas-dataframe-in-s3-in-python
    the below function gets parquet output in a buffer and then write buffer.values() to S3 without any need to save parquet locally
    Also, since you're creating an s3 client you can create credentials using aws s3 keys that can be either stored locally, in an airflow connection or aws secrets manager
    '''

    if format == 'parquet':
        out_buffer = BytesIO()
        input_datafame.to_parquet(out_buffer, index=False)

    elif format == 'csv':
        out_buffer = StringIO()
        input_datafame.to_parquet(out_buffer, index=False)

    s3_client.put_object(Bucket=bucket_name, Key=filepath, Body=out_buffer.getvalue())


if __name__ == '__main__':

    BUCKET = 'vpb-spark-bucket'

    s3_client = boto3.client('s3')

    df = pd.read_parquet('iris.parquet')

    dataframe_to_s3(df, BUCKET, 'iris.parquet', 'parquet', s3_client)