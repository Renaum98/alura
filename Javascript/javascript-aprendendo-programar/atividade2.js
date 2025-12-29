//1. Verificação de idade para compra de bebida

const idade = 10;
if (idade >= 18) {
  console.log("Pode comprar bebida alcoólica");
} else {
  console.log("Venda proibida para menores de 18 anos");
}

//2. Saudação de acordo com a hora
const horaAtual = new Date().getHours();

if (horaAtual.getHours >= 6 && horaAtual < 12) {
  console.log("Bom dia");
} else if (horaAtual.getHours >= 12 && horaAtual < 18) {
  console.log("Boa Tarde");
} else {
  console.log("Boa Noite");
}

//3. Verificação de número positivo ou negativo
const num = 10

//4. Conversão de nota em conceito
//5. Número par ou ímpar com ternário
//6. Menu com switch-case
//7. Validação de campo obrigatório
//8. Validação de senha segura
//9. Compra com saldo
//10. Validação de formulário completo
