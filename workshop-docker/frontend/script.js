const api = "http://127.0.0.1:8000/workshops";

document.getElementById("workshopForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const id = document.getElementById("id").value;
    const titulo = document.getElementById("titulo").value;
    const descricao = document.getElementById("descricao").value;
    const data = document.getElementById("data").value;

    const response = await fetch(api, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id, titulo, descricao, data }),
    });

    if (response.ok) {
        document.getElementById("workshopForm").reset();
        carregarWorkshops();
    } else {
        alert("Erro ao cadastrar workshop.");
    }
});

async function carregarWorkshops() {
    const lista = document.getElementById("lista");
    lista.innerHTML = "";

    const response = await fetch(api);
    const workshops = await response.json();

    workshops.forEach(w => {
        const item = document.createElement("li");
        item.className = "list-group-item";
        item.textContent = `${w.titulo} (${w.data}) - ${w.descricao}`;
        lista.appendChild(item);
    });
}

carregarWorkshops();