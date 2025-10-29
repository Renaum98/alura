import ui from "./ui.js"
import api from "./api.js"

const pensamentoSet = new Set()


async function adicionarChaveAoPensamento() {
  try {
    const pensamentos = await api.buscarPensamentos()
    pensamentos.forEach(pensamento => {
      const chavePensamento = 
      `${pensamento.conteudo.trim().toLowerCase()}-${pensamento.autoria.trim().toLowerCase()}`
      pensamentoSet.add(chavePensamento);
    })
  } catch (error) {
    alert('Erro ao adicionar chave ao pensamento')
  }
}




function removerEspacos(string) {
  return string.replaceAll(/\s+/g, '')
}

const regexConteudo = /^[A-Za-z\s]{10,}$/;

const regexAutoria = /^[a-zA-Z]{3,10}$/;

function validarAutoria(autoria) {
  return regexAutoria.test(autoria)
}

function validarConteudo(conteudo) {
  return regexConteudo.test(conteudo)
}

document.addEventListener("DOMContentLoaded", () => {
  ui.renderizarPensamentos()
  adicionarChaveAoPensamento()

  const formularioPensamento = document.getElementById("pensamento-form")
  const botaoCancelar = document.getElementById("botao-cancelar")
  const inputBusca = document.getElementById("campo-busca")

  formularioPensamento.addEventListener("submit", manipularSubmissaoFormulario)
  botaoCancelar.addEventListener("click", manipularCancelamento)
  inputBusca.addEventListener("input", manipularBusca)
})

async function manipularSubmissaoFormulario(event) {
  event.preventDefault()
  const id = document.getElementById("pensamento-id").value
  const conteudo = document.getElementById("pensamento-conteudo").value
  const autoria = document.getElementById("pensamento-autoria").value
  const data = document.getElementById("pensamento-data").value//pega o campo(input) data na aplicação  

  const conteudoSemEspacos = removerEspacos(conteudo)
  const autoriaSemEspacos = removerEspacos(autoria)
  
  if(!validarConteudo(conteudoSemEspacos)){
    alert("é permitido a inclusão apenas de letras e espaços com no minimo 10 caracteres")
    return
  }

  if(!validarAutoria(autoriaSemEspacos)){
    alert("So é permitido cadastrar autor com 3 a 15 caracteres")
    return
  }

  if (!validarData(data)) {
    alert("Não é permitido o cadastro de datas futuras.")
  } //o evento so ocorrera se a data nao for validada

  const chaveNovoPensamento = 
  `${conteudo.trim().toLowerCase()}-${autoria.trim().toLowerCase()}`

  if(pensamentoSet.has(chaveNovoPensamento)){
    alert('Esse pensamento ja existe')
    return
  }

  try {
    if (id) {
      await api.editarPensamento({ id, conteudo, autoria, data })
    } else {
      await api.salvarPensamento({ conteudo, autoria, data })
    }
    ui.renderizarPensamentos()
  } catch {
    alert("Erro ao salvar pensamento")
  }
}

function manipularCancelamento() {
  ui.limparFormulario()
}

async function manipularBusca() {
  const termoBusca = document.getElementById("campo-busca").value
  try {
    const pensamentosFiltrados = await api.buscarPensamentosPorTermo(termoBusca)
    console.log(pensamentosFiltrados)
    ui.renderizarPensamentos(pensamentosFiltrados)
  } catch (error) {
    alert("Erro ao realizar busca")
  }
}

//função para validar a data não permitindo que seja selecionado uma data futura
function validarData(data) {
  const dataAtual = new Date()//metodo construtor para pegar uma data, se ficar em branco ira pegar a data atual
  const dataInserida = new Date(data)
  return dataInserida <= dataAtual //so ira retornar a dataInserida se for igual ou menor que a atual
}