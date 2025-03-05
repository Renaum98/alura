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

    inputCheckbox.addEventListener("click", function(){
        if (inputCheckbox.checked) {
            nomeItem.style.textDecoration = "line-through";
        }
        else{
            nomeItem.style.textDecoration = "none"
        } 
    })

    containerItemDaLista.appendChild(inputCheckbox);
    containerItemDaLista.appendChild(nomeItem);
    itemDaLista.appendChild(containerItemDaLista);

    const diaDaSemana = new Date().toLocaleDateString("pt-BR", {weekday: "long"}); 
    const data = new Date().toLocaleDateString("pt-BR");
    const hora = new Date().toLocaleTimeString("pt-BR", {
        hour: "numeric",
        minute:"numeric"
    })
    const dataCompleta = `${diaDaSemana} (${data}) às ${hora}`
    const itemData = document.createElement("p");
    itemData.classList.add("texto-data");

    itemData.innerText = dataCompleta;

    itemDaLista.appendChild(itemData)
    //usando o new date é possivel adicionar um data completa e horario atual
    //é possivel tambem formatar a forma que sera exibida
    
    listaDeCompras.appendChild(itemDaLista);

    // com 3 iguais (===) ele compara se o tipo e o valor do que é comparado é igual
    // com return sem nenhum valor atribuido, ele sai da condicional apos ela ser verdadeira
    verificarListaVazia();
})

const mensagemListaVazia = document.querySelector(".mensagem-lista-vazia");

function verificarListaVazia(){
    const itensDaLista = listaDeCompras.querySelectorAll("li");
    if(itensDaLista.length === 0){
        mensagemListaVazia.style.display = "block"
    }
    else{
        mensagemListaVazia.style.display = "none"
    }
}
verificarListaVazia();