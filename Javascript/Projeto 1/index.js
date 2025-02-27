const inputItem = document.getElementById("input-item")
const listaDeCompras = document.getElementById("lista-de-compras");
const botaoAdicionar = document.getElementById("adicionar-item")
let contador = 0;


botaoAdicionar.addEventListener("click", (evento) => {
    evento.preventDefault();
    if(inputItem.value === ""){
        alert('Digite um valor valido!');
        return
    }

    const itemDaLista = document.createElement("li");
    const containerItemDaLista = document.createElement("div")
    containerItemDaLista.classList.add("lista-item-container");
    const inputCheckbox = document.createElement("input");
    inputCheckbox.type = "checkbox";
    inputCheckbox.id = "checkbox-" + contador++;
    const nomeItem = document.createElement("p");
    nomeItem.innerText = inputItem.value;

    containerItemDaLista.appendChild(inputCheckbox);
    containerItemDaLista.appendChild(nomeItem);

    itemDaLista.appendChild(containerItemDaLista);

    listaDeCompras.appendChild(itemDaLista);

    // com 3 iguais (===) ele compara se o tipo e o valor do que é comparado é igual
    // com return sem nenhum valor atribuido, ele sai da condicional apos ela ser verdadeira
})