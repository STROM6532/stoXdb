USE stoxdb;
DELIMITER //
CREATE PROCEDURE GetStockSummary(IN stockSymbol VARCHAR(16))
BEGIN
  SELECT c.symbol,
         MIN(sp.low) AS lowest_price,
         MAX(sp.high) AS highest_price,
         ROUND(AVG(sp.close), 2) AS average_close
  FROM stock_prices sp
  JOIN companies c ON sp.company_id = c.id
  WHERE c.symbol = stockSymbol
  GROUP BY c.symbol;
END //
DELIMITER ;
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'mypassword';
FLUSH PRIVILEGES;
