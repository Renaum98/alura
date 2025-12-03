import "./App.css";
import { FormularioDeEvento } from "./componentes/FormularioDeEvento";

//NO REACT COMPONENTES SÃO FUNÇÕES

function App() {
  return (
    <main>
      <header>
        <img src="/logo.png" alt="" />
      </header>
      <section>
        <img src="/banner.png" alt="" />
      </section>
      <FormularioDeEvento />
    </main>
  );
}

export default App;
