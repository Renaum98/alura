import api from "./api.js";
const ui = {
    async renderizarPets(){
        const listaPets = document.getElementById('caixa-pets')
        try {
            const pets = await api.buscarInformacoesPets();
            pets.forEach(pet => {
                listaPets.innerHTML += `
                <div>
                <ul>
                    <li>Especie: ${pet.especie}</li>
                    <li>Nome: ${pet.nome}</li>
                    <li>Raça: ${pet.raca}</li>
                </ul>
                </div>
                `
            });
        } catch (error) {
            console.error('Erro ao obter pets',error);
            alert('Erro ao obter pets. Tente novamente mais tarde.')
        }
    }

};
export default ui;