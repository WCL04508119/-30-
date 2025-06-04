const express = require('express');
const path = require('path');
const Database = require('better-sqlite3');

const db = new Database('data.db');

// create tables if they don't exist
const createLogs = `CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    content TEXT NOT NULL
);`;
const createLinks = `CREATE TABLE IF NOT EXISTS links (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT NOT NULL,
    description TEXT
);`;

db.exec(createLogs);
db.exec(createLinks);

const app = express();
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));
app.use(express.static('public'));

// API routes for logs
app.get('/api/logs', (req, res) => {
    const logs = db.prepare('SELECT * FROM logs ORDER BY id DESC').all();
    res.json(logs);
});

app.post('/api/logs', (req, res) => {
    const { date, content } = req.body;
    const stmt = db.prepare('INSERT INTO logs (date, content) VALUES (?, ?)');
    const info = stmt.run(date, content);
    res.json({ id: info.lastInsertRowid });
});

app.put('/api/logs/:id', (req, res) => {
    const { id } = req.params;
    const { date, content } = req.body;
    const stmt = db.prepare('UPDATE logs SET date=?, content=? WHERE id=?');
    stmt.run(date, content, id);
    res.json({ message: 'updated' });
});

app.delete('/api/logs/:id', (req, res) => {
    const { id } = req.params;
    const stmt = db.prepare('DELETE FROM logs WHERE id=?');
    stmt.run(id);
    res.json({ message: 'deleted' });
});

// API routes for links
app.get('/api/links', (req, res) => {
    const links = db.prepare('SELECT * FROM links ORDER BY id DESC').all();
    res.json(links);
});

app.post('/api/links', (req, res) => {
    const { url, description } = req.body;
    const stmt = db.prepare('INSERT INTO links (url, description) VALUES (?, ?)');
    const info = stmt.run(url, description);
    res.json({ id: info.lastInsertRowid });
});

app.put('/api/links/:id', (req, res) => {
    const { id } = req.params;
    const { url, description } = req.body;
    const stmt = db.prepare('UPDATE links SET url=?, description=? WHERE id=?');
    stmt.run(url, description, id);
    res.json({ message: 'updated' });
});

app.delete('/api/links/:id', (req, res) => {
    const { id } = req.params;
    const stmt = db.prepare('DELETE FROM links WHERE id=?');
    stmt.run(id);
    res.json({ message: 'deleted' });
});

// frontend page
app.get('/', (req, res) => {
    res.render('index');
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log('Server running on port', PORT);
});

