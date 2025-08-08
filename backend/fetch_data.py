import requests
from datetime import datetime
from database import insert_stock_data

def fetch_stock_data(symbol='AAPL'):
    url = f'https://query1.finance.yahoo.com/v7/finance/chart/{symbol}?range=1mo&interval=1d'
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch data")
        return []

    result = response.json()
    timestamps = result['chart']['result'][0]['timestamp']
    indicators = result['chart']['result'][0]['indicators']['quote'][0]
    prices = []

    for i in range(len(timestamps)):
        prices.append({
            'date': datetime.fromtimestamp(timestamps[i]).strftime('%Y-%m-%d'),
            'open': indicators['open'][i],
            'high': indicators['high'][i],
            'low': indicators['low'][i],
            'close': indicators['close'][i],
            'volume': indicators['volume'][i],
            'symbol': symbol
        })

    return prices

def fetch_and_store_latest_data(symbol='AAPL'):
    data = fetch_stock_data(symbol)
    for entry in data:
        insert_stock_data(entry)
