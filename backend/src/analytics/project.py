import pandas as pd
import numpy as np
from collections import Counter
import re
import os
from datetime import datetime
import math
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import copy
import statistics
import json
from sklearn.preprocessing import LabelEncoder

#Загрузка таблиц
file_path = "backend/src/Таблицы/answers.xlsx"
initial_df = pd.read_excel(file_path)
#------------------------------------------------------------------------------------------------------------
# Предобработка данных
initial_df[initial_df.columns] = initial_df[initial_df.columns].astype(str)
initial_df = initial_df.loc[:, :initial_df.columns[34]]
initial_df[initial_df.columns[4:16]] = initial_df[initial_df.columns[4:16]].apply(pd.to_numeric, errors='coerce').astype('Int32')
initial_df.columns = [col.split(" ", 1)[1] if " " in col else col for col in initial_df.columns]
initial_df = initial_df.replace("nan", "Нет ответа")

profession = initial_df.columns[-1] #ПРОФЕССИЯ

initial_df.drop("Какие методы популяризации закаливания организма Вы считаете наиболее эффективными (не более 3 вариантов):", axis=1, inplace=True)
initial_df.drop("Укажите Вашу профессию:", axis=1, inplace=True)
#------------------------------------------------------------------------------------------------------------
# Определение допустимых значений для первого столбца
valid_values = [
    "Средство повышения устойчивости организма к воздействию стрессовых факторов",
    "Возможность вести здоровый образ жизни",
    "Вид спорта и хобби",
    "Популярный способ укрепить иммунитет",
    "Круг союзников и друзей, интересные люди",
    "Способ почувствовать безопасность и обрести спокойствие",
    "Альтернатива медикаментозному лечению",
    "Метод физиотерапии"
]

# Замена значений, не входящих в список допустимых значений
initial_df["Для Вас закаливание и зимнее плавание - это:"] = np.where(
    initial_df["Для Вас закаливание и зимнее плавание - это:"].isin(valid_values),
    initial_df["Для Вас закаливание и зимнее плавание - это:"],
    "Другое"  # Замена на "Другое" для всех неподходящих значений
)
#------------------------------------------------------------------------------------------------------------
# Определение допустимых значений для столбца ["Из каких источников Вы чаще всего получаете информацию по теме закаливания организма (не более 3 вариантов):"]
valid_sources = [
    "Статьи/блоги в интернете",
    "Тематические паблики/сообщества в социальных сетях",
    "Электронная рассылка",
    "Книги и журналы о здоровом образе жизни и закаливании",
    "Консультации с врачами и специалистами по физической культуре",
    "Советы опытных зимних пловцов, знакомых"
]

# Находим самый часто встречаемый ответ, который не является 'nan'
most_common_answer = initial_df["Из каких источников Вы чаще всего получаете информацию по теме закаливания организма (не более 3 вариантов):"].value_counts().idxmax()

# Замена значений, не входящих в список допустимых значений
initial_df["Из каких источников Вы чаще всего получаете информацию по теме закаливания организма (не более 3 вариантов):"] = np.where(
    initial_df["Из каких источников Вы чаще всего получаете информацию по теме закаливания организма (не более 3 вариантов):"].isin(valid_sources),
    initial_df["Из каких источников Вы чаще всего получаете информацию по теме закаливания организма (не более 3 вариантов):"],
    f"Другое ({most_common_answer})"  # Замена на "Другое" с добавлением наиболее часто встречаемого ответа
)

#------------------------------------------------------------------------------------------------------------
#Обработка таблицы для корреляции
correlation_table = initial_df.copy()

encoding_dict = {}

# Задаем диапазоны столбцов
columns_to_encode = list(correlation_table.columns[:4]) + list(correlation_table.columns[17:])

# Обработка каждого столбца из заданного диапазона
for column in columns_to_encode:
    # Инициализация LabelEncoder
    encoder = LabelEncoder()
    
    # Применяем LabelEncoder к столбцу
    correlation_table[column] = encoder.fit_transform(correlation_table[column])
    
    # Создаем словарь для столбца, где ключ - оригинальное значение, значение - закодированное значение
    encoding_dict[column] = dict(zip(encoder.classes_, encoder.transform(encoder.classes_)))
#------------------------------------------------------------------------------------------------------------

# print(correlation_table["Основные физиологические эффекты от закаливания, которые Вы получили (1 – эффект выражен минимально, 5 – эффект выражен максимально): [Улучшение самочувствия]"][15:60])
# print(initial_df.columns[4:16].to_list())
print(encoding_dict)