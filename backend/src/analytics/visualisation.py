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

for col, result in project.practiced_types_results.items():
    create_table(result, f'Самый популярный тип закаливания')

for col, result in project.practice_breaks_results.items():
    create_table(result, f'Самый популярный перерыв практики')

for col, result in project.motives_results.items():
    create_table(result, f'Самый популярный мотив закаливания')

for col, result in project.negative_factors_results.items():
    create_table(result, f'Самый популярный негативный фактор')

for col, result in project.promotion_methods_results.items():
    create_table(result, f'Самый популярный метод популяризации закаливания')

for col, result in project.information_sources_results.items():
    create_table(result, f'Самый популярный источник информации')