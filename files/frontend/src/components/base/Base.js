import React, { Fragment } from 'react';
import { Outlet } from 'react-router-dom';
import NavBar from "../navbar/NavBar";
import './Base.style.css';

export default function Base() {
  return (
    <Fragment>
      <NavBar />
      <main>
        <Outlet />
      </main>
    </Fragment>
  );
}