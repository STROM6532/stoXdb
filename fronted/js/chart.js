let chart;
function renderChart(data) {
  const ctx = document.getElementById('stockChart').getContext('2d');
  const labels = data.map(entry => entry.date).reverse();
  const prices = data.map(entry => entry.close).reverse();

  if (chart) chart.destroy();

  chart = new Chart(ctx, {
    type: 'line',
    data: {
      labels,
      datasets: [{
        label: 'Closing Price',
        data: prices,
        borderColor: '#00f7ff',
        fill: false
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { display: true }
      },
      scales: {
        x: { title: { display: true, text: 'Date' } },
        y: { title: { display: true, text: 'Price (USD)' } }
      }
    }
  });
}

