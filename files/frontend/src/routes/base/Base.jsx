import React, { Fragment } from 'react';
// import { Outlet } from 'react-router-dom';
import NavBar from '../../components/navbar/NavBar';

import './Base.css';

function Base( {navContent, mainContent}) {
  return (
    <div className='base-container'>
      <NavBar content={navContent}/>
      <main>
        {mainContent}
      </main>
    </div>
  );
}

export default Base;