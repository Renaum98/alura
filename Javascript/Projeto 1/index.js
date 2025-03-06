import { criarItemDaLista } from "./scripts/criaritemDaLista.js"; // função importada do modulo "script"
import verificarListaVazia from "./scripts/verificarListaVazia.js";//import default

const listaDeCompras = document.getElementById("lista-de-compras");
const botaoAdicionar = document.getElementById("adicionar-item")



botaoAdicionar.addEventListener("click", (evento) => {
    evento.preventDefault();
    const itemDaLista = criarItemDaLista();
    listaDeCompras.appendChild(itemDaLista);
    verificarListaVazia(listaDeCompras);
})


verificarListaVazia(listaDeCompras);