# STOXDB Database Setup

This folder contains all SQL and scripts to set up and seed the STOXDB MySQL database.

## 📂 Structure
- **schema/** → SQL files to create tables
- **seed/** → SQL files with sample data
- **procedures/** → SQL stored procedures/views
- **scripts/** → Python automation scripts
- **README.md** → This guide

## ⚙️ Setup Steps

1. **Create `.env` file** in project root:
    ```
    DB_HOST=localhost
    DB_USER=root
    DB_PASS=yourpassword
    DB_NAME=stoxdb
    ```

2. **Install dependencies**:
    ```bash
    pip install mysql-connector-python python-dotenv
    ```

3. **Run the init script**:
    ```bash
    python database/scripts/init_db.py
    ```

4. **Verify in MySQL**:
    ```sql
    USE stoxdb;
    SHOW TABLES;
    SELECT * FROM companies;
    ```

You now have a ready-to-use database with sample data.
