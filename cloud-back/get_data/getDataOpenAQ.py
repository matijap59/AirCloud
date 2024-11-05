import requests
import json


def lambda_handler(event, context):
    cities_info = []
    page = 1
    limit = 100
    headers = {
        "X-API-Key": "e02e0dcd89ae677eb13ae403e1953479687309431996f73679a22ec98642156f"
    }

    while True:
        print(f"Fetching page {page}...")
        response = requests.get(f'https://api.openaq.org/v2/cities?limit={limit}&page={page}', headers=headers)
        data = response.json()

        if 'results' not in data or not data['results']:
            break

        # Iteracija kroz rezultate
        for city in data['results']:
            city_name = city.get('city')
            locations = city.get('locations')
            if city_name is not None and locations is not None:
                cities_info.append(f"City: {city_name}, Locations: {locations}")

        page += 1

    return {
        "statusCode": 200,
        "body": cities_info
    }