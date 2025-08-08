import mysql.connector

def run_sql_file(path, cursor):
    with open(path, 'r') as file:
        sql = file.read()
        for statement in sql.split(';'):
            if statement.strip():
                cursor.execute(statement)

def initialize_database():
    conn = mysql.connector.connect(
        host='localhost',
        user='your_username',
        password='your_password'
    )
    cursor = conn.cursor()

    run_sql_file('../schema/create_tables.sql', cursor)
    run_sql_file('../seed/sample_data.sql', cursor)
    run_sql_file('../procedures/stock_summary_proc.sql', cursor)

    conn.commit()
    cursor.close()
    conn.close()
    print("Database initialized with schema, sample data, and procedures.")

if __name__ == '__main__':
    initialize_database()

