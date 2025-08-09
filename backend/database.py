import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()  # Load DB credentials from .env

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASS", ""),
        database=os.getenv("DB_NAME", "stoxdb")
    )
