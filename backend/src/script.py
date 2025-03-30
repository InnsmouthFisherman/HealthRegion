import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from collections import Counter
import re

def validate_table(file_path):
   
    initial_df = pd.read_csv(file_path)
    df = initial_df.copy()

    df = df.fillna('пусто')


