import { Box, Button, Card, CardActions, CardContent, TextField, Typography } from '@mui/material';
import React, { useContext } from 'react';
import { useNavigate } from 'react-router-dom';

import { clgContext } from '../theme';

const Form = () => {
	const { logi } = useContext(clgContext);
	const navigate = useNavigate();

	const card = (
		<React.Fragment>
			<CardContent>
				<Typography
					variant="h5"
					component="div"
					sx={{ borderBottom: '1px solid' }}
				>
					Регион Здоровья
				</Typography>
				<Typography
					gutterBottom
					sx={{ mt: 2 }}
				>
					Введите данные в форму
				</Typography>

				<TextField
					id="name-form"
					label="Имя"
					variant="standard"
					color="info"
					type="email"
				/>
				<TextField
					sx={{ ml: 5 }}
					id="mail-form"
					label="Email"
					variant="standard"
					color="info"
					type="email"
				/>
				<Typography sx={{ color: 'text.secondary', mt: 5 }}>еще какая то инфа</Typography>
				<TextField
					id="name-form"
					label="Имя"
					variant="standard"
					color="info"
					type="email"
				/>
				<TextField
					sx={{ ml: 5 }}
					id="mail-form"
					label="Email"
					variant="standard"
					color="info"
					type="email"
				/>
				<Typography
					sx={{ mt: 2 }}
					variant="body2"
				>
					тут можно что то про
					<br />
					{'конфиденциальность написать'}
				</Typography>
			</CardContent>
			<CardActions sx={{ display: 'flex', justifyContent: 'space-between' }}>
				<Button
					size="small"
					color="secondary"
					variant="outlined"
				>
					Узнать о
				</Button>
				<Button
					size="small"
					color="info"
					variant="contained"
				>
					Отправить форму
				</Button>
			</CardActions>
		</React.Fragment>
	);

	return (
		<div
			style={{
				display: 'flex',
				justifyContent: 'center',
				alignItems: 'center',
				flexDirection: 'column',
				height: '70vh',
			}}
		>
			<Button
				variant="contained"
				color="info"
				onClick={() => navigate('/')}
			>
				to Home
			</Button>
			{/* <Button
				variant="contained"
				color="error"
				onClick={() => logi('Context')}
			>
				Context
			</Button> */}

			<h1>Пример формы</h1>

			<Box sx={{ minWidth: 350 }}>
				<Card variant="outlined">{card}</Card>
			</Box>
		</div>
	);
};

export default Form;
