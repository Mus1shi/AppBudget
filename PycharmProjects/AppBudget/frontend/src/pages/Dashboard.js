import React from 'react';
import ExpenseChart from '../components/ExpenseChart';

const Dashboard = () => {
  return (
    <div className="container mx-auto px-4">
      <h1 className="text-3xl font-bold text-[#2E8B57] mb-6">
        Tableau de bord
      </h1>
      <ExpenseChart />
    </div>
  );
};

export default Dashboard;
