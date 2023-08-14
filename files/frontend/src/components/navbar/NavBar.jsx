import React from 'react'
import { Link } from 'react-router-dom';
import logo from '../../assets/logo.svg';
import './NavBar.scss';

function NavBar({content}) {

  return (
    <nav>
      <ul className='links'>
        <Link className='logo-title' to='/home'>
          <img src={logo} width={30} />
        </Link>
        {content}
      </ul>
      
      <div className='links'>
        <Link to='/home'>Home</Link>
        <Link to='/foo'>Foo</Link>
      </div>
    </nav>
  );
}

export default NavBar;