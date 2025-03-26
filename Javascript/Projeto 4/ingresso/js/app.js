//objetivo: diminuir a quantidade disponivel de ingressos com base na compra do usuario
let campoPista = document.getElementById('qtd-pista');
let campoSuperior = document.getElementById('qtd-superior');
let campoInferior = document.getElementById('qtd-inferior');
campoPista.value = 100
campoSuperior.value = 200
campoInferior.value = 400
let novoValor = valorFinal = 0

function comprar() {
    let selecaoIngressos = document.getElementById('tipo-ingresso').value;
    let selecaoQuantidade = document.getElementById('qtd').value
    
    if (selecaoQuantidade <= 0){
        alert('Digite uma quantidade válida')
        return
    }
    
    switch (selecaoIngressos) {
        case 'inferior':
            novoValor = campoInferior.value - selecaoQuantidade;
            if(novoValor < 0) {
                qtdeIndisponivel()
                break;
            }else{
                campoInferior.textContent = novoValor;
                campoInferior.value -= selecaoQuantidade;
                break;
            } 
            
        case 'superior':
            novoValor = campoSuperior.value - selecaoQuantidade;
            if (novoValor < 0) {
                qtdeIndisponivel()
                break;
            }else{
                campoSuperior.value -= selecaoQuantidade;
                campoSuperior.textContent = novoValor;
                break; 
            }
            
        case 'pista':
            novoValor = campoPista.value - selecaoQuantidade;
            if (novoValor < 0) {
                qtdeIndisponivel()
                break;
            } else {
                campoPista.value -= selecaoQuantidade;
                campoPista.textContent = novoValor
                break;  
            }

        default:
            alert('Nenhuma opção selecionada.')
            break;
        }
    document.getElementById('qtd').value = ''

            
}
function qtdeIndisponivel() {
    alert('Os ingressos para essa categoria acabaram.')
}