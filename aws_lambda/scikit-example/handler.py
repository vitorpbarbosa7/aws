import json
import joblib

# load before to use warm start after ?
# load before as best practice

model_name = 'models/all_data_model.pkl'
model = joblib.load(model_name)

def predict(event, context):
    body = {
        "message": "OK"        
    }

    params = event['queryStringParameters']

    medInc = float(params['medInc']) / 100000
    houseAge = float(params['houseAge'])
    aveRooms = float(params['aveRooms'])
    aveBedrms = float(params['aveBedrms'])
    population = float(params['population'])
    aveOccup = float(params['aveOccup'])
    latitude = float(params['latitude'])
    longitude = float(params['longitude'])

    inputVector = [medInc, houseAge, aveRooms, aveBedrms, population, aveOccup, latitude, longitude]
    data = [inputVector]

    predictedPrice = model.predict(data)[0] * 100000
    predictedPrice = round(predictedPrice, 2)
    body['predictedPrie'] = predictedPrice

    response = {
        "statusCode": 200,
        "body": json.dumps(body),
        "headers": {
            # cross origin resource sharing
            "Access-Control-Allow-Origin": "*"
        }
    }

    return response
