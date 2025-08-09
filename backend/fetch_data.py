import yfinance as yf
from database import get_db_connection

def fetch_and_store(symbol, company_id):
    print(f"Fetching data for {symbol}...")
    stock = yf.Ticker(symbol)
    hist = stock.history(period="1y")  # last 1 year

    conn = get_db_connection()
    cursor = conn.cursor()

    for date, row in hist.iterrows():
        cursor.execute("""
            INSERT INTO stock_prices (company_id, date, open, high, low, close, volume)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                open=VALUES(open),
                high=VALUES(high),
                low=VALUES(low),
                close=VALUES(close),
                volume=VALUES(volume)
        """, (
            company_id, date.date(), float(row['Open']), float(row['High']),
            float(row['Low']), float(row['Close']), int(row['Volume'])
        ))

    conn.commit()
    cursor.close()
    conn.close()
    print(f"Data stored for {symbol}")

if __name__ == "__main__":
    # Example usage: fetch for Apple
    fetch_and_store("AAPL", 1)
