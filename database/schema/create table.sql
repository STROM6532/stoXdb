-- Drop old tables if exist
DROP TABLE IF EXISTS stock_prices;
DROP TABLE IF EXISTS companies;

-- Companies table
CREATE TABLE companies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    symbol VARCHAR(10) NOT NULL UNIQUE,
    name VARCHAR(100) NOT NULL,
    sector VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Stock prices table
CREATE TABLE stock_prices (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    company_id INT NOT NULL,
    date DATE NOT NULL,
    open DECIMAL(10, 2),
    high DECIMAL(10, 2),
    low DECIMAL(10, 2),
    close DECIMAL(10, 2),
    volume BIGINT,
    FOREIGN KEY (company_id) REFERENCES companies(id) ON DE_
