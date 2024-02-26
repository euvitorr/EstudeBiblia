import React from 'react';

function VersesSection({ verses }) {
  return (
    <div className="lg:w-1/2 bg-indigo-600 text-white flex flex-col">
      <div className="p-8 flex flex-1 items-start overflow-auto">
        <div className="flex-1 pl-10">
          <form id="formNote">
            {verses.map((verse, index) => (
              <div key={index} className="flex mb-8">
                <input
                  id={`indigo-checkbox-${index}`}
                  type="checkbox"
                  className="w-4 h-4 text-indigo-600 bg-black-100 border-black-300 rounded focus:ring-indigo-500 dark:focus:ring-indigo-600 dark:ring-offset-black-800 focus:ring-2 dark:bg-black-700 dark:border-black-600 mr-4 mt-2"
                  value={`opcao${verse.number}`}
                />
                <div className="flex-grow">
                  <h3 className="sm:text-2xl lg:text-sm mb-1" id={`verse-${verse.number}`}>{verse.text}</h3>
                  <h4 className="sm:text-lg lg:text-xs text-indigo-300 italic" id={`verselocal-${verse.number}`}>
                    {verse.book} - {verse.chapter}:{verse.number}
                  </h4>
                </div>
                <button className="text-indigo-300 flex-shrink-0 ml-2">
                  <svg stroke="currentColor" strokeWidth="2" fill="none" strokeLinecap="round" strokeLinejoin="round" className="w-6 h-6" viewBox="0 0 24 24">
                    <circle cx="12" cy="12" r="1"/>
                    <circle cx="19" cy="12" r="1"/>
                    <circle cx="5" cy="12" r="1"/>
                  </svg>
                </button>
              </div>
            ))}
          </form>
        </div>
      </div>
    </div>
  );
}

export default VersesSection;
