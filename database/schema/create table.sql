-- create_tables.sql
drop database stoxdb;
CREATE DATABASE IF NOT EXISTS stoxdb;
USE stoxdb;

CREATE TABLE IF NOT EXISTS companies (
  id INT AUTO_INCREMENT PRIMARY KEY,
  symbol VARCHAR(16) NOT NULL UNIQUE,
  name VARCHAR(255) NOT NULL,
  sector VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS stock_prices (
  id BIGINT AUTO_INCREMENT PRIMARY KEY,
  company_id INT NOT NULL,
  date DATE NOT NULL,
  open DECIMAL(12,4),
  high DECIMAL(12,4),
  low DECIMAL(12,4),
  close DECIMAL(12,4),
  volume BIGINT,
  INDEX idx_company_date (company_id, date),
  FOREIGN KEY (company_id) REFERENCES companies(id)
);
