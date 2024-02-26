import React from 'react';

function NotesSection({ annotations }) {
  return (
    <div className="overflow-auto flex-grow">
      {annotations.map((annotation, index) => (
        <div key={index} className="bg-gray-200 px-8 py-6 flex items-center border-b border-gray-300">
          <div className="flex ml-4">
            <div className="flex flex-col pl-4 pr-8">
              <h2 className="font-medium text-sm">{annotation.title}</h2>
              <h3 className="text-gray-500 text-sm">{annotation.content}</h3>
              <h3 className="text-gray-500 text-sm mt-2">{annotation.start_verse} - {annotation.end_verse}</h3>
            </div>
          </div>
          <button className="text-gray-500 flex items-center text-sm focus:outline-none rounded ml-auto py-2 leading-none">
            {/* Ícone de edição */}
            <svg stroke="currentColor" strokeWidth="2" fill="none" strokeLinecap="round" strokeLinejoin="round" className="w-4 h-4 mr-2" viewBox="0 0 24 24">
              <path d="M12 20h9"/>
              <path d="M16.5 3.5a2.121 2.121 0 013 3L12 14l-4 1 1-4 7.5-7.5z"/>
            </svg>
            Editar Anotação
          </button>
        </div>
      ))}
    </div>
  );
}

export default NotesSection;
