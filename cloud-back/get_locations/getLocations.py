import requests


def lambda_handler(event, context):
    unique_locations = set()
    page = 1
    limit = 100
    headers = {
        "X-API-Key": "e02e0dcd89ae677eb13ae403e1953479687309431996f73679a22ec98642156f"
    }

    while True:
        # Ispis može biti zamenjen logovanjem u Lambda okruženju
        print(f"Fetching page {page}...")

        # Poziv ka API-ju
        response = requests.get(f'https://api.openaq.org/v2/locations?limit={limit}&page={page}', headers=headers)

        # Parsiranje odgovora u JSON format
        data = response.json()

        # Provera da li postoje rezultati
        if 'results' not in data or not data['results']:
            break

        # Dodavanje jedinstvenih lokacija
        for location in data['results']:
            loc_id = location.get('id')
            loc_name = location.get('name')
            if loc_id is not None and loc_name is not None:
                unique_locations.add((loc_id, loc_name))

        page += 1

    return {
        "statusCode": 200,
        "body": list(unique_locations)
    }