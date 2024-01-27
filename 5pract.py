import pandas as pd
# Чтение данных из CSV файла в датафрейм
df = pd.read_csv('D:/Тютин/работы/anime.csv')
# Вывод первых пяти строк датафрейма
print("1. Весь датасет:")
print(df)
# Вывод размерности массива (количество строк и столбцов)
print("\n2. Размерность массива:")
print(df.shape)
# Вывод наименования и описания колонок
print("\n3. Наименование и описание колонок:")
print(df.columns)
print(df.describe())
# Вывод уникальных значений по каждой колонке
print("\n4. Уникальные значения:")
print(df.nunique())
# Сортировка по столбцу 'place' в порядке убывания
print("\n5. Сортировка по определенным параметрам:")
df_sorted = df.sort_values(by='place', ascending=False)
print(df_sorted.head())
# Удаление ненужных столбцов 'is_verified' и 'player_pronouns'
print("\n6. Удаление ненужных столбцов:")
df = df.drop(['is_verified', 'player_pronouns'], axis=1)
print(df.head())
# Удаление дубликатов
print("\n7. Удаление дубликатов:")
df = df.drop_duplicates()
print(df.head())
# Замена значений 'es' на 'ru' в столбце 'player_country'
print("\n8. Замена определенных значений:")
df['player_country'].replace({'es': 'ru'}, inplace=True)
print(df.head())
# Анализ с использованием функций info
print("\n9. Анализ с помощью функций info:")
print(df.info())
# Анализ с использованием функций describe
print("\n10. Анализ с помощью функций describe:")
print(df.describe())
# Выборка данных по условию (строки с 'place' > 3 и столбцы 'speedrun_time', 'player_signup_date')
print("\n11. Выборка данных по строкам и столбцам с помощью loc:")
selected_data = df.loc[df['place'] > 3, ['speedrun_time', 'player_signup_date']]
print(selected_data.head())
# Сохранение нового датасета в CSV файл
print("\n12. Сохранение нового датасета")
df.to_csv('speedrun.csv', index=False)