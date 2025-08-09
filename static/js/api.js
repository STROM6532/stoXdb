// api.js - Backend API calls
function loadChart(symbol) {
  fetch(`/api/data?symbol=${symbol}`)
    .then(res => res.json())
    .then(data => {
      if (!data.length) {
        alert(`⚠ No data found for symbol: ${symbol}`);
        return;
      }
      renderChart(data);
    })
    .catch(err => console.error('❌ API Error:', err));
}


