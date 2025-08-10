import mysql.connector
import os
from dotenv import load_dotenv

# Load env variables
load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS", "")
DB_NAME = os.getenv("DB_NAME", "stoxdb")

# BASE_DIR should point to the 'database' folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
# ^ Moves up from scripts/ to database/

def run_sql_file(cursor, filepath):
    """Reads and executes SQL commands from a file."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"SQL file not found: {filepath}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        sql_commands = f.read().split(';')
        for command in sql_commands:
            command = command.strip()
            if command:
                cursor.execute(command)

def init_database():
    """Initialize the MySQL database by creating tables and inserting sample data."""
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS
    )
    cursor = conn.cursor()

    # Create DB if it doesn't exist
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    conn.database = DB_NAME

    # Create tables
    print("Creating tables...")
    run_sql_file(cursor, os.path.join(BASE_DIR, "schema", "create_tables.sql"))

    # Insert sample data
    print("Inserting sample data...")
    run_sql_file(cursor, os.path.join(BASE_DIR, "seed", "sample_data.sql"))

    conn.commit()
    cursor.close()
    conn.close()
    print(f"✅ Database '{DB_NAME}' initialized successfully.")

if __name__ == "__main__":
    init_database()
