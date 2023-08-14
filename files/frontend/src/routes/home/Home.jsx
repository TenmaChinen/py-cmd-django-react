import React, { Fragment } from 'react'
import HelloWorld from './../../components/hello-world/HelloWorld'
import styles from './Home.module.css';
import Base from '../base/Base';

function Home() {

  return (
    <Base
      navContent={
        <Fragment>
          <h1>Home</h1>
        </Fragment>
      }
      mainContent={
        <div className={styles.container}>
          <h1>HOME PAGES</h1>
          <HelloWorld />
        </div>
      }
    />
  );
}

export default Home;