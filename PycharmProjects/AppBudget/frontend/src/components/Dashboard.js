import React, { useEffect, useState } from 'react';
import api from '../api';

const Dashboard = () => {
    const [summary, setSummary] = useState([]);

    useEffect(() => {
        api.get('transactions/summary/')
            .then((response) => setSummary(response.data))
            .catch((error) => console.error('Erreur lors de la récupération du résumé :', error));
    }, []);

    return (
        <div className="p-4 bg-gray-100 rounded-lg">
            <h2 className="text-2xl font-semibold mb-4">Tableau de Bord</h2>
            <ul className="space-y-2">
                {summary.map((item, index) => (
                    <li
                        key={index}
                        className="p-3 bg-white shadow-md rounded-md border-l-4 border-blue-500"
                    >
                        <span className="font-bold">{item['category__name']}:</span> {item.total} €
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Dashboard;
