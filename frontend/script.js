async function generatePlan() {
    const prompt = document.getElementById("prompt").value;

    if (!prompt) {
        alert("Please enter an idea");
        return;
    }

    const outputDiv = document.getElementById("output");
    outputDiv.innerHTML = "<p>⏳ Generating business plan...</p>";

    try {
        const response = await fetch(
            `http://127.0.0.1:8000/generate?prompt=${encodeURIComponent(prompt)}`
        );

        const data = await response.json();

        // Display formatted output
        outputDiv.innerHTML = formatOutput(data.output);

        // Show download button
        document.getElementById("downloadBtn").style.display = "block";

    } catch (error) {
        outputDiv.innerHTML = "<p style='color:red;'>❌ Error generating plan</p>";
        console.error(error);
    }
}


// Format text into structured HTML
function formatOutput(text) {
    let formatted = text;

    // Main title
    formatted = formatted.replace(
        /================ BUSINESS PLAN ================/g,
        "<h2>🚀 Business Plan</h2>"
    );

    // Section separators
    formatted = formatted.replace(
        /----------------------------------------------/g,
        "<hr>"
    );

    // Section headings
    formatted = formatted.replace(/IDEA:/g, "<h3>💡 Idea</h3>");
    formatted = formatted.replace(/MARKET ANALYSIS:/g, "<h3>📊 Market Analysis</h3>");
    formatted = formatted.replace(/BUSINESS MODEL:/g, "<h3>🏗️ Business Model</h3>");
    formatted = formatted.replace(/GROWTH STRATEGY:/g, "<h3>📈 Growth Strategy</h3>");

    // Convert "- point" into list items
    formatted = formatted.replace(/^- (.*)$/gm, "<li>$1</li>");

    // Wrap list items in <ul>
    formatted = formatted.replace(/(<li>.*<\/li>)/gs, "<ul>$1</ul>");

    // Line breaks
    formatted = formatted.replace(/\n/g, "<br>");

    return formatted;
}


// Download DOCX file
function downloadPlan() {
    const prompt = document.getElementById("prompt").value;

    if (!prompt) {
        alert("Please enter an idea first");
        return;
    }

    window.open(
        `http://127.0.0.1:8000/download?prompt=${encodeURIComponent(prompt)}`
    );
}