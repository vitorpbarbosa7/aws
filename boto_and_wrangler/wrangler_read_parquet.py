import awswrangler as wr
import pandas as pd
from IPython.display import display

df = wr.s3.read_parquet('s3://vpb-spark-bucket/iris.parquet')
display(df.head())

