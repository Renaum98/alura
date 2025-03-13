//1-Criar uma função que exibe "Olá, mundo!" no console.

function olaMundo(){
    console.log('Olá, Mundo');
} 
olaMundo();  

//2-Criar uma função que recebe um nome como parâmetro e exibe "Olá, [nome]!" no console.

var nome = prompt('Digite se Nome: ')
function mostrarNome(n) {
    console.log(`Olá ${n}`);
}
mostrarNome(nome);

//3-Criar uma função que recebe um número como parâmetro e retorna o dobro desse número.

function numEmDobro(n) {
    let numero = parseInt(n)
    return numero*2
}
console.log(numEmDobro(10));

//4-Criar uma função que recebe três números como parâmetros e retorna a média deles.

const num1 = parseFloat(prompt('Digite o Primeiro numero:'));
const num2 = parseFloat(prompt('Digite o Segundo numero:'));
const num3 = parseFloat(prompt('Digite o Terceiro numero:'));

function media(n1,n2,n3) {

    return (n1 + n2 + n3) / 3;
}

console.log(`A média de ${num1}, ${num2} e ${num3} é: ${(media(num1,num2,num3)).toFixed(1)}`);

//5-Criar uma função que recebe dois números como parâmetros e retorna o maior deles.

function maiorNumero(n1,n2) {
    if (n1>n2){
        const maior = n1;
        return `${maior} é o maior numero`;
    }else if(n1 == n2){
        return 'Os dois valores são iguais';
    }else{
        const maior = n2;
        return `${n2} é o maior numero`;
    }
}
console.log(maiorNumero(8,8))

//6-Criar uma função que recebe um número como parâmetro e retorna o resultado da multiplicação desse número por ele mesmo

function multiplicação(n1) {
    return n1*n1
}
console.log(multiplicação(5))