import React from 'react';
import { Route, Routes } from '../../node_modules/react-router-dom/dist/index';
import Home from '../home/Home';

const AppRouter = () => {
	return (
		<Routes>
			<Route
				index
				element={<Home />}
			/>
			{/* <Route
				path="/login"
				element={<smt />}
			/> */}
		</Routes>
	);
};

export default AppRouter;
