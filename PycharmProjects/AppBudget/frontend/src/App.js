import React from 'react';
import Dashboard from './components/Dashboard';
import TransactionList from './components/TransactionList';
import TransactionForm from './components/TransactionForm';

const App = () => {
    return (
        <div className="min-h-screen bg-gray-100">
            <header className="bg-blue-600 text-white p-4">
                <h1 className="text-3xl font-bold">Application de Budget</h1>
            </header>
            <main className="container mx-auto p-4 space-y-8">
                <Dashboard />
                <TransactionForm />
                <TransactionList />
            </main>
        </div>
    );
};

export default App;
