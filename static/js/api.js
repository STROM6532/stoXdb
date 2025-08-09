// Handles API calls to Flask backend
const API_BASE = "http://127.0.0.1:5000"; // Change if different

async function fetchData(endpoint) {
    const res = await fetch(`${API_BASE}${endpoint}`);
    if (!res.ok) throw new Error(`Error: ${res.status}`);
    return res.json();
}
