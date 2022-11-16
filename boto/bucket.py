import boto3
from pprint import pprint
import json
import pandas as pd
from IPython.display import display

def write_json(object, path_file:str):
    json_object = json.dumps(object, indent=4, default=str)
    with open(path_file, 'w') as file:
        file.write(json_object)


BUCKET = 'vpb-spark-bucket'
FILE = 'iris.csv'

s3_client = boto3.client('s3')

results = s3_client.list_objects(Bucket = BUCKET)

write_json(results, 'parsed_response.json')

contents = results['Contents']

write_json(contents, 'contents.json')

data_key = 'iris.csv'

data_body = s3_client.get_object(Bucket = BUCKET, Key = data_key)
# print(data_body)
df = pd.read_csv(data_body['Body'])
display(df.head())

# df = pd.read_csv(data_read.decode('utf-8'))
# print(type(df))
# print(df)




# prefix_one_object = s3_client.list_objects(Bucket = BUCKET, Prefix = FILE)

# for object in prefix_one_object.get('Contents'):
#     print(type(object))
#     print(object)

#     key = object.get('Key')
#     print(type(key))
#     print(key)
#     data = s3_client.get_object(Bucket = BUCKET, Key = key)
#     print(data)
#     print(type(data))
    
    # contents = data['Body'].read()
    # contents.decode('utf-8')



# for my_bucket_object in my_bucket.objects.all():
#     print(my_bucket_object)