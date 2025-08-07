import requests
import mysql.connector
import time

API_KEY = "your_alpha_vantage_api_key"  # Replace with your actual key

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="stock_db"
    )

def fetch_and_store(company_symbol, company_id):
    print(f"Fetching data for {company_symbol}")
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={company_symbol}&apikey={API_KEY}"

    response = requests.get(url)
    data = response.json()

    if "Time Series (Daily)" not in data:
        print("Invalid response or API limit hit.")
        return

    daily_data = data["Time Series (Daily)"]
    conn = connect_db()
    cursor = conn.cursor()

    for date, values in daily_data.items():
        try:
            cursor.execute("""
                INSERT INTO stock_prices (company_id, date, open_price, high, low, close_price, volume)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE close_price = VALUES(close_price)
            """, (
                company_id,
                date,
                float(values['1. open']),
                float(values['2. high']),
                float(values['3. low']),
                float(values['4. close']),
                int(values['5. volume'])
            ))
        except Exception as e:
            print(f"Error inserting {date}: {e}")
            continue

    conn.commit()
    cursor.close()
    conn.close()
    print(f"Data for {company_symbol} saved.")

# Example usage
if __name__ == '__main__':
    companies = {
        "TCS": 1,
        "INFY": 2,
        "RELIANCE": 3
    }
    for symbol, company_id in companies.items():
        fetch_and_store(symbol, company_id)
        time.sleep(15)  # Alpha Vantage limit: 5 requests/minute
