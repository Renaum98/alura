//Crie uma função que calcule o índice de massa corporal (IMC) de uma pessoa, a partir de sua altura, em metros, e peso, em quilogramas, que serão recebidos como parâmetro.

function calcIMC(altura,peso) {
    parseFloat(altura)
    parseFloat(peso)
    return peso / (altura**2)
}
console.log(`Seu IMC é igual a: ${calcIMC(1.80,86.20).toFixed(2)}`)

//Crie uma função que calcule o valor do fatorial de um número passado como parâmetro.

//Crie uma função que converte um valor em dólar, passado como parâmetro, e retorna o valor equivalente em reais. Para isso, considere a cotação do dólar igual a R$4,80.

function conversor(valor) {
    parseFloat(valor);
    return valor * 4.80;
}
console.log(`O valor em reais é igual a R$${conversor(8).toFixed(2)}`)

//Crie uma função que mostre na tela a área e o perímetro de uma sala retangular, utilizando altura e largura que serão dadas como parâmetro.

function areaPerimetro(altura,largura) {
    parseFloat(altura,largura)
    return altura*largura
}

//Crie uma função que mostre na tela a área e o perímetro de uma sala circular, utilizando seu raio que será fornecido como parâmetro. Considere Pi = 3,14.

//Crie uma função que mostre na tela a tabuada de um número dado como parâmetro.
function tabuada(numero) {
    let cont = 0
    while (cont!=11) {
        console.log(`${numero} x ${cont} = ${numero*cont}`);
        cont++
    }
}
tabuada(2)