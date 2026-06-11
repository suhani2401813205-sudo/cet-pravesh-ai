const express = require('express');
const { spawn } = require('child_process');
const path = require('path');

const app = express();
const PORT = 3000;

// JSON body parse karne ke liye
app.use(express.json());

// CORS — frontend se request allow karo
app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Headers', 'Content-Type');
    next();
});

// Static frontend files serve karo
app.use(express.static(path.join(__dirname, '../frontend')));

// Main API endpoint
app.post('/recommend', (req, res) => {
    const { percentile, branch, city, max_fees, priority } = req.body;

    // Python script call karo
    const args = [
    path.join(__dirname, 'recommend.py'),
    percentile,
    branch,
    city || '',
    max_fees ? max_fees.toString() : '',
    priority || 'placement'
];

   const pythonCmd = process.platform === 'win32' ? 'py' : 'python3';
const python = spawn(pythonCmd, args);

    let result = '';
    let error = '';

    // Python ka output pakdo
    python.stdout.on('data', (data) => {
        result += data.toString();
    });

    // Error pakdo
    python.stderr.on('data', (data) => {
        error += data.toString();
    });

    // Python khatam hone pe response bhejo
    python.on('close', (code) => {
        if (code !== 0) {
            return res.status(500).json({ error: error });
        }
        try {
            const colleges = JSON.parse(result);
            res.json({ success: true, colleges });
        } catch (e) {
            res.status(500).json({ error: 'Parsing error' });
        }
    });
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});