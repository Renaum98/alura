import "./App.css";
import { Banner } from "./componentes/Banner";
import { FormularioDeEvento } from "./componentes/FormularioDeEvento";
import { Tema } from "./componentes/Tema";

//NO REACT COMPONENTES SÃO FUNÇÕES

function App() {
  const temas = [
    {
      id: 1,
      nome: "front-end",
    },
    {
      id: 2,
      nome: "back-end",
    },
    {
      id: 3,
      nome: "dev-ops",
    },
    {
      id: 4,
      nome: "Inteligência artificial",
    },
    {
      id: 5,
      nome: "data science",
    },
    {
      id: 6,
      nome: "cloud",
    },
  ];

  return (
    <main>
      <header>
        <img src="/logo.png" alt="" />
      </header>
      <Banner />
      <FormularioDeEvento />
      {temas.map(function (item) { /*o map é quase igual o forEach com a diferença que retorna um valor*/
        return (
          <section key={item.id}>
            <Tema tema={item} />
          </section>
        );
      })}
    </main>
  );
}

export default App;
