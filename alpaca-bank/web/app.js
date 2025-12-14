const express = require('express');
const crypto = require('crypto');
const path = require('path');
const app = express();

const FLAG = process.env.FLAG ?? "Alpaca{**** REDACTED ****}";
const TRILLION = 1_000_000_000_000;

app.use(express.json());

const users = new Set();
const balances = new Map();

app.post('/api/register', (req, res) => {
    const id = crypto.randomBytes(10).toString('hex');
    users.add(id);
    balances.set(id, 10); // Initial balance
    res.status(201).json({ user: id });
});

app.get('/api/user/:user', (req, res) => {
    const user = req.params.user;
    if (!users.has(user)) return res.status(404).send({ error: 'User not found' });
    res.status(200).json({
        user: user,
        balance: balances.get(user),
        flag: balances.get(user) >= TRILLION ? FLAG : null // 🚩
    });
});

app.post('/api/transfer', (req, res) => {
    const { fromUser, toUser, amount } = req.body;

    if (!Number.isInteger(amount) || amount <= 0) {
        return res.status(400).send({ error: 'Invalid amount' });
    }
    if (!users.has(fromUser) || !users.has(toUser)) {
        return res.status(400).send({ error: 'Invalid user ID' });
    }

    const fromBalance = balances.get(fromUser);
    const toBalance = balances.get(toUser);
    if (fromBalance < amount) {
        return res.status(400).send({ error: 'Insufficient funds' });
    }
    
    balances.set(fromUser, fromBalance - amount);
    balances.set(toUser, toBalance + amount);

    res.status(200).json({
        receipt: `${fromUser} -> ${toUser} (${amount} yen)`
    });
});

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(3000, () => {
    console.log('Server listening on port 3000');
});