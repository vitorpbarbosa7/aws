import boto3

s3 = boto3.resource('s3')

BUCKET = 'vpb-spark-bucket'
PREFIX = 'iris'

my_bucket = s3.Bucket(BUCKET)

s3_client = boto3.client('s3')

result = s3_client.list_objects(Bucket = BUCKET, Prefix = PREFIX)

print(result)

for object in result.get('Contents'):
    data = s3_client.get_object(Bucket = BUCKET, Key = object.get('Key'))
    contents = data['Body'].read()
    print(contents.decode('utf-8'))

# for my_bucket_object in my_bucket.objects.all():
#     print(my_bucket_object)