import gerarDiaDaSemana from "./gerarDiaDaSemana.js";
const inputItem = document.getElementById("input-item")
let contador = 0;

export function criarItemDaLista() {
    
    if(inputItem.value === ""){
        alert('Digite um valor valido!');
        return
    } // export usado antes da função para dizer ao sistema que essa função vai ser usada em outro lugar

    const itemDaLista = document.createElement("li");// criando um elemento dentro do html
    const containerItemDaLista = document.createElement("div")
    containerItemDaLista.classList.add("lista-item-container");//adicionando uma classe ao elemento div criado
    const inputCheckbox = document.createElement("input");//add um input 
    inputCheckbox.type = "checkbox"; // colocando o tipo de input criado como um "checkbox"
    inputCheckbox.id = "checkbox-" + contador++; // criando um id personalizado ao input
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

    const dataCompleta = gerarDiaDaSemana();

    const itemData = document.createElement("p");
    itemData.classList.add("texto-data");

    itemData.innerText = dataCompleta;

    itemDaLista.appendChild(itemData);
    //usando o new date é possivel adicionar um data completa e horario atual
    //é possivel tambem formatar a forma que sera exibida
    // com 3 iguais (===) ele compara se o tipo e o valor do que é comparado é igual
    // com return sem nenhum valor atribuido, ele sai da condicional apos ela ser verdadeir
    return itemDaLista;
}
