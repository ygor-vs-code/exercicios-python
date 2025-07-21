function isInViewportProjetos(el) {
    const rect = el.getBoundingClientRect();
    return (
        rect.top <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.bottom >= 0
    );
}

function mostrarProjetos() {
    const secao = document.querySelector("#projetos");
    if (isInViewportProjetos(secao)) {
        secao.classList.add("show");
        window.removeEventListener("scroll", mostrarProjetos);
    }
}

window.addEventListener("load", mostrarProjetos);
window.addEventListener("scroll", mostrarProjetos);
