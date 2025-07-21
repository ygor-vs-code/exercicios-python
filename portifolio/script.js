function digitarTexto(elemento, texto, delay = 50, callback) {
    let i = 0;
    const intervalo = setInterval(() => {
        elemento.textContent += texto.charAt(i);
        i++;
        if (i === texto.length) {
            clearInterval(intervalo);
            if (callback) callback();
        }
    }, delay);
}

window.addEventListener("DOMContentLoaded", () => {
    const linha1 = document.getElementById("linha1");
    const linha2 = document.getElementById("linha2");

    digitarTexto(linha1, "$ python portifolio.py", 60, () => {
        setTimeout(() => {
            digitarTexto(linha2, "> Hello, World!", 60);
        }, 500);
    });
});






const btnTopo = document.getElementById("btnTopo");

window.addEventListener("scroll", () => {
    if (window.scrollY > 300) {
        btnTopo.classList.add("show");
    } else {
        btnTopo.classList.remove("show");
    }
});

btnTopo.addEventListener("click", () => {
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
});
