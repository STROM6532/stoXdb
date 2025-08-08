# STOXDB Database Setup

This folder contains everything needed to set up and seed the MySQL database for the STOXDB project.

## Contents

- schema/create_tables.sql — SQL to define required tables.
- seed/sample_data.sql — Optional demo data for testing.
- procedures/stock_summary_proc.sql — (Optional) stored procedure to summarize stock data.
- scripts/init_db.py — Python script to run all SQL setup in one command.

## Usage

1. Make sure MySQL is running.
2. Update the credentials in init_db.py
3. Run:

```bash
python scripts/init_db.py
```

This will create the database, populate it with sample data, and create the stored procedure.

