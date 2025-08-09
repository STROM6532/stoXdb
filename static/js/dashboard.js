
document.addEventListener("DOMContentLoaded", async () => {
    try {
        const data = await fetchData("/api/stocks");
        renderStocks(data);
    } catch (err) {
        console.error(err);
    }
});

function renderStocks(stocks) {
    const container = document.getElementById("stock-container");
    container.innerHTML = "";
    stocks.forEach(stock => {
        const div = document.createElement("div");
        div.classList.add("stock-card");
        div.innerHTML = `<h3>${stock.name}</h3><p>Price: $${stock.price}</p>`;
        container.appendChild(div);
    });
}
