// Fonction pour récupérer les données du backend
async function fetchData() {
    try {
        const response = await fetch('http://localhost:5000/data');
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Erreur lors de la récupération des données :', error);
    }
}

// Fonction pour afficher les données dans le tableau
async function displayData() {
    const tableBody = document.getElementById('data-table').getElementsByTagName('tbody')[0];
    const data = await fetchData();

    // Efface le contenu actuel du tableau
    tableBody.innerHTML = '';

    // Remplit le tableau avec les données
    data.forEach(item => {
        const row = tableBody.insertRow();
        const cell1 = row.insertCell(0);
        const cell2 = row.insertCell(1);
        cell1.textContent = item.id;
        cell2.textContent = item.value;
    });
}

// Appelle la fonction pour afficher les données au chargement de la page
displayData();
