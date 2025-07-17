import ui from './ui.js'
import api from './api.js'

document.addEventListener("DOMContentLoaded", () => {
    ui.rederizarPensamentos()

    const formularioPensamento = document.getElementById("pensamento-form")
    formularioPensamento.addEventListener("submit", manipularSubmissaoFormulario)
})

async function manipularSubmissaoFormulario(event) {
    event.preventDefault()
    const id = document.getElementById('pensamento-id').value
    const conteudo = document.getElementById('pensamento-conteudo').value
    const autoria = document.getElementById('pensamento-autoria').value

    try {
        if(id){
            await api.editarPensamentos({id, conteudo, autoria})
        }else {
            await api.salvarPensamentos({conteudo,autoria})
        }
        ui.rederizarPensamentos()
    } catch {
        alert('Erro ao salvar pensamento')
    }
}

const botaoCancelar = document.getElementById('botao-cancelar')
botaoCancelar.onclick = () => {
    document.getElementById("pensamento-form").reset()
}