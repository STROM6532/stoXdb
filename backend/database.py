import mysql.connector
import os

def get_connection():
    return mysql.connector.connect(
        host='localhost',
        user='your_username',
        password='your_password',
        database='stoxdb'
    )

def insert_stock_data(entry):
    conn = get_connection()
    cursor = conn.cursor()

    query = '''
    INSERT INTO stock_prices (symbol, date, open, high, low, close, volume)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        open=VALUES(open),
        high=VALUES(high),
        low=VALUES(low),
        close=VALUES(close),
        volume=VALUES(volume)
    '''
    cursor.execute(query, (
        entry['symbol'], entry['date'], entry['open'],
        entry['high'], entry['low'], entry['close'], entry['volume']
    ))

    conn.commit()
    cursor.close()
    conn.close()

def get_stock_data(symbol='AAPL'):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = '''
    SELECT date, open, high, low, close, volume
    FROM stock_prices
    WHERE symbol = %s
    ORDER BY date DESC
    LIMIT 30
    '''
    cursor.execute(query, (symbol,))
    result = cursor.fetchall()

    cursor.close()
    conn.close()
    return result

