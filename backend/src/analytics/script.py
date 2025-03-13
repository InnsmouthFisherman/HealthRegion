import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from collections import Counter
import re

#Загрузка таблиц

file_path = "backend/src/analytics/tables/2024-10-30 Zakalivanie i zimnee plavanie.xlsx"
initial_df = pd.read_excel(file_path)
df = initial_df.copy()

df = df.fillna('пусто')


