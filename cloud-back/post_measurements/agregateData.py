import boto3
from datetime import datetime, timedelta
import requests
from collections import defaultdict
import pandas as pd

# Kreiraj boto3 resource za DynamoDB
dynamodb = boto3.resource('dynamodb')
table_name = 'aggregatedMeasurements'  # Zameni imenom tvoje tabele
table = dynamodb.Table(table_name)


def fetch_and_store_measurements(event, context):
    location_id = event.get('location_id', None)
    days_back = event.get('days_back', 365)

    url = "https://api.openaq.org/v2/measurements"

    date_limit_start = (datetime.utcnow() - timedelta(days=days_back)).isoformat() + "Z"
    date_limit_end = datetime.utcnow().isoformat() + "Z"

    headers = {
        "X-API-Key": "e02e0dcd89ae677eb13ae403e1953479687309431996f73679a22ec98642156f"
    }

    all_parameters = []
    offset = 0
    limit = 100
    items_stored = 0

    while True:
        response = requests.get(
            f"{url}?location_id={location_id}&date_gte={date_limit_start}&date_lte={date_limit_end}&limit={limit}&offset={offset}",
            headers=headers
        )

        if response.status_code == 200:
            parameters_data = response.json()
            parameters = parameters_data.get('results', [])
            all_parameters.extend(parameters)

            if len(parameters) < limit:
                break

            offset += limit
        else:
            print(f"Error fetching parameters: {response.status_code}")
            return {"status": "error", "message": f"Failed to fetch data, status code: {response.status_code}"}

    # Sort parameters
    all_parameters.sort(key=lambda x: x['date']['utc'], reverse=False)

    aggregated_data = defaultdict(list)
    for param in all_parameters:
        date_key = param['date']['utc'][:10]  # Uzimamo samo datum (YYYY-MM-DD)
        aggregated_data[date_key].append(param['value'])

    avg_values = {date: sum(values) / len(values) for date, values in aggregated_data.items()}

    df = pd.DataFrame(list(avg_values.items()), columns=['Date', 'Avg Value'])

    for date, avg_value in avg_values.items():
        print(f"Date: {date}, Avg Value: {avg_value:.2f}")

        item = {
            'location_id': location_id,
            'date': date,
            'avg_value': round(avg_value, 2)
        }

        try:
            # Upis u DynamoDB
            table.put_item(Item=item)
            items_stored += 1
        except Exception as e:
            print(f"Failed to store item for date {date}: {str(e)}")
            return {"status": "error", "message": f"Failed to store data for {date}", "error": str(e)}

    # Kraj funkcije, vraćamo status
    return {
        "status": "success",
        "message": f"Stored {items_stored} items in DynamoDB",
        "stored_items_count": items_stored,
        "dataframe": df
    }
