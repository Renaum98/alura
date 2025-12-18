//atividade 1 - Boas-vindas personalizadas
let nome = "Renan Matos";
console.log(`Olá ${nome}, seja bem vindo.`);
//atividade 2 - Cálculo de idade
let anoAtual = 2025;
let anoAniversario = 1998;
let idade = anoAtual - anoAniversario;

console.log(`Você tem ${idade} anos atualmente`);

//atividade 3 - Mensagem de localização

let cidade = "São Paulo";
let estado = "SP";
let pais = "Brasil";

console.log(`Você mora em ${cidade}-${estado},${pais}`);

//atividade 4 -Tipo da variável:

let temCarteira = true;
console.log(typeof temCarteira);

//atividade 5 - Simulação bancária simples:

let saldo = 0;
let deposito = 200;
let saque = 50;
console.log(`
    |Seu saldo atual R$:${saldo},00
    |Foi depositado R$:${deposito},00
    |Foi sacado R$:${saque},00
    |Seu saldo atual é R$:${(saldo = deposito - saque)},00
    `);

//atividade 6 - Média de notas:

let matematica = 2;
let portugues = 5;
let ciencias = 1;

console.log(`
    |Boletim Escolar
    |Portugues = ${portugues}
    |Matematica = ${matematica}
    |Ciencias = ${ciencias}
    |Média Final = ${(portugues + matematica + ciencias) / 3}`);

//atividade 7 - Reajuste de salário:

let salario = 3000;
let porcentagem = 20;
let aumento = salario + (salario * porcentagem) / 100;
console.log(`
    |Salario atual: R$${salario}
    |Aumento: ${porcentagem}%
    |Salario com aumento: R$${aumento}`)

//atividade 8 - Contador de cliques:

let cliques = 0; 

cliques++; 

cliques++; 

cliques++; 

console.log("O botão foi clicado " + cliques + " vezes."); 

//atividade 9 - Constantes não podem ser alteradas

const PI = 3.14; 

// PI = 3.1415; // ❌ Isso causaria erro pois constantes não podem ser modificadas 

console.log("PI é uma constante e não pode ser alterada: " + PI);

//atividade 10 - Concatenando tipos diferentes

let mensagem = "O número é "; 

let numero = 42; 

let combinado = mensagem + numero; 

console.log(combinado); // "O número é 42" 

console.log(typeof combinado); // string 
