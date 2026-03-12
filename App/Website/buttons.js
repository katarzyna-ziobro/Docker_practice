document.getElementById("luckyBtn").addEventListener("click", async () => {
    const response = await fetch("/lucky");
    const data = await response.json();

    document.getElementById("result").innerText = data.number;
});