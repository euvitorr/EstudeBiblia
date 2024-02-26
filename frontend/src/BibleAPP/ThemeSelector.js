import React, { useState, useEffect } from 'react';

function ThemeSelector() {
  const [theme, setTheme] = useState('');

  useEffect(() => {
    const savedTheme = localStorage.getItem('theme') || 'indigo';
    setTheme(savedTheme);
    applyTheme(savedTheme);
  }, []);

  const changeTheme = (newTheme) => {
    setTheme(newTheme);
    localStorage.setItem('theme', newTheme);
    applyTheme(newTheme);
  };

  const applyTheme = (themeName) => {
    document.documentElement.classList.remove('gray', 'red', 'orange', 'green', 'teal', 'blue', 'indigo', 'purple', 'pink');
    document.documentElement.classList.add(themeName);
  };

  return (
    <div className="fixed h-screen right-0 top-0 items-center flex">
      <div>
        <div className="p-2 bg-white border-l-4 border-t-4 border-b-4 border-indigo-400 inline-flex items-center rounded-tl-lg shadow-2xl rounded-bl-lg z-10 flex-col">
          {['gray', 'red', 'orange', 'green', 'teal', 'blue', 'indigo', 'purple', 'pink'].map((color) => (
            <button key={color} onClick={() => changeTheme(color)} className={`bg-${color}-500 w-6 h-6 rounded-full mb-4 outline-none focus:outline-none`}></button>
          ))}
        </div>

        <div className="p-2 bg-white border-l-4 border-t-4 border-b-4 border-indigo-400 items-center rounded-tl-lg shadow-2xl rounded-bl-lg z-10 flex-col">
          <button className="outline-none focus:outline-none" id="openModal">
            <i className="fas fa-pencil-alt text-indigo-600"></i>
          </button>
        </div>
      </div>
    </div>
  );
}

export default ThemeSelector;
