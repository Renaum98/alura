function sortear(){
    //Aqui foi recuperado os valores que vão ser usados no sorteio dos numeros
    let valorQuantidade = parseInt(document.querySelector('#quantidade').value);
    let valorDe = parseInt(document.querySelector('#de').value);
    let valorAte = parseInt(document.querySelector('#ate').value);

    //Uma lista vazia criada para armazenar os numeros sorteados
    let listaSorteados = []

    //Condicional para caso o Usuario não digite todos os valores necessarios
    if (valorQuantidade == '' || valorAte == '' || valorDe == '') {
        alert('ERRO, digite um número em todos os campos.')
        return
    }

    //Um loop com a quantidade de numeros que o Usuario definir em valorQuantidade
    for(let i = 0; i < valorQuantidade; i++){
        let sorteador = obterNumeroAleatorio(valorDe,valorAte);

        while (listaSorteados.includes(sorteador)) {
            sorteador = obterNumeroAleatorio(valorDe,valorAte);
        }


        //numero adicionado a lista criada anteriormente
        listaSorteados.push(sorteador);
    }
    //Recuperando o campo no html onde sera exibido o valor gerado
    let resultadoLista = document.querySelector('#resultado');
    //Apresentando o valor gerado no HTML 
    resultadoLista.innerHTML = `<label class="texto__paragrafo">Números sorteados:  ${listaSorteados}</label>`;
}

function obterNumeroAleatorio(min,max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function reiniciar(){
    
}