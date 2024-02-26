import React from 'react';

function UserProfile({ user }) {
  return (
    <div>
      <div className="p-8 shadow-md relative bg-white">
        <div className="flex items-center">
          <img src={user.image} className="w-10 h-10 block rounded object-cover object-top" alt="Profile" />
          <div className="text-indigo-600 font-medium ml-3">{user.name}</div>
          <button className="bg-indigo-100 text-indigo-400 ml-auto w-8 h-8 flex items-center justify-center rounded">
            <svg stroke="currentColor" className="w-4 h-4" viewBox="0 0 24 24" strokeWidth="2.2" fill="none" strokeLinecap="round" strokeLinejoin="round">
              <path d="M18 8A6 6 0 006 8c0 7-3 9-3 9h18s-3-2-3-9M13.73 21a2 2 0 01-3.46 0"/>
            </svg>
          </button>
        </div>
      </div>
    </div>
  );
}

export default UserProfile;
