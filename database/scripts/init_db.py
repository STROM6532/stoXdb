# init_db.py
import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()  # reads .env from project root if present

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS", "")       # set '' if no password
DB_NAME = os.getenv("DB_NAME", "stoxdb")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # project root

def run_sql_file(cursor, filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        sql = f.read()
    # split by ; but keep procedures which may contain delimiter — simple approach:
    # If files are simple (no custom delimiters except procedures) this works.
    statements = [s.strip() for s in sql.split(';') if s.strip()]
    for stmt in statements:
        cursor.execute(stmt)

def init_database():
    # Connect without database to create it first
    conn = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASS)
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    conn.database = DB_NAME

    print("Creating tables...")
    run_sql_file(cursor, os.path.join(BASE_DIR, "database", "schema", "create_tables.sql"))

    print("Seeding sample data...")
    run_sql_file(cursor, os.path.join(BASE_DIR, "database", "seed", "sample_data.sql"))

    conn.commit()
    cursor.close()
    conn.close()
    print("Database initialized successfully.")

if __name__ == "__main__":
    init_database()
