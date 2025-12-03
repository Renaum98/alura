import './App.css'

//NO REACT COMPONENTES SÃO FUNÇÕES


//props é um objeto
// props.children
function TituloFormulario ({ children }) {
  return(
    <h2>{children}</h2>
  )
}

function CampoDeFormulario({ children }){
  return(
    <fieldset>
      {children}
    </fieldset>
  )
}

function Label({ children, htmlFor }){
  return(
    <label htmlFor={htmlFor}>
      {children}
    </label>
  )
}

function CampoDeEntrada({props}){
  return <input {...props}/>
}

function FormularioDeEvento(){
  return(
    <form className='form-evento'>
      <TituloFormulario>
        Preencha pra criar um evento:
        </TituloFormulario>
      <CampoDeFormulario>
        <Label htmlFor="nomeId">
          Qual o nome do evento?
        </Label>
        <CampoDeEntrada 
        type="text" 
        id="nomeId" 
        placeholder='Summer dev hits'/>
      </CampoDeFormulario>
    </form>
  )
}

function App() {
  return (
    <main>
      <header>
        <img src="/logo.png" alt="" />
      </header>
      <section>
        <img src="/banner.png" alt="" />
      </section>
      <FormularioDeEvento/>
    </main>
  )
}

export default App
