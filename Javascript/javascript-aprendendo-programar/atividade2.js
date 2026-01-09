//1. Verificação de idade para compra de bebida

const idade = 10;
if (idade >= 18) {
  console.log("Pode comprar bebida alcoólica");
} else {
  console.log("Venda proibida para menores de 18 anos");
}

//2. Saudação de acordo com a hora
const horaAtual = new Date().getHours();

if (horaAtual >= 6 && horaAtual < 12) {
  console.log("Bom dia");
} else if (horaAtual >= 12 && horaAtual < 18) {
  console.log("Boa Tarde");
} else {
  console.log("Boa Noite");
}

//3. Verificação de número positivo ou negativo
const num = -5

if (num > 0) {
  console.log(`${num} é positivo`)
} else if (num < 0) {
  console.log(`${num} é Negativo`)
} else {
  console.log(`${num} é 0`)
}

//4. Conversão de nota em conceito
const nota = 5
if (nota >= 9 && nota <= 10) {
  console.log('Sua nota foi A');
} else if (nota >= 8 && nota < 9) {
  console.log('Sua nota foi B');
} else if (nota >= 6 && nota <= 7.9) {
  console.log('Sua nota foi C');
} else if (nota >= 4 && nota <= 5.9) {
  console.log('Sua nota foi D')
} else if (nota >= 0 && nota <= 3.9) {
  console.log('Sua nota foi E')
}
//5. Número par ou ímpar com ternário

let numero2 = 7; 

let resultado = (numero2 % 2 === 0) ? "Par" : "Ímpar"; 

console.log(`O número é: ${resultado}`); 

//6. Menu com switch-case
const opcao = 3
switch (opcao) {
  case 1:
    console.log('Cadastrar')
    break;
  case 2:
    console.log('Listar')
    break
  case 3:
    console.log('Sair')
    break
  default:
    break;
}

//7. Validação de campo obrigatório
const email = ""
if (!email) {
  console.log('Cadastre um email')
} else {
  console.log('E-mail válido')
}

//8. Validação de senha segura
const senha = ""
const senhaValida = false

if (senhaValida) {
  console.log('Senha Valida')
} else {
  console.log('Senha muito curta')
}


//9. Compra com saldo
const saldoDisponivel = 250.10
const valorCompra = 135.95
if (saldoDisponivel < valorCompra) {
  console.log(`
    Saldo indisponivel
    O valor da compra é de ${valorCompra} e seu saldo é ${saldoDisponivel}`)
} else {
  console.log(`
    Compra aprovada no valor:
    R$${valorCompra}
    Seu novo saldo é de R$${saldoDisponivel - valorCompra}`)
}
//10. Validação de formulário completo
const nome = ''
const email2 = ''
const anos = ''
const formularioValido = true

if (formularioValido) {
  console.log("Formulário enviado com sucesso");
} else {
  console.log("Por favor, preencha todos os campos corretamente");
}