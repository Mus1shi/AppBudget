import React, { useEffect, useState } from 'react';
import api from '../api';
import useWebSocket from 'react-use-websocket';

const TransactionList = () => {
    const [transactions, setTransactions] = useState([]);
    const { lastJsonMessage } = useWebSocket('ws://127.0.0.1:8000/ws/transactions/');

    useEffect(() => {
        api.get('transactions/')
            .then((response) => setTransactions(response.data))
            .catch((error) => console.error('Erreur lors de la récupération des transactions :', error));
    }, []);

    useEffect(() => {
        if (lastJsonMessage) {
            setTransactions((prev) => [...prev, lastJsonMessage]);
        }
    }, [lastJsonMessage]);

    return (
        <div className="p-4 bg-gray-100 rounded-lg">
            <h2 className="text-2xl font-semibold mb-4">Liste des Transactions</h2>
            <ul className="space-y-2">
                {transactions.map((transaction) => (
                    <li
                        key={transaction.id}
                        className="p-3 bg-white shadow-md rounded-md border-l-4 border-blue-500"
                    >
                        {transaction.amount} {transaction.currency} - {transaction.category}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default TransactionList;
