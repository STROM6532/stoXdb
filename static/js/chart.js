// chart.js - Chart.js rendering logic
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
        backgroundColor: 'rgba(0, 247, 255, 0.15)',
        fill: true,
        tension: 0.3
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { labels: { color: '#fff' } }
      },
      scales: {
        x: {
          title: { display: true, text: 'Date', color: '#fff' },
          ticks: { color: '#fff' }
        },
        y: {
          title: { display: true, text: 'Price (USD)', color: '#fff' },
          ticks: { color: '#fff' }
        }
      }
    }
  });
}

