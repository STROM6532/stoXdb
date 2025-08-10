import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS", "")
DB_NAME = os.getenv("DB_NAME", "stoxdb")

try:
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME
    )
    if conn.is_connected():
        print(f"✅ Successfully connected to MySQL database '{DB_NAME}'")
    conn.close()
except mysql.connector.Error as err:
    print(f"❌ Connection failed: {err}")
