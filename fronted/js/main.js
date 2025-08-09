// Common functions for all pages

// Format currency values
function formatCurrency(value) {
    return `$${Number(value).toFixed(2)}`;
}

// Show a toast message
function showToast(message, type = "info") {
    const toast = document.createElement("div");
    toast.className = `toast toast-${type}`;
    toast.textContent = message;
    document.body.appendChild(toast);
    setTimeout(() => toast.remove(), 3000);
}

// Page ready log
document.addEventListener("DOMContentLoaded", () => {
    console.log("STOXDB frontend loaded");
});

