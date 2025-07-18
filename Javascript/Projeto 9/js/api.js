const URL_BASE = "http://localhost:3000"


const api = {
    async buscarPensamentos() {
        try {
            const response = await fetch(`${URL_BASE}/pensamentos`)
            return await response.json()
        } 
        catch {
            alert('Erro ao buscar pensamentos')
            throw error
        }
    },
    async salvarPensamentos(pensamento) {
        try {
            const response = await fetch(`${URL_BASE}/pensamentos`,{
                method: "POST",
                headers: {
                    "Content-Type":"application/json"
                },
                body: JSON.stringify(pensamento)
            })
            return await response.json()
        } 
        catch {
            alert('Erro ao salvar pensamentos')
            throw error
        }
    },

    async buscarPensamentoPorId(id) {
        try {
            const response = await fetch(`${URL_BASE}/pensamentos/${id}`)
            return await response.json()
        } 
        catch {
            alert('Erro ao buscar pensamento por ID')
            throw error
        }
    },

    async editarPensamentos(pensamento) {
        try {
            const response = await fetch(`${URL_BASE}/pensamentos/${pensamento.id}`,{
                method: "PUT",
                headers: {
                    "Content-Type":"application/json"
                },
                body: JSON.stringify(pensamento)
            })
            return await response.json()
        } 
        catch {
            alert('Erro ao editar pensamento')
            throw error
        }
    },

    async exlcuirPensamentos(id) {
        try {
            const response = await fetch(`${URL_BASE}/pensamentos/${id}`,{
                method: "DELETE",
            })
        } 
        catch {
            alert('Erro ao excluir o pensamento')
            throw error
        }
    }
}

export default api;