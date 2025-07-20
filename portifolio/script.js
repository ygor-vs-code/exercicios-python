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
