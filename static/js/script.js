document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    if (form) {
        form.addEventListener("submit", function () {
            // Création d'une zone d'affichage pour le chronomètre si elle n'existe pas
            let timerDiv = document.getElementById("loading-timer");
            if (!timerDiv) {
                timerDiv = document.createElement("div");
                timerDiv.id = "loading-timer";
                timerDiv.style.marginTop = "15px";
                timerDiv.style.fontSize = "16px";
                timerDiv.style.fontWeight = "bold";
                timerDiv.style.color = "#007bff";
                form.appendChild(timerDiv);
            }

            // Démarrage du chronomètre en millisecondes pour plus de précision
            const startTime = performance.now();
            const interval = setInterval(() => {
                const elapsed = ((performance.now() - startTime) / 1000).toFixed(1);
                timerDiv.innerHTML = `⏳ Analyse en cours... (${elapsed}s)`;
            }, 100);
        });
    }
});