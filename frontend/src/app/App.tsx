import './App.css';
import { ColorModeContext, useMode } from '../theme/index';
import { CssBaseline, ThemeProvider } from '@mui/material';

import React from 'react';
import AppRouter from './AppRouter';

function App() {
	const [theme, colorMode] = useMode();
	return (
		<ThemeProvider theme={theme}>
			<CssBaseline />
			<div>
				<div className="App-info">
					<AppRouter />
				</div>
			</div>
		</ThemeProvider>
	);
}

export default App;
