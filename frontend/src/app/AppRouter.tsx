import React from 'react';
import { Route, Routes } from '../../node_modules/react-router-dom/dist/index';
import Home from '../home/Home';
import Form from '../form/Form';

const AppRouter = () => {
	return (
		<Routes>
			<Route
				index
				element={<Home />}
			/>
			<Route
				path="/form"
				element={<Form />}
			/>
		</Routes>
	);
};

export default AppRouter;
