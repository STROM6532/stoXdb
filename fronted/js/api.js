// Centralized API interaction functions
const API_BASE_URL = "http://localhost:5000/api"; // Flask backend URL

// Generic GET request
async function fetchData(endpoint) {
    try {
        const res = await fetch(`${API_BASE_URL}/${endpoint}`);
        if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);
        return await res.json();
    } catch (err) {
        console.error("API Fetch Error:", err);
        return null;
    }
}

// Generic POST r

