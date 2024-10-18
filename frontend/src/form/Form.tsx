import { Box, Button, Card, CardActions, CardContent, Typography } from '@mui/material';
import React from 'react';

const Form = () => {
	const card = (
		<React.Fragment>
			<CardContent>
				<Typography gutterBottom>Word of the Day</Typography>
				<Typography
					variant="h5"
					component="div"
				>
					be - nev - olent
				</Typography>
				<Typography sx={{ color: 'text.secondary', mb: 1.5 }}>adjective</Typography>
				<Typography variant="body2">
					well meaning and kindly.
					<br />
					{'"a benevolent smile"'}
				</Typography>
			</CardContent>
			<CardActions>
				<Button
					size="small"
					color="secondary"
				>
					Learn More
				</Button>
			</CardActions>
		</React.Fragment>
	);
	return (
		<div>
			<p>oein</p>
			<Button
				variant="contained"
				color="error"
			>
				Hello form
			</Button>
			<h1>smt txt</h1>

			<Box sx={{ minWidth: 275 }}>
				<Card variant="outlined">{card}</Card>
			</Box>
		</div>
	);
};

export default Form;
