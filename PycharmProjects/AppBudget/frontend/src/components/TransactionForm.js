import React, { useState } from 'react';
import api from '../api';

const TransactionForm = () => {
    const [amount, setAmount] = useState('');
    const [category, setCategory] = useState('');
    const [currency, setCurrency] = useState('');

    const handleSubmit = (event) => {
        event.preventDefault();
        api.post('transactions/', { amount, category, currency })
            .then(() => {
                setAmount('');
                setCategory('');
                setCurrency('');
            })
            .catch((error) => console.error('Erreur lors de l’ajout de la transaction :', error));
    };

    return (
        <form
            className="p-4 bg-gray-100 rounded-lg shadow-md space-y-4"
            onSubmit={handleSubmit}
        >
            <h2 className="text-2xl font-semibold mb-4">Ajouter une Transaction</h2>
            <div className="space-y-2">
                <label className="block">
                    <span className="text-gray-700">Montant :</span>
                    <input
                        type="number"
                        value={amount}
                        onChange={(e) => setAmount(e.target.value)}
                        className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-200"
                        required
                    />
                </label>
                <label className="block">
                    <span className="text-gray-700">Catégorie :</span>
                    <input
                        type="text"
                        value={category}
                        onChange={(e) => setCategory(e.target.value)}
                        className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-200"
                        required
                    />
                </label>
                <label className="block">
                    <span className="text-gray-700">Devise :</span>
                    <input
                        type="text"
                        value={currency}
                        onChange={(e) => setCurrency(e.target.value)}
                        className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-200"
                        required
                    />
                </label>
            </div>
            <button
                type="submit"
                className="px-4 py-2 bg-blue-500 text-white rounded-lg shadow hover:bg-blue-600 focus:outline-none focus:ring focus:ring-blue-200"
            >
                Ajouter
            </button>
        </form>
    );
};

export default TransactionForm;
