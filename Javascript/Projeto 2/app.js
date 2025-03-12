alert("Ola Mundo");
let numeroSecreto = 29;
console.log(numeroSecreto)

let chute

while(chute != numeroSecreto){
    chute = prompt('Escolha um numero entre 1 e 30.');
    
    if (numeroSecreto == chute){
        alert(`Você acertou o numero secreto ${numeroSecreto}`)
        
    }else{
        if (chute > numeroSecreto) {
            alert(`O numero secreto é menor que ${chute}`)
        }
        else{
            alert(`O numero secreto é maior que ${chute}`)
        }
    }
};


