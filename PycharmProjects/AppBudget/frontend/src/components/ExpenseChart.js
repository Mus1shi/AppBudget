import { Bar } from 'react-chartjs-2';
import React, { useEffect, useState } from 'react';

const ExpenseChart = () => {
  const [chartData, setChartData] = useState({});

  useEffect(() => {
    fetch('/api/expense_summary/') // URL de l'API Django
      .then((response) => response.json())
      .then((data) => {
        const labels = data.map((item) => item.category__name);
        const values = data.map((item) => item.total);

        setChartData({
          labels: labels,
          datasets: [
            {
              label: 'Dépenses par catégorie',
              data: values,
              backgroundColor: 'rgba(75, 192, 192, 0.2)',
              borderColor: 'rgba(75, 192, 192, 1)',
              borderWidth: 1,
            },
          ],
        });
      });
  }, []);

  return (
    <div>
      <h2 className="text-2xl font-bold text-[#2E8B57] mb-4">
        Dépenses par catégorie
      </h2>
      {chartData.labels ? <Bar data={chartData} /> : <p>Chargement...</p>}
    </div>
  );
};

export default ExpenseChart;
