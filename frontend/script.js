async function generatePlan() {
    const prompt = document.getElementById("prompt").value;

    if (!prompt) {
        alert("Please enter an idea");
        return;
    }

    document.getElementById("output").innerText = "Generating...";

    try {
        const response = await fetch(`http://127.0.0.1:8000/generate?prompt=${encodeURIComponent(prompt)}`);
        const data = await response.json();

        document.getElementById("output").innerText =
            JSON.stringify(data.data, null, 2);

        document.getElementById("downloadBtn").style.display = "block";

    } catch (error) {
        document.getElementById("output").innerText = "Error generating plan";
        console.error(error);
    }
}

function downloadPlan() {
    const prompt = document.getElementById("prompt").value;

    window.open(`http://127.0.0.1:8000/download?prompt=${encodeURIComponent(prompt)}`);
}