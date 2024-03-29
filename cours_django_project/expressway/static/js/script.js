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
