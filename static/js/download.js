// download.js - Download chart as PNG
document.getElementById('download-chart')?.addEventListener('click', () => {
  const canvas = document.getElementById('stockChart');
  const image = canvas.toDataURL('image/png');
  const link = document.createElement('a');
  link.href = image;
  link.download = 'stoxdb_chart.png';
  link.click();
});


