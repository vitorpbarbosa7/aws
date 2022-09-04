# The Lambda Function 

import json


def hello(event, context):
    '''
    args:
    event: different informations about the event, that trigger the lambda execution
    context: function invocation and runtime environment
    ----------------------------------------------------------


    '''
    body = {
        "message": "Go Serverless v1.0! Your Lambda function executed successfully!",
        "input": event
    }

    print(body['message'])

    # api gateway service will format this to a proper http response message 
    # status and body from http message
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
