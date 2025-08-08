INSERT INTO stock_prices (symbol, date, open, high, low, close, volume) VALUES
('AAPL', '2025-08-01', 192.5, 194.2, 191.0, 193.8, 45000000),
('AAPL', '2025-08-02', 193.8, 195.5, 192.0, 194.9, 47000000),
('AAPL', '2025-08-03', 194.9, 197.0, 194.5, 196.7, 46000000);

-- 📁 database/procedures/stock_summary_proc.sql
USE stoxdb;

DELIMITER //
CREATE PROCEDURE GetStockSummary(IN stockSymbol VARCHAR(10))
BEGIN
    SELECT 
        symbol,
        COUNT(*) AS total_days,
        AVG(close) AS avg_close,
        MAX(high) AS max_high,
        MIN(low) AS min_low
    FROM stock_prices
    WHERE symbol = stockSymbol
    GROUP BY symbol;
END //
DELIMITER ;

