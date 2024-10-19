import { Button } from '@mui/material';
import React from 'react';
import { useNavigate } from 'react-router-dom';

const Home = () => {
	const navigate = useNavigate();
	return (
		<div>
			<Button
				className=""
				variant="outlined"
				color="info"
				onClick={() => navigate('/form')}
			>
				to forms
			</Button>
		</div>
	);
};

export default Home;
