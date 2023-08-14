import React from 'react'
import { Link } from 'react-router-dom';
import logo from '../../assets/logo.svg';
import './NavBar.style.scss';

export default function NavBar() {

  return (
    <nav>
      <Link className='logo-title' to='/home'>
        <img src={logo} width={40} />
        <span>Home</span>
      </Link>
      
      <div className='links'>
        <Link to='/foo'>FOO</Link>
      </div>
    </nav>
  );
}
