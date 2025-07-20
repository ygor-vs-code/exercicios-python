function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
        rect.top <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.bottom >= 0
    );
}

function animateOnScroll() {
    const sobre = document.querySelector("#sobre");
    if (isInViewport(sobre)) {
        sobre.classList.add("show");
        iniciarDigitacao();
        window.removeEventListener("scroll", animateOnScroll);
    }
}

window.addEventListener("load", animateOnScroll);
window.addEventListener("scroll", animateOnScroll);

function iniciarDigitacao() {
    const textoElemento = document.getElementById("textoDigitado");
    const texto = textoElemento.getAttribute("data-text");
    let index = 0;

    function digitar() {
        if (index < texto.length) {
            
            if (texto.charAt(index) === '\\' && texto.charAt(index + 1) === 'n') {
                textoElemento.innerHTML += '<br>';
                index += 2;
            } else {
                textoElemento.innerHTML += texto.charAt(index);
                index++;
            }
            setTimeout(digitar, 20);
        }
    }

    if (!textoElemento.dataset.digitado) {
        textoElemento.dataset.digitado = "true";
        digitar();
    }
}