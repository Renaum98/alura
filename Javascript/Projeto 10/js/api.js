const URL_BASE = "http://localhost:3000"

const api = {
  async buscarPensamentos() {
    try {
      const response = await axios.get(`${URL_BASE}/pensamentos`)
      return await response.data
    }
    catch {
      alert('Erro ao buscar pensamentos')
      throw error
    }
  },

  async buscarPensamentoPorId(id) {
    try {
      const response = await axios.get(`${URL_BASE}/pensamentos/${id}`)
      return await response.data
    }
    catch {
      alert('Erro ao buscar pensamento')
      throw error
    }
  },

  async salvarPensamento(pensamento) {
    try {
      const response = await axios.post(`${URL_BASE}/pensamentos`, pensamento)
      return await response.data
    }
    catch {
      alert('Erro ao salvar pensamento')
      throw error
    }
  },

  async editarPensamento(pensamento) {
    try {
      const response = await axios.put(`${URL_BASE}/pensamentos/${pensamento.id}`, pensamento)
      return await response.data
    }
    catch {
      alert('Erro ao editar pensamento')
      throw error
    }
  },

  async excluirPensamento(id) {
    try {
      const response = await axios.delete(`${URL_BASE}/pensamentos/${id}`)
    }
    catch {
      alert('Erro ao excluir um pensamento')
      throw error
    }
  },
  async buscarPensamentoPorTermo(termo){
    try {
      const pensamentos = await this.buscarPensamento()
      const termoEmMinusculas = termo.toLowerCase()
  
      const pensamentosFiltrados = pensamentos.filter(pensamento => {
        return (pensamento.conteudo.toLowerCase().includes(termoEmMinusculas)) || pensamento.autoria.toLowerCase().includes(termoEmMinusculas)
      })
      return pensamentosFiltrados
      
    } 
    catch (error) {
      alert('Erro ao filtrar pensamentos')
      throw error
    }
  }   
}



export default api