//Objetivo do codigo é adicionar nomes a um programa e sortear entre eles 
//O primeiro passo é adicionar os nomes a uma lista
//Depois colocar esses nomes em exibição
//Logo apos definir a função do botão sortear e sorttear os nomes salvando em um dicionario talvez
function adicionar() {
    let nome = document.getElementById('nome-amigo').value;
    let caixaNomes = document.getElementById('lista-amigos');
    if (nome == ''){
        alert('Digite um nome!')
        return
    }
    caixaNomes.textContent = nome
}