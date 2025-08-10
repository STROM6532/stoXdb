USE stoxdb;

INSERT INTO companies (symbol, name, sector) VALUES
('AAPL', 'Apple Inc.', 'Technology'),
('MSFT', 'Microsoft Corporation', 'Technology'),
('GOOGL', 'Alphabet Inc.', 'Technology');

INSERT INTO stock_prices (company_id, date, open, high, low, close, volume) VALUES
(1, '2025-08-01', 190.12, 193.50, 189.80, 192.33, 53400000),
(1, '2025-08-02', 192.40, 195.00, 191.50, 194.85, 48900000),
(2, '2025-08-01', 320.50, 325.10, 318.90, 324.00, 30000000),
(3, '2025-08-01', 140.00, 145.00, 139.50, 144.25, 28000000);
