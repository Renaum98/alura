alert("Olá Mundo");
let numeroSecreto = Math.random(0,10);
console.log(numeroSecreto);
let chute;
let cont = 1

while(chute != numeroSecreto){
    chute = prompt('Escolha um numero entre 1 e 10.');
    if (numeroSecreto == chute){
        break;
    }else{
        if (chute > numeroSecreto) {
            alert(`O numero secreto é menor que ${chute}`)
        }
        else{
            alert(`O numero secreto é maior que ${chute}`)
        }
        cont++;
    }
};

let palavraTentativa = cont > 1 ? 'tentativas' : 'tentativa'
alert(`Você acertou o numero secreto ${numeroSecreto} com ${cont} ${palavraTentativa}.`)




/*if (cont > 1){
    alert(`Você acertou o numero secreto ${numeroSecreto} com ${cont} ${palavraTentativa}.`)
}else{
    alert(`Você acertou o numero secreto ${numeroSecreto} com ${cont} ${palavraTentativa}.`)
}*/


