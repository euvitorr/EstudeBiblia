import React, { useState, useEffect } from 'react';

// Dados temporários simulando livros e seus capítulos
const temporaryBooks = [
  { id: 'gen', name: 'Gênesis' },
  { id: 'exo', name: 'Êxodo' },
  // Adicione mais livros conforme desejar
];

function VerseSelector() {
  const [selectedBook, setSelectedBook] = useState('');
  const [chapters, setChapters] = useState([]);
  const [selectedChapter, setSelectedChapter] = useState('');

  // Quando um livro é selecionado, atualize a lista de capítulos
  useEffect(() => {
    if (selectedBook) {
      // Simulando a busca de capítulos do livro selecionado
      const fetchedChapters = [
        { id: '1', name: 'Capítulo 1' },
        { id: '2', name: 'Capítulo 2' },
        // Adicione mais capítulos conforme necessário
      ];
      setChapters(fetchedChapters);
      setSelectedChapter('');
    }
  }, [selectedBook]);

  const handleBookChange = (e) => {
    const newSelectedBook = e.target.value;
    setSelectedBook(newSelectedBook);
    // Simulação de callback ao selecionar um livro
    console.log(`Livro selecionado: ${newSelectedBook}`);
  };

  const handleChapterChange = (e) => {
    const newSelectedChapter = e.target.value;
    setSelectedChapter(newSelectedChapter);
    // Simulação de callback ao selecionar um capítulo
    console.log(`Capítulo selecionado: ${newSelectedChapter}`);
  };

  return (
    <div>
      <div className="relative inline-block text-left mb-4">
        <select value={selectedBook} onChange={handleBookChange} className="dropdown-button bg-white rounded border px-4 py-2">
          <option value="">Selecione um livro</option>
          {temporaryBooks.map((book) => (
            <option key={book.id} value={book.id}>{book.name}</option>
          ))}
        </select>
      </div>
      <div className="relative inline-block text-left">
        <select value={selectedChapter} onChange={handleChapterChange} className="dropdown-button bg-white rounded border px-4 py-2" disabled={!selectedBook}>
          <option value="">Selecione um capítulo</option>
          {chapters.map((chapter) => (
            <option key={chapter.id} value={chapter.id}>{chapter.name}</option>
          ))}
        </select>
      </div>
    </div>
  );
}

export default VerseSelector;
