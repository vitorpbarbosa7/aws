import boto3
import pandas as pd
from IPython.display import display
from io import BytesIO

BUCKET = 'vpb-spark-bucket'
FILE = 'iris.csv'

s3 = boto3.resource('s3')

filename = 'iris.parquet'

buffer = BytesIO()
object = s3.Object(BUCKET, filename)
object.download_fileobj(buffer)
print(type(buffer))
print(dir(buffer))

df = pd.read_parquet(buffer)
display(df.head())