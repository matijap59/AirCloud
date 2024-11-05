import requests
import json

headers = {
        "X-API-Key": "e02e0dcd89ae677eb13ae403e1953479687309431996f73679a22ec98642156f"
}

def lambda_handler(event, context):
    # URL za sve gradove
    url = "https://api.openaq.org/v2/cities"
    response = requests.get(url, headers=headers)
    cities_data = response.json()

    # Prolazak kroz gradove i ispis naziva
    for city in cities_data['results']:
        print(f"City: {city['city']}, Locations: {city['locations']}")

    return {
        'statusCode': 200,
        'body': 'Hello from getDataOpenAQ'
    }