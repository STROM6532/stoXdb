document.addEventListener("DOMContentLoaded", () => {
    console.log("Welcome page loaded");

    const goBtn = document.getElementById("goDashboard");
    if (goBtn) {
        goBtn.addEventListener("click", () => {
            window.location.href = "dashboard.html";
        });
    }
});

