import './App.css';
import { useMode } from '../theme/index';
import { Button, CssBaseline, ThemeProvider } from '@mui/material';
import SendIcon from '@mui/icons-material/Send';

import React from 'react';
import AppRouter from './AppRouter';

function App() {
	const [theme, colorMode] = useMode();
	return (
		<ThemeProvider theme={theme}>
			<CssBaseline />
			<div>
				<div className="App">
					<Button
						variant="contained"
						color="warning"
						endIcon={<SendIcon />}
						onClick={colorMode.toggleColorMode}
					>
						Toggle Theme
					</Button>
					<AppRouter />
				</div>
			</div>
		</ThemeProvider>
	);
}

export default App;
