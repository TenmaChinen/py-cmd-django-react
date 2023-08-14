import React, { Fragment } from 'react'

import style from './Foo.module.scss';
import Base from './../base/Base';
import { getFooList } from '../../api/foo.api';


function Foo() {

  const [ fooItems, setFooItems ] = React.useState( [] );

  React.useEffect( () => {
    async function loadFooList() {
      const fooItemArray = await getFooList();
      setFooItems( fooItemArray );
    }
    loadFooList();
  }, [] );

  return (
    <Base
      navContent={
        <Fragment>
          <h1>Foo</h1>
        </Fragment>
      }
      mainContent={
        <div className={style.container}>
          <ul>
            {fooItems.map( ( fooItem, idx ) => {
              return <li key={idx} >{fooItem}</li>
            } )}
          </ul>
        </div>
      }
    />
  );
}

export default Foo;