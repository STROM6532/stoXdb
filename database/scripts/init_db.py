import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS", "")
DB_NAME = os.getenv("DB_NAME", "stoxdb")

def run_sql_file(cursor, filepath):
    with open(filepath, 'r') as f:
        sql_commands = f.read().split(';')
        for command in sql_commands:
            if command.strip():
                cursor.execute(command)

def init_database():
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS
    )
    cursor = conn.cursor()

    # Create DB if not exists
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    conn.database = DB_NAME

    # Create tables
    print("Creating tables...")
    run_sql_file(cursor, os.path.join("database", "schema", "create_tables.sql"))

    # Seed data
    print("Inserting sample data...")
    run_sql_file(cursor, os.path.join("database", "seed", "sample_data.sql"))

    # Stored procedures
    print("Creating stored procedures...")
    run_sql_file(cursor, os.path.join("database", "procedures", "stock_summary_proc.sql"))

    conn.commit()
    cursor.close()
    conn.close()
    print("Database initialized successfully!")

if __name__ == "__main__":
    init_database()
