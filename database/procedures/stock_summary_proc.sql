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
