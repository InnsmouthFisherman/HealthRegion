import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from collections import Counter

#Загрузка таблиц
file_path = "backend/src/Таблицы/2024-10-30 Zakalivanie i zimnee plavanie.xlsx"
initial_df = pd.read_excel(file_path)
df = initial_df.copy()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#Предобработка данных
#Замена названия столбцов на более короткое
df.drop("Наше социологическое исследование посвящено изучению вопросов, связанных с мотивацией и популяризацией закаливания организма. Пройти опрос можно только один раз. Просим Вас ответить на вопросы и благодарим за участие.", axis=1, inplace=True)
short_column_names = [
    'Закаливание_мнение', 'Мотив_иммунитет', 'Мотив_адаптация', 
    'Мотив_системы', 'Мотив_обмен', 'Мотив_работоспособность', 'Мотив_ЗОЖ', 
    'Мотив_спорт', 'Мотив_соревнования', 'Мотив_жизненная_ситуация', 'Мотив_вызов',
    'Фактор_непонимание', 'Фактор_негативный_опыт', 'Фактор_отсутствие_поддержки',
    'Фактор_информация', 'Фактор_страх', 'Фактор_время', 'Фактор_инфраструктура',
    'Фактор_удаленность', 'Фактор_инструкторы', 'Возраст_начала', 'Эффект_самочувствие',
    'Эффект_заболеваемость', 'Эффект_работоспособность', 'Эффект_организм',
    'Эффект_устойчивость', 'Эффект_органы', 'Эффект_ремиссия', 'Эффект_энергия',
    'Эффект_качество_жизни', 'Психоэффект_стресс', 'Психоэффект_самоконтроль',
    'Психоэффект_настроение', 'Психоэффект_привычка', 'Психоэффект_память', 'Психоэффект_тревога',
    'Уверенность_адаптация', 'Типы_обтирание', 'Типы_обливание', 'Типы_душ',
    'Типы_босохождение', 'Типы_баня', 'Типы_воздух', 'Типы_бег', 'Типы_прорубь',
    'Типы_плавание', 'Период_практики', 'Частота_практики', 'Перерывы_практики', 
    'Способ_практики', 'Сочетание_баня', 'Источники_интернет_статьи', 'Источники_соцсети',
    'Источники_рассылка', 'Источники_литература', 'Источники_консультации', 
    'Источники_советы', 'Источники_мероприятия', 'Метод_онлайн_ресурсы',
    'Метод_соцсети', 'Метод_семинары', 'Метод_группы', 'Метод_информационные_материалы',
    'Метод_сотрудничество', 'Метод_мессенджеры', 'Пол', 'Возраст', 'Регион',
    'Семейное_положение', 'Деятельность', 'Образование', 'Профессия'
]
df.columns = short_column_names

#Объединение большого количества столбцов в один, чтобы не было много пропущенных значений
df['Мотивы закаливания'] = df.iloc[:, 1:11].apply(lambda row: '; '.join(row.dropna().astype(str)), axis=1)
df['Негативные факторы'] = df.iloc[:, 11:21].apply(lambda row: '; '.join(row.dropna().astype(str)), axis=1)
df['Практикуемые типы закаливания'] = df.loc[:, "Типы_обтирание":"Типы_плавание"].apply(lambda row: '; '.join(row.dropna().astype(str)), axis=1)
df["Источники информации по теме закаливание"] =  df.loc[:, "Источники_интернет_статьи":"Источники_мероприятия"].apply(lambda row: '; '.join(row.dropna().astype(str)), axis=1)
df["Методы популяризации закаливания"] = df.loc[:, "Метод_онлайн_ресурсы":"Метод_мессенджеры"].apply(lambda row: '; '.join(row.dropna().astype(str)), axis=1)
df["Общее количество баллов самочувствия после закаливания"] = df.loc[:, "Эффект_самочувствие":"Психоэффект_тревога"].sum(axis=1)


#Удаление объединенных столбцов
df.drop(columns=['Мотив_иммунитет', 'Мотив_адаптация', 'Мотив_системы', 'Мотив_обмен', 'Мотив_работоспособность', 
                 'Мотив_ЗОЖ', 'Мотив_спорт', 'Мотив_соревнования', 'Мотив_жизненная_ситуация', 'Мотив_вызов'], inplace=True)

df.drop(columns=['Фактор_непонимание', 'Фактор_негативный_опыт', 'Фактор_отсутствие_поддержки', 'Фактор_информация', 
                 'Фактор_страх', 'Фактор_время', 'Фактор_инфраструктура', 'Фактор_удаленность', 'Фактор_инструкторы'], inplace=True)

df.drop(columns=['Типы_обтирание', 'Типы_обливание', 'Типы_душ', 'Типы_босохождение', 'Типы_баня', 
                 'Типы_воздух', 'Типы_бег', 'Типы_прорубь', 'Типы_плавание'], inplace=True)

df.drop(columns=['Источники_интернет_статьи', 'Источники_соцсети', 'Источники_рассылка', 'Источники_литература', 
                 'Источники_консультации', 'Источники_советы', 'Источники_мероприятия'], inplace=True)

df.drop(columns=['Метод_онлайн_ресурсы', 'Метод_соцсети', 'Метод_семинары', 'Метод_группы', 'Метод_информационные_материалы', 
                 'Метод_сотрудничество', 'Метод_мессенджеры'], inplace=True)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#Обработка таблицы для корреляции
correlation_table = df.copy()
correlation_table.drop(columns=correlation_table.columns[2:17], inplace=True)
encoding_dict = {}

for column in correlation_table.columns:
    if column != "Общее количество баллов самочувствия после закаливания":
        encoder = LabelEncoder()
        correlation_table[column] = encoder.fit_transform(correlation_table[column].astype(str))
        encoding_dict[column] = dict(zip(encoder.classes_, encoder.transform(encoder.classes_)))

# Расчет корреляции
correlation_matrix = correlation_table.corr()
correlated_columns = correlation_matrix["Общее количество баллов самочувствия после закаливания"].abs().sort_values(ascending=False)

# Находим 5 столбцов с наибольшей корреляцией
top_5_columns = correlated_columns.index[1:6]  # Пропускаем сам столбец "Общее количество баллов самочувствия"

# Поиск двух самых встречаемых значений в каждом из топ-5 столбцов и добавление ранга значимости
result_corr = []
for rank, col in enumerate(top_5_columns, start=1):
    value_counts = df[col].value_counts().nlargest(2)
    most_common_values = value_counts.index.tolist()
    significance_text = f"Ранг значимости {rank}, где чем выше ранг, тем значимее признак"
    result_corr.append((col, significance_text, most_common_values))


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#Нахождение моды для каждой столбца
columns_mode = []

# Функция для нахождения моды столбца
def find_mode(column):
    counter = Counter(column)
    most_common = counter.most_common()
    
    # Если мода 'Не указано', берем второе по популярности слово
    if most_common[0][0] == 'Не указано' and len(most_common) > 1:
        return most_common[1][0]
    else:
        return most_common[0][0]

# Проходим по каждой колонке и находим моду до -6 индекса столбца
for column in df.columns[:-5]:
    mode_value = find_mode(df[column])
    columns_mode.append((column, mode_value))

# Проходим по каждой колонке и находим моду от -5 индекса столбца
for col in df.columns[-5:-1]:
    values_list = []  # Временный список для хранения значений из одного столбца
    
    # Проход по каждой ячейке столбца
    for value in df[col]:
        if pd.notna(value):  # Проверка на ненулевое значение
            split_values = value.split(';')  # Разделение строки по символу ";"
            values_list.extend(split_values)  # Добавление значений в список
    
    # Поиск моды для текущего столбца
    if values_list:
        mode_value = Counter(values_list).most_common(1)[0][0]  # Нахождение наиболее частого элемента
        columns_mode.append((col, mode_value))  # Добавление кортежа в список

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#Функции для аналитики

def find_most_common_type_per_value(df, group_col, characteristic_col):
    """
    Функция для нахождения самого популярного значения в столбце characteristic_col для каждого значения в столбце group_col.
    """
    return (
        df.groupby(group_col)[characteristic_col]
        .agg(lambda x: x.mode().iloc[0] if not x.mode().empty else None)
        .reset_index()
        .rename(columns={characteristic_col: f'Самый популярный {characteristic_col} для {group_col}'})
    )

# Список столбцов для группировки
columns_practica = ['Пол', 'Возраст', 'Регион', 'Семейное_положение', 'Деятельность', 'Профессия']

# Список характеристических столбцов для анализа
characteristics_columns = [
    'Мотивы закаливания', 
    'Негативные факторы', 
    'Методы популяризации закаливания', 
    'Источники информации по теме закаливание',
    'Перерывы_практики',
    'Практикуемые типы закаливания'
]

# Создание словаря для хранения результатов
results_characteristics = {}

# Применение для каждого характеристического столбца
for characteristic in characteristics_columns:
    # Разделение данных по знаку ";"
    table_characteristic = df.copy()
    table_characteristic = table_characteristic.assign(
        **{characteristic: table_characteristic[characteristic].str.split(';')}
    ).explode(characteristic)
    
    # Удаление лишних пробелов в значениях
    table_characteristic[characteristic] = table_characteristic[characteristic].str.strip()
    
    # Создание словаря для текущей характеристики
    results_characteristics[characteristic] = {}
    
    # Нахождение самого популярного значения для каждого столбца из columns_practica
    for col in columns_practica:
        results_characteristics[characteristic][col] = find_most_common_type_per_value(table_characteristic, col, characteristic)

# Вывод результатов
# for characteristic, results in results_characteristics.items():
#     print(f"\nРезультаты для '{characteristic}':")
#     for col, result in results.items():
#         print(f"\nСамый популярный {characteristic} для '{col}':")
#         print(result)

print(results_characteristics["Перерывы_практики"])