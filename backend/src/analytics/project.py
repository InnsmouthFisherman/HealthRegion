import pandas as pd
import numpy as np

file_path = "answers.xlsx"

initial_df = pd.read_excel(file_path)

initial_df[initial_df.columns] = initial_df[initial_df.columns].astype(str)
initial_df = initial_df.loc[:, :initial_df.columns[34]]
initial_df.columns = [col[3:] for col in initial_df.columns]

# initial_df[initial_df.columns[4:16]] = initial_df[initial_df.columns[4:16]].apply(pd.to_numeric, errors='coerce').astype('Int32')

print(initial_df.columns.to_list())
