import React from 'react';
import BackgroundShapes from './BackgroundShapes';
import ContentArea from './ContentArea';

function MainContent() {
  return (
    <div className="h-screen w-screen bg-indigo-400 overflow-hidden absolute flex items-center">
      <BackgroundShapes />
      <ContentArea />
    </div>
  );
}

export default MainContent;
