function isInViewportContato(el) {
    const rect = el.getBoundingClientRect();
    return (
        rect.top <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.bottom >= 0
    );
}

function mostrarContato() {
    const contato = document.querySelector("#contato");
    if (isInViewportContato(contato)) {
        contato.classList.add("show");
        window.removeEventListener("scroll", mostrarContato);
    }
}

window.addEventListener("load", mostrarContato);
window.addEventListener("scroll", mostrarContato);
