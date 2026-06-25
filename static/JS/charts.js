document.addEventListener("DOMContentLoaded", function () {
  const ctx = document.getElementById("categoryChart");

  if (!ctx) return;

  new Chart(ctx, {
    type: "pie",
    data: {
      labels: window.categoryLabels,
      datasets: [
        {
          data: window.categoryValues,
          backgroundColor: [
            "#ff6384",
            "#36a2eb",
            "#ffce56",
            "#4caf50",
            "#9c27b0",
          ],
        },
      ],
    },
    options: {
      plugins: {
        legend: {
          position: "bottom",
        },
      },
    },
  });
});
