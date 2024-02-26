import React from 'react';
import Header from './BibleAPP/Header';
import MainContent from './BibleAPP/MainContent';
// Importação do CSS do Tailwind gerado (assumindo que você adicionou as diretivas do Tailwind em index.css)
import './index.css'; 

function App() {
  return (
    <div className="App"> {/* Você pode começar a usar as classes do Tailwind aqui. Por exemplo, use "App" para aplicar estilos. */}
      <Header />
      <MainContent />
    </div>
  );
}

export default App;
