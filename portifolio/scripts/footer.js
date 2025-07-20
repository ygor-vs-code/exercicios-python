function isInViewportFooter(element) {
    const rect = element.getBoundingClientRect();
    return (
        rect.top <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.bottom >= 0
    );
}

function mostrarFooter() {
    const footer = document.querySelector("#footer");
    if (isInViewportFooter(footer)) {
        footer.classList.add("show");
        window.removeEventListener("scroll", mostrarFooter);
    }
}

window.addEventListener("load", mostrarFooter);
window.addEventListener("scroll", mostrarFooter);
