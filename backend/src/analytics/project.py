import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from collections import Counter

#Загрузка таблиц
file_path = "tables/2024-10-30 Zakalivanie i zimnee plavanie.xlsx"
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

# Список столбцов для группировки
columns = ['Пол', 'Возраст', 'Регион', 'Семейное_положение', 'Деятельность', 'Профессия']

# Функция для предварительной обработки столбца (разделение и очистка)
def prepare_column(df, characteristic_col):
    """
    Разделяет значения по ';' и удаляет лишние пробелы в указанном столбце.
    """
    processed_df = df.copy()
    processed_df = processed_df.assign(
        **{characteristic_col: processed_df[characteristic_col].str.split(';')}
    ).explode(characteristic_col)
    processed_df[characteristic_col] = processed_df[characteristic_col].str.strip()
    return processed_df

# Функция для нахождения самого популярного значения в каждом столбце для каждого значения в columns
def find_most_common_type_per_value(df, group_col, characteristic_col):
    return (
        df.groupby(group_col)[characteristic_col]
        .agg(lambda x: x.mode().iloc[0] if not x.mode().empty else None)
        .reset_index()
        .rename(columns={characteristic_col: f'Самый популярный {characteristic_col} для {group_col}'})
    )

# Обработка и нахождение результатов для каждого столбца отдельно
# Мотивы закаливания
motives_table = prepare_column(df, 'Мотивы закаливания')
motives_results = {col: find_most_common_type_per_value(motives_table, col, 'Мотивы закаливания') for col in columns}

# Негативные факторы
negative_factors_table = prepare_column(df, 'Негативные факторы')
negative_factors_results = {col: find_most_common_type_per_value(negative_factors_table, col, 'Негативные факторы') for col in columns}

# Методы популяризации закаливания
promotion_methods_table = prepare_column(df, 'Методы популяризации закаливания')
promotion_methods_results = {col: find_most_common_type_per_value(promotion_methods_table, col, 'Методы популяризации закаливания') for col in columns}

# Источники информации по теме закаливание
information_sources_table = prepare_column(df, 'Источники информации по теме закаливание')
information_sources_results = {col: find_most_common_type_per_value(information_sources_table, col, 'Источники информации по теме закаливание') for col in columns}

# Перерывы практики
practice_breaks_table = prepare_column(df, 'Перерывы_практики')
practice_breaks_results = {col: find_most_common_type_per_value(practice_breaks_table, col, 'Перерывы_практики') for col in columns}

# Практикуемые типы закаливания
practiced_types_table = prepare_column(df, 'Практикуемые типы закаливания')
practiced_types_results = {col: find_most_common_type_per_value(practiced_types_table, col, 'Практикуемые типы закаливания') for col in columns}

# Вывод результатов
# print("\nРезультаты для 'Мотивы закаливания':")
# for col, result in motives_results.items():
#     print(f"\nСамый популярный мотив закаливания для '{col}':")
#     print(result)

# print("\nРезультаты для 'Негативные факторы':")
# for col, result in negative_factors_results.items():
#     print(f"\nСамый популярный негативный фактор для '{col}':")
#     print(result)

# print("\nРезультаты для 'Методы популяризации закаливания':")
# for col, result in promotion_methods_results.items():
#     print(f"\nСамый популярный метод популяризации закаливания для '{col}':")
#     print(result)

# print("\nРезультаты для 'Источники информации по теме закаливание':")
# for col, result in information_sources_results.items():
#     print(f"\nСамый популярный источник информации для '{col}':")
#     print(result)

# print("\nРезультаты для 'Перерывы практики':")
# for col, result in practice_breaks_results.items():
#     print(f"\nСамый популярный перерыв практики для '{col}':")
#     print(result)

# print("\nРезультаты для 'Практикуемые типы закаливания':")
# for col, result in practiced_types_results.items():
#     print(f"\nСамый популярный тип закаливания для '{col}':")
#     print(result)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

#4

# Определение столбцов с эффектами и группировки
effect_columns = df.loc[:, 'Эффект_самочувствие':'Психоэффект_тревога'].columns
group_columns = ['Период_практики', 'Перерывы_практики', 'Практикуемые типы закаливания']

# Функция для нахождения столбцов с максимальным количеством "5" для заданного столбца группировки
def get_sorted_effect_counts_overall(df, group_col):
    # Преобразуем значения "5" в 1, остальные в 0
    filtered_df = df[effect_columns].applymap(lambda x: 1 if x == 5 else 0)
    
    # Добавляем столбец группировки и считаем сумму значений "5" по столбцам с эффектами
    grouped_counts = pd.concat([df[group_col], filtered_df], axis=1).groupby(group_col)[effect_columns].sum()
    
    # Суммируем общее количество "5" по всем значениям группы
    total_counts = grouped_counts.sum(axis=0).sort_values(ascending=False)
    
    # Создаем список кортежей (название столбца, количество "5"), отсортированных по убыванию
    sorted_effect_counts = [(col, count) for col, count in total_counts.items()]
    
    return sorted_effect_counts

# Создаем результаты для каждого группирующего столбца
results_period_practica = get_sorted_effect_counts_overall(df, 'Период_практики')
results_breaks_practica = get_sorted_effect_counts_overall(df, 'Перерывы_практики')
results_types_practica = get_sorted_effect_counts_overall(df, 'Практикуемые типы закаливания')

# Вывод результатов
print("\nРезультаты для 'Период_практики':")
print(results_period_practica)

print("\nРезультаты для 'Перерывы_практики':")
print(results_breaks_practica)

print("\nРезультаты для 'Практикуемые типы закаливания':")
print(results_types_practica)
