// NAVBAR
let header = document.querySelector('header');
let links = document.querySelectorAll('header nav a span');

header.addEventListener('mouseover', () => {
    links.forEach(link => {
        link.style.display = 'block';
    });
});

header.addEventListener('mouseout', () => {
    links.forEach(link => {
        link.style.display = 'none';
    });
});


// BARRE DE RECHERCHE
let form = document.querySelector('#search');

form.addEventListener('submit', (event) => {

    event.preventDefault();

    let valeur = document.querySelector('#search_bar').value;

    if (!isNaN(valeur)) {
        window.location.href = 'show/' + valeur;
    } else {
        alert("Veuillez entrer un nombre valide.");
    }
});