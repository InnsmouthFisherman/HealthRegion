import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';

const initialState = {
	items: {},
	isLoading: false,
};

export const getsmtItems = createAsyncThunk('smtItems/getsmtItems', async (_, thunkAPI) => {});

const smtItemsSlice = createSlice({
	name: 'smtItems',
	initialState,

	extraReducers: builder => {
		builder
			.addCase(getsmtItems.pending, state => {
				state.isLoading = true;
			})
			.addCase(getsmtItems.fulfilled, (state, { payload }) => {
				state.isLoading = false;
				state.items = payload;
			})
			.addCase(getsmtItems.rejected, state => {
				state.isLoading = false;
			});
	},
});

export default smtItemsSlice.reducer;
