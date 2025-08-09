document.addEventListener("DOMContentLoaded", async () => {
    const chartContainer = document.getElementById("chart-container");
    const stockList = document.getElementById("stock-list");

    // Fetch stock data from API
    const stocks = await fetchData("stocks");

    if (stocks && stocks.length > 0) {
        stockList.innerHTML = "";
        stocks.forEach(stock => {
            const card = document.createElement("div");
            card.className = "stock-card";
            card.innerHTML = `
                <h3>${stock.symbol} - ${stock.name}</h3>
                <p>Price: ${formatCurrency(stock.price)}</p>
                <p>Sector: ${stock.sector}</p>
            `;
            stockList.appendChild(card);
        });

        // Example placeholder chart (can integrate Chart.js later)
        chartContainer.innerHTML = `<div class="chart-title">Stock Prices Overview</div>
                                    <p>📊 Chart will render here...</p>`;
    } else {
        stockList.innerHTML = `<p>⚠️ No stock data available</p>`;
    }
});

