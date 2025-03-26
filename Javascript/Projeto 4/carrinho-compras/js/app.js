const carrinhoLista = document.getElementById('lista-produtos');
const valorTotal = document.getElementById('valor-total')
let valorFinal = 0

function adicionar() {
    //recuperar valores nome, quantidade e valor
    let valorProduto = document.getElementById('produto').value.split("-");
    let valorQuantidade = document.getElementById('quantidade').value;
    //condicional para não aceitar valores 0 ou menores na quantidade
    if (valorQuantidade <= 0){
        alert('Digite uma quantidade.')
        return
    }
    let precoProduto = valorProduto[1].split('R$')[1];
    let nomeProduto = valorProduto[0];
    
    //calcular o preço
    let subtotalProduto = parseInt(valorQuantidade) * parseInt(precoProduto);
    valorFinal += subtotalProduto;

    //devolvendo ao html as informações
    let cadaItem = document.createElement('section');
    cadaItem.classList.add('carrinho__produtos__produto');
    cadaItem.innerHTML = `<span class="texto-azul">${valorQuantidade}x</span> ${nomeProduto} <span class="texto-azul">R$${precoProduto}</span>` 

    carrinhoLista.appendChild(cadaItem);

    valorTotal.innerHTML = `R$${valorFinal}`;

    document.getElementById('quantidade').value = ''
}

function limpar() {
    document.getElementById('quantidade').value = ''
    carrinhoLista.innerHTML = ''
    valorTotal.innerHTML = 'R$0'
}
