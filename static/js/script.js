function openNav() {
    document.getElementById("myNav").style.width = "100%";
}

function closeNav() {
    document.getElementById("myNav").style.width = "0%";
}

// Get the current URL pathname
const currentPath = window.location.pathname;

// Select all navigation links
const navigationLinks = document.querySelectorAll('nav ul li a');

// Loop through the links and compare their href with the current URL
navigationLinks.forEach(link => {
    if (link.getAttribute('href') === currentPath) {
        link.parentElement.classList.add('active'); // Add "active" class to parent <li>
    }
});