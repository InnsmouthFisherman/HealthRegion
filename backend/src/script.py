import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from collections import Counter
import re
from collections import defaultdict

# def validate_table(file_path):
   
#     initial_df = pd.read_csv(file_path)
#     df = initial_df.copy()

#     df = df.fillna('пусто')

file_path = 'C:\Users\Maxim K\Desktop\HealthRegion-main\backend\src\tables\test2.csv'

# table = validate_table(file_path)

def group_columns_by_prefix(df):
    column_groups = defaultdict(list)
    
    for col in df.columns:
        if '/' in col:
            group_key = col.split('/', 1)[0].strip()
            column_groups[group_key].append(col)
    
    return column_groups

def merge_grouped_columns(df, column_groups):
    merged_data = {}
    
    for group_key, cols in column_groups.items():
        if len(cols) > 1:  # Объединяем только если есть дубликаты
            merged_data[group_key] = df[cols].apply(lambda x: ', '.join(x.dropna().astype(str).str.strip()), axis=1)
    
    return merged_data

# Загрузка данных
file_path = 'C:\Users\Maxim K\Desktop\HealthRegion-main\backend\src\tables\test2.csv'
df = pd.read_excel(file_path)

# Группировка и объединение столбцов
column_groups = group_columns_by_prefix(df)
merged_data = merge_grouped_columns(df, column_groups)

# Удаление исходных столбцов
columns_to_drop = [col for cols in column_groups.values() for col in cols]
df = df.drop(columns=columns_to_drop)

# Добавление объединенных столбцов
for col_name, col_data in merged_data.items():
    df[col_name] = col_data

# Теперь df содержит обновленные данные
print(df.columns)