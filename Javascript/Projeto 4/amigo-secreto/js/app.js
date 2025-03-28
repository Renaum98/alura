//Objetivo do codigo é adicionar nomes a um programa e sortear entre eles 
//O primeiro passo é adicionar os nomes a uma lista
//Depois colocar esses nomes em exibição
//Logo apos definir a função do botão sortear e sorttear os nomes salvando em um dicionario talvez
let listaNomes = []

function adicionar() {
    let nome = document.getElementById('nome-amigo').value;
    if (nome == ''){
        alert('Digite um nome!')
        return
    }
    if (listaNomes.includes(nome)){
        alert('Nome ja cadastrado, coloque outro')
        return
    }
    let caixaNomes = document.getElementById('lista-amigos');
    listaNomes.push(nome)
    caixaNomes.textContent = listaNomes
    document.getElementById('nome-amigo').value = '';
}
function sortear() {
    if (listaNomes.length < 4){
        alert('Adicione pelo menos 4 amigos!');
        return;
    }
    embaralha(listaNomes);
    let sorteio = document.getElementById('lista-sorteio');

    for (let i = 0; i < listaNomes.length; i++){

        if (i == listaNomes.length - 1) {
            sorteio.innerHTML = sorteio.innerHTML + `${listaNomes[i]} => ${listaNomes[0]} <br>`
        }else{
            sorteio.innerHTML = sorteio.innerHTML + `${listaNomes[i]} => ${listaNomes[i+1]} <br>`
        }
    }
}
function reiniciar() {
    let listaNomes = []
    document.getElementById('lista-sorteio').textContent = '';
    document.getElementById('lista-amigos').textContent = ''
}
function embaralha(lista) {
    for (let indice = lista.length; indice; indice--){

        const indiceAleatorio = Math.floor(Math.random() * indice);

        [lista[indice - 1], lista[indiceAleatorio]] = [lista[indiceAleatorio], lista[indice - 1]];
    }
}