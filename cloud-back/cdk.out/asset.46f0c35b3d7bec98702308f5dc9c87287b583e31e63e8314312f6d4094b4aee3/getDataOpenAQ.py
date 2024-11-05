import requests


def lambda_handler(event, context):
    # URL za sve gradove
    url = "https://api.openaq.org/v2/cities"
    response = requests.get(url)
    cities_data = response.json()

    # Prolazak kroz gradove i ispis naziva
    for city in cities_data['results']:
        print(f"City: {city['city']}, Locations: {city['locations']}")
    return {
        'statusCode': 200,
        'body': cities_data
    }