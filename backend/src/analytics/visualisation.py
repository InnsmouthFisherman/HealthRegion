import matplotlib.pyplot as plt
import pandas as pd
import project

# Функция для создания таблицы
def create_table(data, title):
    fig, ax = plt.subplots(figsize=(10, len(data)/2))
    ax.axis('off')  # Отключаем оси

    # Создаем таблицу
    table = ax.table(cellText=data.values, colLabels=data.columns, cellLoc='center', loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.5)

    plt.title(title)
    plt.show()

# Создаем таблицы для results_tipi_zakalivania
for col, result in project.results_tipi_zakalivania.items():
    create_table(result, f'Самый популярный тип закаливания')

# Создаем таблицы для results_pirif_practica
for col, result in project.results_pirif_practica.items():
    create_table(result, f'Самый популярный перерыв практики')