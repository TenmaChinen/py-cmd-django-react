import React from 'react'
import { Routes, Route } from 'react-router-dom'
import Home from './routes/home/Home'
import Foo from './routes/foo/Foo'

export default function App() {
	return (
		<Routes>
			<Route path='/home' element={<Home />} />
			<Route path='/foo' element={<Foo />} />
		</Routes>
	);
}