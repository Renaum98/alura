//Valores que sempre são Falsy

const numero = 0;
const indefinido = undefined;
const nulo = null;
const textoVazio = "";
const notANumber = NaN;

//qualquer valor que nao esteja nessa lista é considerado Truthy

const nome = "marcos";

if (nome) {
  console.log(`Ola ${nome}`);
} else {
  console.log("Ainda não sei o seu nome");
}

const idade = 16;

if (idade != null) {
  if (idade >= 18) {
    console.log("Maior de idade");
  } else if (idade >= 0 && idade < 18) {
    console.log("Menor de idade");
  }
}
