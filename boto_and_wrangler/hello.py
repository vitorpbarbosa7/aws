import boto3

session = boto3.Session(profile_name='spark_user')
client = session.client('ec2')

print(type(session))
print(type(client))

print(session.profile_name)

resp = client.run_instances(ImageId='ami-09dc6ca003392c5c3',
                        InstanceType='t2.micro',
                        MinCount=1,
                        MaxCount=1)

for instance in resp['Instances']:
    print(instance['InstanceId'])