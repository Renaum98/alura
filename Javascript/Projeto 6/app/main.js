let livros = []
const endpointDaApi = 'https://guilhermeonrails.github.io/casadocodigo/livros.json';
getBuscarLivrosdaApi();


async function getBuscarLivrosdaApi() {
    const res = await fetch(endpointDaApi);
    livros = await res.json();
    let livrosComDesconto = aplicarDesconto(livros)
    exibirOsLivrosNaTela(livrosComDesconto);
}