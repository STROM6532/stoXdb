function loadChart(symbol) {
  fetch(`/api/data?symbol=${symbol}`)
    .then(res => res.json())
    .then(data => renderChart(data))
    .catch(err => console.error('API error:', err));
}

