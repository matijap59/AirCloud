import json
import boto3
import pandas as pd
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta

dynamodb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    # Čitanje podataka iz DynamoDB tabele 'aggregatedMeasurements'
    table = dynamodb.Table('aggregatedMeasurements')

    # Dobijanje svih stavki iz tabele
    response = table.scan()
    data = response['Items']

    # Konvertovanje podataka u DataFrame
    df = pd.DataFrame(data)

    # Pretvorite 'Date' u datetime tip
    df['Date'] = pd.to_datetime(df['Date'])
    df['Avg Value'] = df['Avg Value'].astype(float)  # Uverite se da su vrednosti u ispravnom formatu

    # Definisanje ulaznih i izlaznih podataka za regresiju
    df['Date_num'] = pd.to_datetime(df['Date']).map(pd.Timestamp.toordinal)
    X = df[['Date_num']]  # Ulazi (numerički datumi)
    y = df['Avg Value']  # Izlazi (prosečne vrednosti)

    # Kreiranje i treniranje linearnog regresionog modela
    model = LinearRegression()
    model.fit(X, y)

    # Kreiranje predikcija za narednih 7 dana
    future_dates = pd.date_range(start=datetime.now(), periods=7)  # Trenutni datum + 7 dana
    future_dates_num = future_dates.map(pd.Timestamp.toordinal).values.reshape(-1, 1)

    # Pravljenje predikcija
    predictions = model.predict(future_dates_num)

    # Priprema podataka za unos u 'prediction-table-date'
    prediction_table = dynamodb.Table('prediction-table-date')
    for date, prediction in zip(future_dates, predictions):
        prediction_item = {
            'Date': date.strftime('%Y-%m-%d'),  # Pretvorite datum u string
            'Predicted Avg Value': float(prediction)  # Uverite se da je predikcija u ispravnom formatu
        }
        # Upisivanje predikcija u tabelu
        prediction_table.put_item(Item=prediction_item)

    return {
        'statusCode': 200,
        'body': json.dumps('Predikcije su uspešno upisane!')
    }