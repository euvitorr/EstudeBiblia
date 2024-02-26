import React, { useState, useEffect, useRef } from 'react';

function UserProfile({ user }) {
  // Dados fictícios para livros e capítulos
  const books = [
    { id: 'gen', name: 'Gênesis', chapters: 50 },
    { id: 'exo', name: 'Êxodo', chapters: 40 },
    // Adicione mais conforme necessário
  ];

  // Estados
  const [isBooksDropdownOpen, setIsBooksDropdownOpen] = useState(false);
  const [isChaptersDropdownOpen, setIsChaptersDropdownOpen] = useState(false);
  const [selectedBook, setSelectedBook] = useState(books[0]);
  const [selectedChapter, setSelectedChapter] = useState('1');
  const [searchTerm, setSearchTerm] = useState('');


  // Referências
  const booksDropdownRef = useRef(null);
  const chaptersDropdownRef = useRef(null);

  // Funções para controle dos dropdowns
  const toggleBooksDropdown = () => setIsBooksDropdownOpen(!isBooksDropdownOpen);
  const toggleChaptersDropdown = () => setIsChaptersDropdownOpen(!isChaptersDropdownOpen);

  const selectBook = (book) => {
    setSelectedBook(book);
    setIsBooksDropdownOpen(false);
    // Reseta o capítulo selecionado ao mudar o livro
    setSelectedChapter('1');
  };

  const selectChapter = (chapter) => {
    setSelectedChapter(chapter);
    setIsChaptersDropdownOpen(false);
  };

  // Efeito para adicionar o ouvinte de eventos para cliques fora dos dropdowns
  useEffect(() => {
    function handleClickOutside(event) {
      if (booksDropdownRef.current && !booksDropdownRef.current.contains(event.target)) {
        setIsBooksDropdownOpen(false);
      }
      if (chaptersDropdownRef.current && !chaptersDropdownRef.current.contains(event.target)) {
        setIsChaptersDropdownOpen(false);
      }
    }
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  // Gerar capítulos com base no livro selecionado
  const chapters = Array.from({ length: selectedBook.chapters }, (_, i) => `${i + 1}`);

  return (
    <div className="p-4 md:p-8 shadow-md relative bg-white">
      <div className="flex items-center">
        <img src={user.image} className="w-10 h-10 block rounded object-cover object-top" alt="Profile" />
        <div className="text-indigo-600 font-medium ml-3">{user.name}</div>
      </div>

      <div className="mt-6 flex">
        <div className="relative inline-block text-left" ref={booksDropdownRef}>
          <button onClick={toggleBooksDropdown} className="bg-indigo-500 text-white py-2 text-sm px-3 rounded focus:outline-none">
             {selectedBook.name}
          </button>
          {isBooksDropdownOpen && (
            <div className="overflow-y-auto max-h-80 absolute z-10 mt-2 w-56 origin-top-right rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
              {books.map((book) => (
                <link key={book.id} className="block px-4 py-2 text-sm text-gray-700 hover:bg-indigo-500 hover:text-white cursor-pointer" onClick={() => selectBook(book)}>
                  {book.name}
                </link>
              ))}
            </div>
          )}
        </div>

        <div className="relative inline-block text-left  pl-2 " ref={chaptersDropdownRef}>
          <button onClick={toggleChaptersDropdown} className="bg-indigo-500 text-white py-2 text-sm px-3 rounded focus:outline-none">
             {selectedChapter}
          </button>
          {isChaptersDropdownOpen && (
            <div className="overflow-y-auto max-h-80 absolute z-10 mt-2 w-56 origin-top-right rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
              {chapters.map((chapter) => (
                <link key={chapter} className="block px-4 py-2 text-sm text-gray-700 hover:bg-indigo-500 hover:text-white cursor-pointer" onClick={() => selectChapter(chapter)}>
                  {chapter}
                </link>
              ))}
            </div>
          )}
        </div>


        <div className="relative ml-auto flex-1 pl-2 sm:block hidden">
          <input
            type="text"
            placeholder="Pesquisar em toda bíblia"
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-full border rounded border-gray-400 h-full focus:outline-none pl-4 pr-8 text-gray-700 text-sm"
          />
        </div>
      </div>
    </div>
  );
}

export default UserProfile;
