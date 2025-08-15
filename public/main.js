async function fetchLogs() {
    const res = await fetch('/api/logs');
    const logs = await res.json();
    const list = document.getElementById('log-list');
    list.innerHTML = '';
    logs.forEach(log => {
        const li = document.createElement('li');
        li.innerHTML = `<span>${log.date} - ${log.content}</span>
            <button onclick="editLog(${log.id}, '${log.date}', '${log.content.replace(/'/g,"&#39;")}')">编辑</button>
            <button onclick="deleteLog(${log.id})">删除</button>`;
        list.appendChild(li);
    });
}

async function fetchLinks() {
    const res = await fetch('/api/links');
    const links = await res.json();
    const list = document.getElementById('link-list');
    list.innerHTML = '';
    links.forEach(link => {
        const li = document.createElement('li');
        li.innerHTML = `<span><a href="${link.url}" target="_blank">${link.url}</a> - ${link.description || ''}</span>
            <button onclick="editLink(${link.id}, '${link.url}', '${(link.description||'').replace(/'/g,"&#39;")}')">编辑</button>
            <button onclick="deleteLink(${link.id})">删除</button>`;
        list.appendChild(li);
    });
}

// Log functions
async function saveLog(e) {
    e.preventDefault();
    const id = document.getElementById('log-id').value;
    const date = document.getElementById('log-date').value;
    const content = document.getElementById('log-content').value;
    if (id) {
        await fetch(`/api/logs/${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ date, content })
        });
    } else {
        await fetch('/api/logs', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ date, content })
        });
    }
    document.getElementById('log-form').reset();
    fetchLogs();
}

function editLog(id, date, content) {
    document.getElementById('log-id').value = id;
    document.getElementById('log-date').value = date;
    document.getElementById('log-content').value = content;
}

async function deleteLog(id) {
    await fetch(`/api/logs/${id}`, { method: 'DELETE' });
    fetchLogs();
}

// Link functions
async function saveLink(e) {
    e.preventDefault();
    const id = document.getElementById('link-id').value;
    const url = document.getElementById('link-url').value;
    const description = document.getElementById('link-desc').value;
    if (id) {
        await fetch(`/api/links/${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url, description })
        });
    } else {
        await fetch('/api/links', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url, description })
        });
    }
    document.getElementById('link-form').reset();
    fetchLinks();
}

function editLink(id, url, description) {
    document.getElementById('link-id').value = id;
    document.getElementById('link-url').value = url;
    document.getElementById('link-desc').value = description;
}

async function deleteLink(id) {
    await fetch(`/api/links/${id}`, { method: 'DELETE' });
    fetchLinks();
}

// Event listeners

document.getElementById('log-form').addEventListener('submit', saveLog);
document.getElementById('link-form').addEventListener('submit', saveLink);

fetchLogs();
fetchLinks();
