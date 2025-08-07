// Sample static data for companies
const stockData = {
    "TCS": {
        labels: ["2024-01-01", "2024-02-01", "2024-03-01", "2024-04-01"],
        data: [3100, 3200, 3300, 3450]
    },
    "INFY": {
        labels: ["2024-01-01", "2024-02-01", "2024-03-01", "2024-04-01"],
        data: [1400, 1445, 1490, 1530]
    },
    "RELIANCE": {
        labels: ["2024-01-01", "2024-02-01", "2024-03-01", "2024-04-01"],
        data: [2500, 2580, 2670, 2750]
    }
};

let chart;

function loadChart() {
    const company = document.getElementById("company").value;
    const ctx = document.getElementById("stockChart").getContext("2d");

    if (chart) chart.destroy(); // destroy existing chart before rendering new one

    chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: stockData[company].labels,
            datasets: [{
                label: company + " Stock Price",
                data: stockData[company].data,
                borderColor: 'blue',
                borderWidth: 2,
                fill: false
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    title: {
                        display: true,
                        text: "Price (INR)"
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: "Date"
                    }
                }
            }
        }
    });
}

function downloadChart() {
    html2canvas(document.getElementById('stockChart')).then(canvas => {
        const link = document.createElement('a');
        link.download = 'stock_chart.png';
        link.href = canvas.toDataURL();
        link.click();
    });
}

// Load chart on first page load
window.onload = loadChart;

