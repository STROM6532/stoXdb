-- Insert sample companies
INSERT INTO companies (symbol, name, sector) VALUES
('AAPL', 'Apple Inc.', 'Technology'),
('GOOGL', 'Alphabet Inc.', 'Technology'),
('MSFT', 'Microsoft Corp.', 'Technology');

-- Insert sample stock prices
INSERT INTO stock_prices (company_id, date, open, high, low, close, volume) VALUES
(1, '2025-08-01', 185.00, 187.50, 183.00, 186.75, 50000000),
(1, '2025-08-02', 186.75, 188.00, 185.50, 187.20, 48000000),
(2, '2025-08-01', 2800.00, 2850.00, 2785.00, 2825.50, 1500000),
(3, '2025-08-01', 330.00, 335.00, 328.50, 334.00, 25000000);
