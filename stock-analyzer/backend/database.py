import mysql.connector
from datetime import datetime

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",    # replace with your MySQL password
        database="stock_db"          # replace with your actual DB name
    )

def get_stock_data(company_symbol):
    conn = connect_db()
    cursor = conn.cursor()
    
    query = """
        SELECT date, close_price
        FROM stock_prices
        WHERE company_id = (
            SELECT company_id FROM companies WHERE symbol = %s
        )
        ORDER BY date ASC
    """
    cursor.execute(query, (company_symbol,))
    results = cursor.fetchall()
    
    labels = [row[0].strftime("%Y-%m-%d") for row in results]
    prices = [row[1] for row in results]
    
    cursor.close()
    conn.close()

    return {"labels": labels, "data": prices}

